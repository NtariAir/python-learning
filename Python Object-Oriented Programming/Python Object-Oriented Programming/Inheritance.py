def separation(func):
    def work(arg):
        sep_begin = "-----------------------------"
        sep_end =   "============================="
        print(sep_begin)
        func(arg)
        print(sep_begin)
        print("func:", func)
        print(sep_begin)
        print("arg:", arg)
        print(sep_end)
    return work

class Person:

    def __init__(self, name, age = 1):
        self.__name = name
        self.__age = age

    def get_info(self):
        return("Имя: {}\tВозраст: {}".format(self.name, self.age))

    @separation
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

class Employee(Person):

    def __init__(self,name, age, company):
        Person.__init__(self, name, age)
        self.company = company

    def get_info(self):
        return "{}\nКомпания: {}".format(Person.get_info(self), self.company)

    @separation
    def disp_info(self):
        print(Employee.get_info(self))

class Student(Person):

    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university

    def get_info(self):
        return "{}\nучится в университете: {}".format(Person.get_info(self), self.university)

    @separation
    def disp_info(self):
        print(Student.get_info(self))

person1 = Person("Том")
person1.name = "Томас"
person1.age = 35

empl1 = Employee("Трудоголик", 36, "Помойка")
stud1 = Student("Неуч", 20, "Шарага")

person1.disp_info()
empl1.disp_info()
stud1.disp_info()