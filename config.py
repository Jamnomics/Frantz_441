##file path imports
from pathlib import Path

#add parent directory  for imports
PROJECT_ROOT = Path(__file__).resolve().parent

#file paths for character storage and RAG summaries
PLAYERS_JSON = PROJECT_ROOT / "data" / "characters" / "players" / "json"
PLAYERS_RAG  = PROJECT_ROOT / "data" / "characters" / "players" / "rag"
NPCS_JSON    = PROJECT_ROOT / "data" / "characters" / "npcs" / "json"
NPCS_RAG     = PROJECT_ROOT / "data" / "characters" / "npcs" / "rag"
DB_PATH      = PROJECT_ROOT / "data" / "chroma"