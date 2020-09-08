from Expression import Expression
from functools import reduce
from math import pi

def iterable(obj):
    try:
        iter(obj)
    except Exception:
        return False
    else:
        return True


class Fourier:

    def __init__(self, *args):
        self.expressions = []
        self.sorted = False
        if len(args):
            new_obj = Fourier()
            for arg in args:
                new_obj += arg
            #self.__dict__.update(new_obj.__dict__)

    def calc(self, t):
        return sum(map(lambda e: e.calc(t), self.expressions))

    def clear(self):
        self.expressions.clear()

    def set_step_function(self, precision=5):
        self.clear()
        for i in range(precision):
            self.__add__([4/pi /((2*i + 1) * (-1) ** i), (2*i + 1)])

    def __add__(self, other):
        self.sorted = False
        if isinstance(other, (float, int)):
            self.expressions.append(Expression(other))
        elif iterable(other):
            c = other[0]
            f = other[1]
            self.expressions.append(Expression(c, f))
        elif isinstance(other, Expression):
            self.expressions.append(other)
        return self

    def sort(self):
        self.expressions = sorted(self.expressions, key=lambda e: e.frequency)
        self.sorted = True

    def __str__(self):
        if not self.sorted:
            self.sort()
        string = "f(t) = "
        for expr in self.expressions:
            if expr == self.expressions[0]:
                string += str(expr)
            else:
                string += str(expr) if expr.coef < 0 else '+{}'.format(expr)
        return string