mylist = [1, 2, 3]
iterator = iter(mylist)
print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))
print('==============')
mylist = [1, 2, 3]
iterator = iter(mylist)

for item in iterator:
    print(item)

for item in iterator:
    print(item)


class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i


counter = Counter(5)
for i in counter:
    print(i)


def reisetodegree(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i
        i += 1


for i in reisetodegree(123345, 500):
    print(i)


class Car:
    def __init__(self, brand):
        self.brand = brand
        print('Its a Car class. Im an init function/')

    def __call__(self, passengers, *args, **kwargs):
        return f'Its a Car {self.brand} with {passengers} passengers'


car = Car('BMW')
print(car(4))


def helper(work):
    work_in_memory = work

    def helper(work):
        return f'Ill help you wit {work_in_memory}. After i will help with {work}'

    return helper


help_ = helper('homework')
print(help_('cleaning'))
print(help_('playing football'))

print(
    helper('homework')('cleaning')
)


def checker(*exc_types):
    def checker(func):
        def checker(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except (exc_types) as ex:
                print(f'we have a problem {ex}')
            else:
                print(f'no problems. result: {result}')
                print(f'{exc_types}')
        return checker
    return checker


@checker(TypeError, SyntaxError, ZeroDivisionError)
def calculate(expression):
    return eval(expression)


calculate("2/0")
