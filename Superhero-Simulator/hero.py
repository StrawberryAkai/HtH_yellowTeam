# hero.py
import random as r
from ability import Ability
from armor import Armor

class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        name: String
        starting_health: Integervhjk’

        current_health: Integer
        '''

        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        
        #set armors to empty array
        self.armors = []
        
        #set ability to empty array
        self.abilities = []
        

    def battle(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        #1) randomly choose winner, print the name of the victor
        # Hint: Look into random library, more specifically the choice method
        winer = r.choice([self, opponent])
        return winer.name
        
    def add_ability(self, ability):
        self.abilities.append(ability)
        
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.max_damage
        return total_damage
    
    def defend(self):
        total_block = 0
        for block in self.armors:
            total_block += block.max_block
        return total_block

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    opponent = Hero("Yuxuan", 200)
    
    lighning = Ability("Thunder Bolt", 25)
    my_hero.add_ability(lighning)
    
    fire = Ability("Fire Ball", 50)
    my_hero.add_ability(fire)
    
    for i in my_hero.abilities:
        print(i.name)
    print(my_hero.name)
    print(my_hero.current_health)
    print(my_hero.battle(opponent))
    print(my_hero.attack())