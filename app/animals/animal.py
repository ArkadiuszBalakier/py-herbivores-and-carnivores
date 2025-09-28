from __future__ import annotations


class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str, health: int = 100, hidden:  bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
            representation_of_animal = f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"
            return representation_of_animal