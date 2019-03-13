class Cat:
    master = "me"
    def __init__(self, name, color, legs):
        self.color = color
        self.legs = legs
        self.name = name
    def meow(self):
        print("MEOW")

def print_cat(cat):
    print("Cat: {0}. master: {3}. color: {1}. legs: {2}".format(cat.name,cat.color, cat.legs, cat.master))
    pass

spit = Cat("Spit","black", 3)
spit.master = "Кто-то"
felix = Cat("Felix","red", 4)
tom = Cat("Tom","grown",4)
print_cat(felix)
print_cat(tom)
print_cat(spit)

