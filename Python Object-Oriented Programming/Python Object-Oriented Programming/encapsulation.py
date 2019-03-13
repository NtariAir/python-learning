class Person:
    def __init__(self, name, age = 1):
        self.name = name
        self.age = age

    def get_info(self):
        return("Имя: {}\tВозраст: {}".format(self.name, self.age))

    def disp_info(self):
        print(Person.get_info(self))


person1 = Person("Том")
person1.disp_info()