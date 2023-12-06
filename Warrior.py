class Warrior:
    def __init__(self, health=50, attack = 5):
        self.is_alive=True
        self.health=health
        self.attack=attack

class Knight(Warrior):
    def __init__(self, health=50, attack=5):
        super.__init__(health,7)

chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()

print(carl.attack)

def fight(w1,w2):
    pass