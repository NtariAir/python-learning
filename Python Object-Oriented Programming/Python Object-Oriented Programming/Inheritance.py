class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

class Cat(Animal):
    def Purr(self):
        print("Purr...")

class Dog(Animal):
    def Bark(self):
        print("Woof!")


pluto = Dog("Pluto", "white")
print(pluto.name)
pluto.Bark()