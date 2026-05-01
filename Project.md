# 1. Base System Functionality

answer...

# 2. Prompt Engineering and Model Parameter Choice

first user promt: ask for player character creation instead of empty message
deepseek-r1:8b > 3b - better balance of speed & context/memory
increase temperature: make it not so deterministic so it can choose more options than repeating the same response over and over

# 3. Tools Usage

answer...

# 4. Planning & Reasoning

answer...

# 5. RAG Implementation

answer...

# 6. Additional Tools / Innovation

answer...

# New Player Example

PS C:\Users\Jamie\Desktop\Frantz_441> & c:\python313\python.exe c:/Users/Jamie/Desktop/Frantz_441/agent.py
RAG: No character files found to index
Agent: Generating response...

DM: Excited to begin our adventure together! To create your player character, I need to know a few details. Please provide me with the following information:

1. **Name**: What would you like your character's name to be?
2. **Race**: Which fantasy race would you like your character to belong to? (e.g., Human, Dwarf, Elf, Halfling, Dragonborn, etc.)
3. **Class**: Which class would you like your character to be? (e.g., Fighter, Wizard, Rogue, Cleric, Paladin, etc.) - don't worry if you're not sure about this one yet!
4. **Backstory**: Do you have a brief history or motivation for your character? (This can help me tailor their personality and abilities)

Please respond with these details, and I'll create your player character!

TTS: tempTTS.mp3 generating...
TTS: tempTTS.mp3 loading...
TTS: en-US-EmmaNeural speaking...
TTS: tempTTS.mp3 unloading...

You: name is Chip, race is human, class is rogue, backstory is teenage orphan looking for parents

Agent: Generating response...
Tool call: create_player({'backstory': 'teenage orphan looking for parents', 'char_class': 'rogue', 'name': 'Chip', 'race': 'human'})
RAG: Indexed new character chip
Saved chip to C:\Users\Jamie\Desktop\Frantz_441\data\characters\players\json and C:\Users\Jamie\Desktop\Frantz_441\data\characters\players\rag
Tool result: {'name': 'Chip', 'race': 'human', 'class': 'rogue', 'level': 1, 'hp': 10, 'max_hp': 10, 'inventory': [], 'status': 'alive', 'backstory': 'teenage orphan looking for parents', 'type': 'player', 'gold': 10}

DM: Welcome, Chip the rogue! I've created your character. Now that we have your character set up, let's begin our adventure!

**Campaign: "The Missing Heirloom"**

You find yourself in the bustling city of Ravenshire, a hub for adventurers and treasure seekers. You've heard rumors of a priceless family heirloom, a golden locket passed down through generations of wealthy merchants. The locket has gone missing, and the merchant's guild is offering a substantial reward to anyone who can retrieve it.

As you arrive at the guild, you're approached by a worried guildmaster, who explains the situation:

"Ah, Chip! We've had reports that the golden locket has been stolen from our most esteemed member, Marcellus Thorne. He's beside himself, and we need someone with your... particular set of skills to help us retrieve the locket."

Marcellus hands you a note with a cryptic message:

"Where shadows dance, darkness reigns
Seek the reflection of a forgotten name"

He leans in closer and whispers:

"Rumor has it that the thief was last seen near the old windmill on the outskirts of town. Be careful, Chip. The streets can be treacherous, especially at night."

You look around and see several locations to consider:

1. **The Old Windmill**: A potential lead on the thief's whereabouts.
2. **The Guild's Archives**: May hold clues about the locket's past or connections to Marcellus Thorne.
3. **The City Watch**: Can provide information or assistance, but might be too slow to help you.

What would you like to do first, Chip?

TTS: tempTTS.mp3 generating...
TTS: tempTTS.mp3 loading...
TTS: en-US-EmmaNeural speaking...
TTS: tempTTS.mp3 unloading...

You: investigate the old windmill

Agent: Generating response...
Tool call: take_action({'target': 'the old windmill', 'action': 'investigate the old windmill', 'context': 'looking around the guild for clues about the stolen locket', 'requires_check': 'false'})
RAG: Indexed new character event_1777655974
Saved event_1777655974 to C:\Users\Jamie\Desktop\Frantz_441\data\actions\json and C:\Users\Jamie\Desktop\Frantz_441\data\actions\rag
Tool result: {'character': 'the old windmill', 'interaction_type': 'action', 'context': 'looking around the guild for clues about the stolen locket', 'status': 'in_progress', 'action': 'investigate the old windmill', 'requires_check': 'false'}

DM: You decide to investigate the old windmill, as it's likely where the thief was last seen. You make your way to the outskirts of town, following the winding roads that lead to the ancient structure.

As you approach the windmill, you notice a peculiar feeling in the air. The wind seems to be picking up, and the creaking of the old wooden blades sounds ominous. You push open the creaky door and step inside.

The interior is musty and dark, with thick layers of dust covering everything. You fumble for your torch and light it, casting flickering shadows on the walls. The air is thick with the scent of decay and neglect.

You begin to explore the windmill, searching for any signs of the thief or clues about the stolen locket. As you climb the creaking stairs, you notice a small door hidden behind a tattered tapestry. The door appears locked, but you suspect it might be hidden key is somewhere nearby.

After a few minutes of searching, you find a small compartment in the wall, containing a rusty key and a note with a cryptic message:

"The eyes that see are not the ones that look"

You ponder the meaning of this message, wondering if it's connected to the locket or something more sinister. You now have three options:

1. **Unlock the door**: Try to unlock the small door you found earlier.
2. **Search the windmill further**: Look for more clues or hidden compartments.
3. **Leave and return to the guild**: Return to the guild and share your findings with Marcellus Thorne.

What would you like to do next, Chip?

TTS: tempTTS.mp3 generating...
TTS: tempTTS.mp3 loading...
TTS: en-US-EmmaNeural speaking...
TTS: tempTTS.mp3 unloading...

You: /exit

PS C:\Users\Jamie\Desktop\Frantz_441> 