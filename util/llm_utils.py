#import necessary libraries
import re
import json
import ollama
import hashlib
import logging
from pathlib import Path
from types import MethodType
from collections import defaultdict
from tools.init import TOOL_SCHEMAS
from tools.tool_runner import run_tool

#create deterministic seed based on string input
ollama_seed = lambda x: int(str(int(hashlib.sha512(x.encode()).hexdigest(), 16))[:8])

#convert list of chat messages to a readable string format
def pretty_stringify_chat(messages):
  stringified_chat = ''
  for message in messages:
      role = message["role"].capitalize()
      content = message["content"]
      stringified_chat += f"{role}: {content}\n\n\n"
  return stringified_chat

#replace {{placeholders}} in a string with values from kwargs
def insert_params(string, **kwargs):
    pattern = r"{{(.*?)}}"
    matches = re.findall(pattern, string)
    for match in matches:
        replacement = kwargs.get(match.strip())
        if replacement is not None:
            string = string.replace("{{" + match + "}}", replacement)
    return string

#decorator to track and print tool calls and their results
def tool_tracker(func):
    calls = defaultdict(list)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        calls[f'{func.__name__}_calls'].append({'name': func.__name__, 'args': args, 'kwargs': kwargs, 'result': result})
        print('\n\nTools Called: \n', calls, '\n\n')
        return result
    return wrapper

#console-based chat interface for testing agents without a full UI
def run_console_chat(**kwargs):
    chat = AgentTemplate.from_file(**kwargs)
    message = chat.start_chat()
    while True:
        print('Agent:', message)
        try:
            message = chat.send(input('You: '))
        except StopIteration as e:
            if isinstance(e.value, tuple):
                print('Agent:', e.value[0])
                ending_match = e.value[1]
                print('Ending match:', ending_match)
            break

#agent template class that manages chat state, tool calls, and response processing
class AgentTemplate:
    def __init__(self, template, **kwargs):
        self.instance = template
        self.instance['options']['seed'] = hash(str(self.instance['options']['seed']))
        self.messages = self.instance['messages']
        self.stop = self.instance['options']['stop'] if 'stop' in self.instance['options'] else None
        self.function_caller = kwargs['function_call_processor'] if 'function_call_processor' in kwargs else None
        process_response_method = kwargs['process_response'] if 'process_response' in kwargs else lambda self, x: x 
        self.process_response = MethodType(process_response_method, self)
        self.parameters = kwargs
        self.instance['tools'] = TOOL_SCHEMAS
        self.last_user_input = "no user input yet"

    #class method to create an agent instance from a JSON template file
    @classmethod
    def from_file(cls, template_file, **kwargs):
        with open(Path(template_file), 'r') as f:
            template = json.load(f)

        return cls(template, **kwargs)

    #method to send chat messages to the model and handle tool calls
    def completion(self, **kwargs):
        self.parameters |= kwargs
        for item in self.messages:
            item['content'] = insert_params(item['content'], **self.parameters)

        return ollama.chat(**self.instance)
    
    #method to handle a single turn of chat, including processing tool calls and results
    def chat_turn(self, **kwargs):
        response = self.completion(**kwargs)
        message = response['message']
        if message.tool_calls:
            self.messages.append({'role': 'assistant', 'content': message.content or '', 'tool_calls': message.tool_calls})
            for tool_call in message.tool_calls:
                name = tool_call.function.name
                args = tool_call.function.arguments
                if name == "reason" and hasattr(self, 'last_user_input'): #check for reasoning and last input
                    args['player_intent'] = self.last_user_input #inject last user input into reasoning tool calls
                print(f'\n[Tool call: {name}({args})]')
                result = run_tool(name, args)
                print(f'[Tool result: {result}]')
                self.messages.append({'role': 'tool', 'content': result})
            response = self.completion()
            message = response['message']
        self.messages.append({'role': message.role, 'content': message.content})
        logging.info(f'{message.role}: {message.content}')
        return response 
    
    #generator function to manage the chat responses and user input until stop condition
    def _chat_generator_func(self):
        while True:
            response = self.chat_turn()

            response = self.process_response(response)

            if self.stop and any(stop_token in response.message.content for stop_token in self.stop):
                return response.message.content

            user_input = yield response.message.content

            logging.info(f'User: {user_input}')
            self.last_user_input = user_input  #track last user input for reasoning
            self.messages.append({'role': 'user', 'content': user_input})
            if user_input == '/exit':
                break
            
    #start the chat generator and return the first message
    def start_chat(self):
        self.chat_generator = self._chat_generator_func()
        first_message = next(self.chat_generator)
        return first_message

    #method to send user input to the chat generator and get the next response
    def send(self, user_input):
        return self.chat_generator.send(user_input)