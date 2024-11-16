class Human:
    height = 170


class Student(Human):
    gladness = 40


class Worker(Human):
    gladness = 60


nick = Student()
ann = Worker()
print(nick.height)
print(nick.gladness)
print(ann.height)
print(ann.gladness)


class GrandParent:
    height = 170
    gladness = 90
    age = 70


class Parent(GrandParent):
    age = 30


class Child(Parent):
    height = 100

    def __init__(self):
        print(self.height)
        print(self.gladness)
        print(self.age)


ch = Child()


class hello_world:
    hello = 'hello'
    _hello = '_hello'
    __hello = '__hello'

    def __init__(self):
        self.world = 'world'
        self._world = '_world'
        self.__world = '__world'

    def printer(self):
        print(self.hello + self.world)
        print(self._hello + self._world)
        print(self.__hello + self.__world)





hello = hello_world()
hello.printer()


class Class1:
    def __init__(self):
        print('hello')


class Class2(Class1):
    def __init__(self):
        super().__init__()
        print('World')


x = Class2


class Class1:
    var = 20

    def __init__(self):
        self.var = 10


class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)


x = Class2()


class Computer:

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128

    def calculate(self):
        print('calculating....................... ')


class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = '360k'

    def display(self):
        print('i show the img on the screen')


class DumbPhone(Display, Computer):
    def info(self):
        print(self.memory)
        print(self.model)
        print(self.resolution)


iphone = DumbPhone(model='S400 Pro Mega Master Ultra Max Air')
iphone.display()
iphone.calculate()
iphone.info()