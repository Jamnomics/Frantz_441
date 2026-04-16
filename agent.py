#clean file paths
from pathlib import Path

#add parent directory to path
import sys
sys.path.append(str(Path(__file__).parents[1]))

#get chat function from util folder
from util.llm_utils import run_console_chat

#run chat with agent
run_console_chat(template_file="util/templates/dm_chat.json")