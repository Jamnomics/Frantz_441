#file path imports
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1]))

#import necessary libraries
from rag.embedder import get_collection

#query the vector store and return relevant character info as a string
def retrieve(query: str, n_results: int = 3) -> str:
    #query ChromaDB for relevant character
    collection = get_collection()
    results = collection.query(query_texts=[query], n_results=n_results)
    if not results["documents"] or not results["documents"][0]:
        return ""
    
    #join all matching docs into a single context string
    docs = results["documents"][0]
    context = "\n\n---\n\n".join(docs)
    return context