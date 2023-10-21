import random as r
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    
    def block(self):
        block_value = r.randint(0, self.max_block)
        return block_value
    
if __name__ == "__main__":
    armor1 = Armor("diamond armor", 150)
    print(armor1.block())