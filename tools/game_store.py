#file path imports
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

#import necessary libraries
import json
import time
from config import ENCOUNTERS_JSON, ENCOUNTERS_RAG, ACTIONS_JSON, ACTIONS_RAG, TALKS_JSON, TALKS_RAG, SKILL_CHECKS_JSON, SKILL_CHECKS_RAG

#shared save logic for all game events
def _save(data: dict, json_dir: Path, rag_dir: Path, summary: str) -> str:
    #use timestamp as unique id so multiple events don't overwrite each other
    timestamp = str(int(time.time()))
    
    #save as JSON
    slug = f"{data.get('type', 'event')}_{timestamp}".lower().replace(" ", "_")
    with open(json_dir / f"{slug}.json", "w") as f:
        json.dump(data, f, indent=2)
    
    #build text summary
    with open(rag_dir / f"{slug}.txt", "w") as f:
        f.write(summary)

    #index into ChromaDB
    from rag.embedder import index_character
    index_character(slug, summary)

    print(f"Saved {slug} to {json_dir} and {rag_dir}")
    return summary

#save encounters using main save logic
def save_encounter(encounter: dict) -> str:
    summary = (
        f"Encounter Type: {encounter['type']}\n"
        f"Location: {encounter['location']}\n"
        f"Participants: {encounter['participants']}\n"
        f"Objective: {encounter['objective']}\n"
        f"Status: {encounter['status']}"
    )
    return _save(encounter, ENCOUNTERS_JSON, ENCOUNTERS_RAG, summary)

#save actions using main save logic
def save_action(action: dict) -> str:
    summary = (
        f"Action: {action['action']}\n"
        f"Target: {action['character']}\n"
        f"Context: {action['context']}\n"
        f"Requires Check: {action['requires_check']}"
    )
    return _save(action, ACTIONS_JSON, ACTIONS_RAG, summary)

#save interactions using main save logic
def save_talk(talk: dict) -> str:
    summary = (
        f"Conversation with: {talk['character']}\n"
        f"Topic: {talk['topic']}\n"
        f"Context: {talk['context']}\n"
        f"Disposition: {talk.get('disposition', 'unknown')}"
    )
    return _save(talk, TALKS_JSON, TALKS_RAG, summary)

#save skill checks using main save logic
def save_skill_check(check: dict) -> str:
    summary = (
        f"Skill Check: {check['skill']}\n"
        f"Roll: {check['roll']} + {check['modifier']} = {check['total']}\n"
        f"DC: {check['difficulty']}\n"
        f"Result: {check['result']}"
    )
    return _save(check, SKILL_CHECKS_JSON, SKILL_CHECKS_RAG, summary)