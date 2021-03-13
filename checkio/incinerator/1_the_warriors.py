"""
In this mission (and in several subsequent ones, related to it) you’ll have a chance "to sit in the developer's chair"
and create the logic of a simple game about battles.
Let's start with the simple task - one-on-one duel. You need to create the class Warrior, the instances of which will
have 2 parameters - health (equal to 50 points) and attack (equal to 5 points), and 1 property - is_alive, which can be
True (if warrior's health is > 0) or False (in the other case). In addition you have to create the second unit type -
Knight, which should be the subclass of the Warrior but have the increased attack - 7. Also you have to create a
function fight(), which will initiate the duel between 2 warriors and define the strongest of them. The duel occurs
according to the following principle:
Every turn, the first warrior will hit the second and this second will lose his health in the same value as the attack
of the first warrior. After that, if he is still alive, the second warrior will do the same to the first one.
The fight ends with the death of one of them. If the first warrior is still alive (and thus the other one is not
anymore), the function should return True, False otherwise.
"""


class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
        
    @property
    def is_alive(self):
        return self.health > 0

    def is_attacked(self, enemy):
        if enemy.is_alive:
            self.health -= enemy.attack


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self, attack=7)
        
    @property
    def is_alive(self):
        return self.health > 0
    
    def is_attacked(self, enemy):
        if enemy.is_alive:
            self.health -= enemy.attack


def fight(f1, f2):
    while f1.is_alive and f2.is_alive:
        f2.is_attacked(f1)
        f1.is_attacked(f2)

    return f1.is_alive


if __name__ == '__main__':
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) is True
    assert fight(dave, carl) is False
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False

    print("Coding complete? Let's try tests!")
