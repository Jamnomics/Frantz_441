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

# Old Player Example

PS C:\Users\Jamie\Desktop\Frantz_441> & c:\python313\python.exe c:/Users/Jamie/Desktop/Frantz_441/agent.py
RAG: Already indexed chip
Agent: Generating response...
Tool call: reason({'chosen_outcome': 'Gorin provides information', 'next_narrative': 'Gorin shares what he knows about the recent strange occurrences in the village, and Chip decides how to proceed.', 'situation': 'The village elder has expressed concern about the disappearances and asked Gorin, the village guard, for help.', 'player_intent': 'progress the campaign', 'possible_outcomes': 'Gorin provides information, a lead is found, or nothing changes'})
Tool result: Proceed with: Gorin shares what he knows about the recent strange occurrences in the village, and Chip decides how to proceed.

DM: Gorin rubs his chin thoughtfully as he leans against the wooden post of the village gate. "To be honest, I don't know much about what's been going on," he says in a deep, rumbling voice. "But I do know that it started a few nights ago. One of our villagers, a young woman named Elara, didn't return from her evening walk. We thought maybe she'd just gone off to visit with friends or something, but when she didn't come back the next day... well, we got worried."

Gorin's expression turns serious. "Since then, three more people have gone missing. All of them were last seen heading into the nearby forest. I've had some of my men search for them, but so far, nothing's turned up."

Chip eyes Gorin's face, taking in every detail. He can tell that the guard is genuinely concerned about the disappearances, and he wants to know more.

What would you like Chip to do next?

(Remember, you're a rogue, so think about stealthy moves, sneaky tricks, or perhaps a daring rescue mission!)

TTS: tempTTS.mp3 generating...
TTS: tempTTS.mp3 loading...
TTS: en-US-EmmaNeural speaking...
TTS: tempTTS.mp3 unloading...

You: ask him for more details about her disappearence

Agent: Generating response...
Tool call: talk_to_character({'context': 'the missing villager', 'character_name': 'Gorin the Gruff', 'topic': 'Elara'})
RAG: Indexed new character event_1777656647
Saved event_1777656647 to C:\Users\Jamie\Desktop\Frantz_441\data\talks\json and C:\Users\Jamie\Desktop\Frantz_441\data\talks\rag
Tool result: {'character': 'Gorin the Gruff', 'interaction_type': 'dialogue', 'context': 'the missing villager', 'status': 'in_progress', 'topic': 'Elara'}

DM: "Tell me more about Elara's disappearance," Chip asks Gorin, his eyes locked on the guard's face. "What was her last known location? Did she say anything strange before she vanished?"

Gorin nods, his expression serious. "Elara was a bit of a loner, but everyone in the village liked her. She was out for her evening walk about an hour after dinner, I think. She usually takes that route to clear her head before bed. But when she didn't show up for breakfast the next morning... well, that's when we started getting worried."

Gorin pauses, collecting his thoughts. "From what our scouts have reported, Elara was seen walking alone in the forest around midnight. They didn't see anyone else with her, but they did notice that the trees seemed to be... twisted, somehow. Like they were leaning in towards her or something. It was quite unsettling."

Chip's eyes narrow, intrigued by Gorin's description of the forest. He can almost feel a malevolent presence lurking just out of sight.

"What about the other missing villagers?" Chip asks, trying to piece together the puzzle. "Did they have any commonalities with Elara? Any clues that might lead us to them?"

Gorin furrows his brow. "That's what's got me stumped. They all seemed to vanish without a word. No signs of struggle or foul play. It's like... they just disappeared into thin air."

Chip nods thoughtfully, taking in Gorin's words. He knows he needs to act fast if he wants to find out what's happening to these villagers.

What would you like Chip to do next?

TTS: tempTTS.mp3 generating...
TTS: tempTTS.mp3 loading...
TTS: en-US-EmmaNeural speaking...
TTS: tempTTS.mp3 unloading...

You: /exit

PS C:\Users\Jamie\Desktop\Frantz_441> 