from app.animals.animal import Animal
from app.animals.herbivore import Herbivore


class Carnivore(Animal):

    def bite(self, other):
        if isinstance(other, Herbivore):
            if not other.hidden:
                other.health -= 50
                Animal.heal_check(other)