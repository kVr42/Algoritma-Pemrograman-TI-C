#polymorphism
class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("The animal makes a sound")

class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name)
    self.breed = breed

  def make_sound(self):
    print("The dog barks")

class Cat(Animal):
  def __init__(self, name, color):
    super().__init__(name)
    self.color = color

  def make_sound(self):
    print("The cat meows")

# Create instances of each class
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

# Call the make_sound method on each instance
dog.make_sound()  # Output: The dog barks
cat.make_sound()  # Output: The cat meows



class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object
