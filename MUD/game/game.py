from characters.character import Character
from characters.race import Race


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


def character_list(char_list):
    print(f'{"Name":<15} {"Race":<12} {"Class":<10} {"Level":>2}')
    print("_" * 45, end="\n\n")

    for _, char in char_list.items():
        print(f"{char.name:<15} {char.race:<12} {char.cclass:<10} {char.level:>5}")
