class Human:
    def __init__(self, name='human'):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for p in args:
            self.passengers.append(p)

    def print_passenger_name(self):
        if self.passengers:
            print(f'Names of {self.brand} passengers: ')
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print('There are no passengers =(')


kate = Human(name='kate')
nick = Human(name='nick')

car = Auto('mercedes')
car.add_passenger(kate)
car.add_passenger(nick)
car.print_passenger_name()
