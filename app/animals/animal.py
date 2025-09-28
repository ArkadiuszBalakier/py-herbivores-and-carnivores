
class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        animal = {"name": self.name, "health": self.health, "hidden": self.hidden}
        Animal.alive.append(animal)

    @staticmethod
    def heal_check(other) -> None:
            if other.health <= 0:
                for animal in Animal.alive:
                    if animal.name == other.name:
                        Animal.alive.remove(animal)
