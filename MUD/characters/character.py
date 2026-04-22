from utils import Stats


## Base Character Class
class Character:
    """Base character class"""

    def __init__(self, d, statlist=Stats):
        self.name = d.get("name", None)
        self.stats = d.get("stats", [80, 80, 80, 80, 80, 80])
        self.race = d.get("race", "Human")
        self.level = d.get("level", 1)
        self.position = d.get("position", "standing")
        self.cclass = d.get("class", "Warrior")

    def __str__(self):
        retvar = f"Character sheet for {self.name}\n"
        retvar += f"Race: {self.race}\n"
        retvar += f"Class: {self.cclass}\n"
        retvar += f"Level: {self.level}\n"
        retvar += "Stats:\n"
        retvar += f"Strength:     {self.get_stat('str'):>3}    Intelligence: {self.get_stat('int'):>3}\n"
        retvar += f"Dexterity:    {self.get_stat('dex'):>3}    Wisdom:       {self.get_stat('wis'):>3}\n"
        retvar += f"Constitution: {self.get_stat('con'):>3}    Charisma:     {self.get_stat('cha'):>3}\n\n"
        return retvar

    def get_stat(self, stat):
        if type(stat) == int:
            return self.stats[stat]
        elif type(stat) == str:
            for k in Stats:
                if stat == k.abv:
                    return self.stats[k.value]
        return None

    # def computed_stat(self, stat):
    #  return int(self.get_stat(stat) * races[self.race].get_mod(stat))

    def pcs(self):
        print(self)
