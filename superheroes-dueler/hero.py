import random

# hero.py
class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        '''

        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
    
    def fight(self, opponent):
        self.opponent = opponent
        winner = random.randint(0,1)
        if winner == int(0):
            print("Wonder Woman defeats Dumbledore!")
        else:
            print("Dumbledore defeats Wonder Woman!")

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
        
    hero1.fight(hero2)