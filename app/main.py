from app.animals.animal import Animal
from app.animals.carnivore import Carnivore
from app.animals.herbivore import Herbivore


lion = Carnivore("Lion King")
rabbit = Herbivore("Susan")
cat = Carnivore("Cat")
rabbit.hide()
print(Animal.alive)