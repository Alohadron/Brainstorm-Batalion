# def process_data(x,y):
#     try:
#         x = int(x)
#         y = int(y)
#     except Exception:
#         print('Error throw from process_data()')
#         raise

# try:
#     process_data('hello', 'from')
# except Exception as e:
#     print('Catch error here')
#     print(e)
#     raise

# class Car:
#     def __int__(self, horse_power, type_of_car, model):
#         self.horse_power = horse_power
#         self.type_of_car = type_of_car
#         self.model = model 
    
    
#     def present(self)
#         print(f,'Car: model{self.model};\
#               type of car {self.type_of_car};\
#               {self.horse_power} h.p')

# class Animal:
#     def __int__(self, name, family,habitat):
#         self.name = name 
#         self.family = family
#         self.habitat = habitat
#     def voice(self):
#         pass
#     def move(self):
#         pass
#     def eat(self):
#         pass
# class Dog(Animal):
#     def __int__(self, name, training_level):
#         super().__int__(name,"Canidae", "Home/street")
#         self.training_level = training_level
#     def voice(self):
#         return f"{self.name} says: Woof-woof!"
#     def move(self):
#         return f"{self.name} runs after a ball."
#     def eat(self):
#         return f"{self.name} is chewing on a bone."
#     def fetch(self):
#         return f"{self.name} brings a stick."

# class Tiger(Animal):
#     def __int__(self, name, stripe_count):
#         super().__int__(name, "Felidae", "Jungle")
#         self.stripe_count = stripe_count

#         def voice(self):
#             return f"{self.name} lets out a powerful roar!"
#         def move(self):
#             return f"{self.name} pounces on its prey."
#         def eat(self): 
#             return f"{self.name} is hunting in the wild."

#    animals = [Dog("Bobik", "Advanced"),
#               Tider("Shere Khan", 150)]

#     for animal in animals:
#         print(f"---{animal.name} ({animal.family})---")
#         print(animal.voice())
#         print(animal.move())
#         print(animal.eat())
#         print()
# import unittest 
# class TestMain(unittest.TestCase):
#     def test_location(self):
#         a = 're'
#         b = 'green'
#         self.assertEquale(a,b)
# if __name__ == '__main__':
#     unittest.main()
    
