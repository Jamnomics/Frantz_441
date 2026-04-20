#file path imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

#import necessary libraries
from tools.roll_dice import schema as dice_schema, run as dice_run
from tools.create_npc  import schema as npc_schema,    run as npc_run
from tools.create_player import schema as player_schema, run as player_run
from tools.reason import schema as reason_schema,  run as reason_run
from tools.run_encounter import schema as encounter_schema,  run as encounter_run

#list of tool schemas to pass to agent template
TOOL_SCHEMAS = [dice_schema, npc_schema, player_schema, reason_schema, encounter_schema]

#map tool names to their run functions
TOOL_FUNCTIONS = {
    "roll_dice": dice_run,
    "create_npc":    npc_run,
    "create_player": player_run,
    "reason": reason_run,
    "run_encounter": encounter_run
}