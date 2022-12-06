# Todo Unlimited Positional Arguments

def add(*args):
    print(args[1])  # Can also access index of args because args is a tuple data type
    sum_ = 0
    for num in args:
        sum_ += num
    print(sum_)


add(1, 2, 3, 4, 6)  # can call unlimited of numbers because of *args


# Todo Unlimited Keyword arguments

def calculate(n, **kwargs):
    print(kwargs)  # kwargs is a dictionary
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]  # accessing keyword argument values
    n *= kwargs["multiple"]
    print(n)


calculate(2, add=3, multiple=5)


# Todo creating optional kwargs

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")  # .get alternate to kwargs[make] which gives error if no argument is passed
        self.model = kwargs.get("model")  # if we use kwargs[model],if we don't give value to it then it will give error
        # self.engine = kwargs["speed"]
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", colour="black")
print(my_car.colour)
