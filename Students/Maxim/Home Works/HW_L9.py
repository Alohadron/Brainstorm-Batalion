class Animal:
    def __init__(self, name, family, habitat):
        self.name = name
        self.family = family
        self.habitat = habitat
    def voice(self):
        pass
    def move(self):
        pass
    def eat(self):
        pass
class Bird(Animal):
    def __init__(self,name,flying_speed):
        super().__init__(name, "Winter", "Forest")
        self.flying_speed = flying_speed
    def voice(self):
        return f'{self.name} says: Chirp Chirp!'
    def move(self):
        return f'{self.name} flies'
    def eat(self):
        return f"{self.name} eats seeds"
    def flying_speed(self):#unique method
        return f"{self.name} flies at 50 km/h"
animals = [Bird('ptichka', "50 km/h")]
for animal in animals: 
    print(f'{animal.name} ({animal.family})')
    print(animal.voice())
    print(animal.move())
    print(animal.eat())
    print()