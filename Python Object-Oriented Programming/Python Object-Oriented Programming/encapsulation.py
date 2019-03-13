class Person:

    def __init__(self, name, age = 1):
        self.__name = name
        self.__age = age

    def get_info(self):
        return("Имя: {}\tВозраст: {}".format(self.name, self.age))

    def disp_info(self):
        print(Person.get_info(self))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        if age in range(1,150):
            self.__age = age
        else:
            print("Недопустимый возраст ({})".format(age))

person1 = Person("Том")
person1.name = "ТОмас"
person1.age = 35
person1.disp_info()
