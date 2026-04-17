#file path imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

#import necessary libraries
from tools.init import TOOL_FUNCTIONS

#separate and clean argumnets from schema
def sanitize_args(tool_input: dict) -> dict:
    #schema-related junk keys
    junk_keys = {'object', 'type', 'properties', 'required'}
    
    #unwrap if args are nested inside a junk key
    for junk in junk_keys:
        if junk in tool_input and isinstance(tool_input[junk], dict):
            tool_input = tool_input[junk]
            break
    
    #remove schema-related junk keys
    cleaned = {k: v for k, v in tool_input.items() if k not in junk_keys}
    
    #cast string numbers to int
    for k, v in cleaned.items():
        if isinstance(v, str) and v.isdigit():
            cleaned[k] = int(v)
    
    #return processed dictionary of clean arguments
    return cleaned

def run_tool(tool_name: str, tool_input: dict) -> str:
    #check if tool exists
    if tool_name not in TOOL_FUNCTIONS:
        return f"Unknown tool: {tool_name}"
    
    #call cleaned tool function
    clean_input = sanitize_args(tool_input)
    return TOOL_FUNCTIONS[tool_name](**clean_input)