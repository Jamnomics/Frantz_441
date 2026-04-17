#file path imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

#import necessary libraries
from tools.roll_dice import schema as dice_schema, run as dice_run

#list of tool schemas to pass to agent template
TOOL_SCHEMAS = [dice_schema]

#map tool names to their run functions
TOOL_FUNCTIONS = {
    "roll_dice": dice_run,
}