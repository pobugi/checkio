"""In the previous mission - Warriors - you've learned how to make a duel between 2 warriors happen. Great job!
But let's move on to something that feels a little more epic - armies! In this mission your task is to add new classes
and functions to the existing ones.

The new class should be the Army and have the method add_units() - for adding the
chosen amount of units to the army. The first unit added will be the first to go to fight,
the second will be the second, ...

Also you need to create a Battle() class with a fight() function, which will determine the strongest army.
The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army and the first warrior of the second army.
As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel, and a new fight
begins between him and the surviving warrior, who keeps his remaining health. This continues until all the soldiers
of one of the armies die. In this case, the fight() function should return True, if the first army won, or False,
if the second one was stronger.
Note that army 1 has the advantage to start every fight!"""


class Army:
    def __init__(self, health, attack, qty):
        self.health = health
        self.attack = attack
        self.num = qty

    def add_units(self, mode, qty):
        self.health = mode().health
        self.attack = mode().attack
        self.num = qty


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
