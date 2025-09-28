from app.animals.animal import Animal


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden