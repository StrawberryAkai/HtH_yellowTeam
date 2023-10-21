import random
class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    
    def attack_method(self):
        damage = random.randint(0, self.max_damage)
        return damage
    
if __name__ == "__main__":
        ability = Ability("y", 10)
        print(ability.attack_method())
        
            