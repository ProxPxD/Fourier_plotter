import math

class Expression:

    def __init__(self, coef=1, frequency=1):
        self.coef = coef
        self.frequency = frequency

    def calc(self, t):
        return complex(self.coef * math.cos(self.frequency * 2 * math.pi * t),
                       self.coef * math.sin(self.frequency * 2 * math.pi * t))

    def __mul__(self, other):
        if isinstance(other, Expression):
            self.coef *= other.coef
            self.frequency += other.frequency
        elif isinstance(other, (float, int)):
            self.coef *= other

    def __eq__(self, other):
        return self.coef == other.coef and self.frequency == other.frequency

    def __str__(self):
        if self.frequency == 0:
            return str(self.coef)
        else:
            return '{:.4}e^({}*2πit)'.format(self.coef, self.frequency)