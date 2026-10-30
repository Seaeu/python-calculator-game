## -- Difficulties -- ##
class Difficulty:
    def __init__(self,name,multiplier,bound,tries,lives,reward):
        self.name = name
        self.mult = multiplier
        self.bound = bound
        self.tries = tries
        self.lives = lives
        self.reward = reward

Simple = Difficulty("Simple",0.5,100,4,5,45)
Easy = Difficulty("Easy", 0.75, 250,3,4,60)
Medium = Difficulty("Medium", 1.25, 750,5,4,75)
Standard = Difficulty("Standard", 1.5, 1000,4,3,100)
Hard = Difficulty("Hard", 1.75, 1500,4,3,65)
Extreme = Difficulty("Extreme", 2, 3500,5,2,50)
IMPOSSIBLE = Difficulty("IMPOSSIBLE", 5, 10000,5,2,75)
# - Make Difficulties readable in 1 dictionary - #
DIFF_LIST = {
    "Simple": Simple,
    "Easy": Easy,
    "Medium": Medium,
    "Standard": Standard,
    "Hard": Hard,
    "Extreme": Extreme,
    "IMPOSSIBLE": IMPOSSIBLE
    }

