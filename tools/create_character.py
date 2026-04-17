#core character creation logic shared by NPC and player tools
def create_character(name: str, race: str, char_class: str, level: int = 1, hp: int = 10) -> dict:
    return {
        "name": name,
        "race": race,
        "class": char_class,
        "level": level,
        "hp": hp,
        "max_hp": hp,
        "inventory": [],
        "status": "alive"
    }