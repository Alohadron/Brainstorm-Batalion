# def process_data(x, y):
#     try:
#         #Try to convert str to int
#         x = int(x)
#         y + int(y)
#     except Exception:
#         print("Error throw from process data()")
#        # raise #try to remove raise
# try:
#     process_data("Hello", "from") #throw error in this method
# except Exception as e:
#     print("Catch error here")
#     print(e) #print error in long
#     #raise #reraise: escalating the error


# class Car:
#     #set parametres in constructor
#     def __init__(self, horse_p, type_of_car, model): #def __init__ is the base of the class
#         #def __init__(self) shows from what will our class consist
#         self.horse_p = horse_p
#         self.type_of_car = type_of_car
#         self.model = model

#     #method of class
#     def present(self):
#         print(f'Model {self.model}\ntype of car {self.type_of_car}\n{self.horse_p} h.p')

# #realization of class
# mercedes = Car(200, 'sport', 'mercedes')
# mercedes.present()

# class Animal:
#     def __init__(self, name, family, habitat):
#         self.name = name
#         self.family = family
#         self.habitat = habitat
#     def voice(self):
#         pass
#     def move(self):
#         pass
#     def eat(self):
#         pass
# class Cat(Animal): #child class and parent class
#     def __init__(self, name, breed):
#         super().__init__(name, 'Felidae', 'Home')
#         #super(). connects Cat with Animal, always written in child class
#         self.breed = breed #unique parameter
#     def voice(self):
#         return f'{self.name} says: Meow!'
#     #self.name = given name of the cat
#     def move(self):
#         return f'{self.name} creeps silently'
#     def eat(self):
#         return f"{self.name} its eating food from a bowl"
#     def purr(self):#unique method
#         return f"{self.name} is purring"
# class Dog(Animal):
#     def __init__(self, name, training_level):
#         super().__init__(name, 'Canidae', 'Home')
#         self.training_level = training_level
#     def voice(self):
#         return f"{self.name} barks!"
#     def move(self):
#         return f'{self.name} runs'
#     def eat(self):
#         return f"{self.name} chews bones"
#     def training_level(self): #another unique method 
#         return f"{self.name} is sporty"
# #example usage.
# animals = [Cat('Murka', "British shorthair"),
#            Dog('Bobik', "Advanced")]

# for animal in animals:
#     print(f'{animal.name} ({animal.family})')
#     print(animal.voice())
#     print(animal.move())
#     print(animal.eat())
#     print()

import unittest
class TestMain(unittest.TestCase):
    def test_location(self):
        a = 'red'
        b = 'green'
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()