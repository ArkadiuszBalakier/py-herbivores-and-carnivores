from app.animals.animal import Animal
from app.animals.herbivore import Herbivore


class Carnivore(Animal):

    @staticmethod
    def bite(other):
        if isinstance(other, Herbivore):
            if not other.hidden:
                other.health -= 50
                if other.health <= 0:
                    for animal in Animal.alive:
                        if animal.name == other.name:
                            Animal.alive.remove(animal)