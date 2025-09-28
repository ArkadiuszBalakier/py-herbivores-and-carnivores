class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden:  bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str | None:
        for animal in Animal.alive:
            representation_of_animal = f"{{Name: {animal.name}, Health: {animal.health}, Hidden: {animal.hidden}}}"
            return representation_of_animal
        return None