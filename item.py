import math


class Item():
    def __init__(self, name : str):
        self.name = name

    



class Potion(Item):
    def __init__(self, name : str , healing_amount : int):
        super.__init__(name)
        self.healing_amount = healing_amount

    def heal(self, ch):
        ch.hp() += self.healing_amount
        print(f"You drank the potion and gained {self.healing_amount} hp")


class Arm(Item):
    def __init__(self, name: str, damage: int):
        super.__init__(name)
        self.damage = damage

    def attack(self, ch):
        points = math.random()*1000
        ch.hp += points
        print(f"You attacked successfully and you damage your opponent for {points} points")



    
