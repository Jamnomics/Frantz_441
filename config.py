#file path imports
from pathlib import Path

#add parent directory  for imports
PROJECT_ROOT = Path(__file__).resolve().parent

#character store
PLAYERS_JSON = PROJECT_ROOT / "data" / "characters" / "players" / "json"
PLAYERS_RAG  = PROJECT_ROOT / "data" / "characters" / "players" / "rag"
NPCS_JSON    = PROJECT_ROOT / "data" / "characters" / "npcs" / "json"
NPCS_RAG     = PROJECT_ROOT / "data" / "characters" / "npcs" / "rag"
DB_PATH      = PROJECT_ROOT / "data" / "chroma"

#game store
ENCOUNTERS_JSON   = PROJECT_ROOT / "data" / "encounters" / "json"
ENCOUNTERS_RAG    = PROJECT_ROOT / "data" / "encounters" / "rag"
ACTIONS_JSON      = PROJECT_ROOT / "data" / "actions" / "json"
ACTIONS_RAG       = PROJECT_ROOT / "data" / "actions" / "rag"
TALKS_JSON        = PROJECT_ROOT / "data" / "talks" / "json"
TALKS_RAG         = PROJECT_ROOT / "data" / "talks" / "rag"
SKILL_CHECKS_JSON = PROJECT_ROOT / "data" / "skill_checks" / "json"
SKILL_CHECKS_RAG  = PROJECT_ROOT / "data" / "skill_checks" / "rag"