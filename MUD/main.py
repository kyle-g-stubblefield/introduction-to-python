from utils import cprint, cstrip, crepl
from characters import Race, Character
from objects import Object
from world import Room


def input_handler(string) -> str:
    retvar = ""
    if string.lower() in ["quit", "exit", "leave", "q", "camp"]:
        retvar = "quit"
    if string.lower() in ["east", "west", "up", "down", "north", "south"]:
        retvar = go(character, locations, rooms, string.lower())
    return retvar


def go(character, locations, rooms, direction):
    # print(rooms[positions[character]])
    # print(direction)
    room = rooms[locations[character]]

    # loop over the exits in the room
    retvar = ""
    for rm in room.exits:
        if rm["direction"] == direction:
            rmid = rm["roomId"]
            locations[character] = rmid
            retvar = rooms[rmid]
            break
        else:
            retvar = "Alas, you cannot go that way. . . ."

    return retvar

    # sanity check, exit not found print alas


if __name__ == "__main__":
    races = {}
    races["Human"] = Race()
    races["Dwarf"] = Race(
        {
            "stats_modifier": [1.1, 1, 1.3, 0.9, 1, 10],
            "size": "medium_small",
            "innate_abilities": ["infravision"],
        }
    )
    races["Grey Elf"] = Race(
        {
            "stats_modifier": [0.7, 1.2, 0.8, 1.1, 1, 1.1],
            "size": "medium_small",
            "innate_abilities": ["infravision", "outdoor_sneak"],
        }
    )
    races["Ogre"] = Race(
        {
            "stats_modifier": [1.5, 0.8, 1.5, 0.5, 0.75, 0.75],
            "size": "large",
            "innate_abilities": ["doorbash"],
        }
    )

    ## Create a moted Instance
    characters = {}
    characters["Moted"] = Character(
        {
            "name": "Moted",
            "race": "Dwarf",
            "class": "Shaman",
            "level": 24,
            "stats": [88, 80, 80, 80, 80, 80],
        }
    )
    characters["Aleolas"] = Character(
        {
            "name": "Aleolas",
            "race": "Grey Elf",
            "class": "Ranger",
            "level": 50,
            "stats": [100, 80, 100, 80, 80, 80],
        }
    )
    characters["Illilel"] = Character(
        {
            "name": "Illilel",
            "race": "Grey Elf",
            "class": "Bard",
            "level": 50,
            "stats": [100, 100, 100, 72, 54, 100],
        }
    )

    rooms = {}
    objects = []

    tss = {
        "name": "a &+rtattered &+csilken sack&N",
        "key_words": ("tattered", "silken", "sack"),
        "room_description": "a &+rtattered &+csilken sack&N lies here, discarded.",
        "description": "This sack seems in a awful condition, large holes open in its silken\nfabric but strangely enough nothing exits from them.",
    }
    windsong = {
        "name": "&+ga &wg&Wl&wi&Wtt&wer&Wi&wng &N&+gelven scimitar&N",
        "room_description": "&+gA glittering elven scimitar is lying on the ground here.&N",
        "key_words": ("scimitar", "elven", "glittering"),
        "description": """&+gIts blade encrusted with diamond dust, this magically light
    &+gelven blade glitters in the sunlight and seems to hum softly
    &+gwhen wielded in battle.&N""",
    }
    objects.append(
        Object(
            {
                "name": "red expo marker",
                "key_words": ("red", "expo", "marker"),
                "room_description": "a red expo marker is carlessly discarded here",
                "description": "Dark magenta low scent marker, half used",
            }
        )
    )

    objects.append(
        Object(
            {
                "name": "green expo marker",
                "key_words": ("green", "expo", "marker"),
                "room_description": "a green expo marker is carlessly discarded here",
                "description": "Forest green low scent marker, half used",
            }
        )
    )

    rooms[1] = Room(
        {
            "number": 1,
            "name": "The Void",
            "description": "There is nothing here but the sound of rushing of wind.\nWe are waiting for the Spirit of God to move over it.",
            "indoors": False,
            "terrain": "no ground",
            "exits": [
                {"direction": "north", "roomId": 1},
                {"direction": "south", "roomId": 1},
                {"direction": "east", "roomId": 2},
                {"direction": "west", "roomId": 3},
                {"direction": "up", "roomId": 1},
                {"direction": "down", "roomId": 1},
            ],
            "objects": [],
        }
    )

    rooms[2] = Room(
        {
            "number": 2,
            "name": "Not The Void",
            "description": "You left\nSo sorry",
            "indoors": False,
            "terrain": "no ground",
            "exits": [
                {"direction": "north", "roomId": 1},
                {"direction": "south", "roomId": 1},
            ],
            "objects": [*objects],
        }
    )

    rooms[3] = Room(
        {
            "number": 3,
            "name": "Not the Not The Void",
            "description": "Now you stuck",
            "indoors": False,
            "terrain": "no ground",
            "exits": [],
            "objects": [*objects],
        }
    )

    ptr = Object(tss)
    objects.append(ptr)
    rooms[2].objects.append(ptr)
    ptr = Object(windsong)
    objects.append(ptr)
    rooms[2].objects.append(ptr)

    # print(here)
    locations = {"Moted": 1, "Illilel": 1, "Aleolas": 1}

    # samples = [
    #     "&+cAshenmoor&N -- a text adventure",
    #     "&Rwarning:&N health is &+Rcritically low&N!",
    #     "&+WTHE RUSTY FLAGON&N",
    #     "&WPlatinum&N: 152 &YGold&N: 42  &wSilver&N: 7  &yCopper&N: 3",
    #     "&ggreen&N  &+Gbright green&N  &ccyan&N  &+cbright cyan&N",
    #     "&mmagenta&N  &Mbright magenta&N  &bblue&N  &Bbright blue&N",
    #     "&&N is a literal ampersand-N, not a reset",
    # ]
    # print("\n\033[1m-- terminal ANSI demo --\033[0m")
    # for s in samples:
    #     print(f"  raw: {s}")
    #     cprint(f"  out: {s}")
    #     print()
    # print("\033[1m-- cstrip --\033[0m")
    # for s in samples:
    #     print(f"  {cstrip(s)}")
    
    character = 'Moted'
    cprint(rooms[locations[character]])
    crepl(
        handler=input_handler,
        prompt="&g> &N",
        banner="&WWelcome to &RRiverview &WChristian &BSchool&N SUD!&N",
        farewell="&CGoodbye!&N",
    )
