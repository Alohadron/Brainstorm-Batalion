class Animal:
    def __init__(self, name, family, habitat):
        self.name = name
        self.family = family
        self.habitat = habitat

    def voice(self):
        return "Неизвестный звук животного" \

    def move(self):
        return "Животное передвигается"

    def eat(self):
        return "Животное ест"

class Dog(Animal):

  def voice(self):
    return "Гав-гав!"

  def move(self):
    return "Бегает на четырех лапах"

  def eat(self):
    return "Ест сухой корм для собак"

  def fetch(self):
    return f"{self.name} приносит палочку!"

class Cat(Animal):

  def voice(self):
    return "Мяу"

  def move(self):
    return "Бесшумно [ходит на четырех лапах]"

  def eat(self):
    return "Ест рыбку"

  def scratch(self):
    return f"{self.name} точит когти о когтеточку!"

class Bird(Animal):

  def voice(self):
    return "Чирик-чирик! 🐦"

  def move(self):
    return "Летит в небе"

  def eat(self):
    return "Клюет зернышки"

  def sing(self):
    return f"{self.name} красиво поет поутру!"

  if __name__ == "__main__":
  dog = Dog(name="Бобик", family="Псовые", habitat="Вольер")
  cat = Cat(name="Мурка", family="Кошачьи", habitat="Дом")
  bird = Bird(name="Чижик", family="Птицы", habitat="Клетка")

  animals = [dog, cat, bird]

  for a in animals:
    print(f"--- {a.name} ({a.family}, среда: {a.habitat}) ---")
    print(f"Голос: {a.voice()}")
    print(f"Движение: {a.move()}")
    print(f"Еда: {a.eat()}")

    if isinstance(a, Dog):
      print(a.fetch())

    elif isinstance(a, Cat):
      print(a.scratch())

    elif isinstance(a, Bird):
      print(a.sing())

    print()