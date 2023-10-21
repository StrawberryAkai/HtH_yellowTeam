from random import randint
class Ability:
    def __init__(self, name, max_damage=50):
        '''Instance properties:
          name: String
          max_damage: Integer
        '''

        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return randint(0, self.max_damage)


if __name__ == "__main__":
    ability1 = Ability("Laser Vision", 70)
    print(f"Attacking with {ability1.name}: {ability1.attack()}")