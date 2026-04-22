#file path imports
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1]))

#import necessary libraries
import chromadb
from config import PLAYERS_RAG, NPCS_RAG, DB_PATH

#initialize ChromaDB client
client = chromadb.PersistentClient(path=str(DB_PATH))

#return or create the ChromaDB collection for characters
def get_collection():
    return client.get_or_create_collection(name="characters")

#read all .txt files from rag folders and embed them into ChromaDB
def index_characters():
    #gather files into collection
    collection = get_collection()
    rag_files = list(PLAYERS_RAG.glob("*.txt")) + list(NPCS_RAG.glob("*.txt"))

    #no rag files to index
    if not rag_files:
        print("RAG: No character files found to index")
        return

    #loop through each file to index
    for path in rag_files:
        doc_id = path.stem

        #skip if already indexed
        existing = collection.get(ids=[doc_id])
        if existing["ids"]:
            print(f"RAG: Already indexed {doc_id}")
            continue

        #read text and add to collection
        text = path.read_text()
        collection.add(ids=[doc_id], documents=[text], metadatas=[{"source": str(path)}])
        print(f"RAG: Indexed {doc_id}")

#index a single character immediately after creation
def index_character(name: str, text: str):
    collection = get_collection()
    doc_id = name.lower().replace(" ", "_")
    collection.upsert(ids=[doc_id], documents=[text], metadatas=[{"source": name}])
    print(f"RAG: Indexed new character {doc_id}")