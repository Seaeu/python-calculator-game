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
# - Make Difficulties readable in 1 array - #
DIFF_LIST = {
    "Simple": Simple,
    "Easy": Easy,
    "Medium": Medium,
    "Standard": Standard,
    "Hard": Hard,
    "Extreme": Extreme,
    "IMPOSSIBLE": IMPOSSIBLE}

## -- Items -- ##
class Item:
    def __init__(self,name,cost,weight,tries,lives,bound):
        self.name = name
        self.cost = cost
        self.rarity = weight
        self.tries = tries
        self.lives = lives
        self.bound = bound

    def buy(self,Difficulty):
        print(f"{self} bought!")
        print(Difficulty)

LifeUp = Item("Life Up",25,40,0,1,0)
OneMoreTry = Item("One More Try",35,40,1,0,0)
RangeThinner = Item("Range Thinner",50,25,0,0)
# - Make Items readable in 1 array - #
ITEM_LIST = {
    "Life UP": LifeUp,
    "One More Try": OneMoreTry,
    "Range Thinner": RangeThinner
}
