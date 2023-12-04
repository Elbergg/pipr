import copy
class Fraction:
    def __init__(self, numerator, denominator, is_zero = False):
        self.gcd = self.GCD(denominator, numerator)
        self.denominator = int(denominator/self.gcd)
        if self.denominator == 0:
            raise ZeroDivisionError
        self.numerator = int(numerator/self.gcd)
        self.is_zero = is_zero
        if self.numerator == 0:
            self.is_zero = True
            self.numerator = 0
            self.denominator = 1
        if self.numerator < 0 or self.denominator < 0:
            self.numerator = -self.numerator
        if self.denominator < 0:
            self.denominator = -self.denominator
    
    def __add__(self, other):
        if self.react_when_zero(other) is not None:
            return self.react_when_zero(other)
        return Fraction(int(self.numerator*other.denominator+other.numerator*self.denominator), int(self.denominator*other.denominator))
    
    def GCD(self, denominator, numerator):
        while numerator != 0:
            gcd = denominator % numerator
            denominator = copy.copy(numerator)
            numerator = copy.copy(gcd)
        return denominator
    
    def __sub__(self, other):
        if self.react_when_zero(other) is not None:
            return self.react_when_zero(other)
        return Fraction(int(self.numerator*other.denominator-other.numerator*self.denominator), int(self.denominator*other.denominator))

    def __mul__(self, other):
        if self.is_zero is True or other.is_zero is True:
            return Fraction(0,1)
        return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)
    
    def __rmul__(self, other):
        if self.is_zero is True or other.is_zero is True:
            return Fraction(0,1)
        return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)
    
    def __truediv__(self, other):
        if other.is_zero is True:
            raise ZeroDivisionError
        if self.is_zero is True:
            return Fraction(0,1)
        return Fraction(self.numerator*other.denominator, self.denominator*other.numerator)
    
    def add_constant(self, cons):
        return Fraction(self.numerator+self.denominator*cons, self.denominator)
    
    def get_numerator(self):
        return self.numerator
    
    def get_denominator(self):
        return self.denominator
    
    def set(self, new_nominator, new_denominator):
        return Fraction(new_nominator, new_denominator)
    
    def get_value(self):
        return self.numerator/self.denominator
    
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
    
    def react_when_zero(self, other):
        if self.is_zero == True:
            return Fraction(other.numerator, other.denominator)
        if other.is_zero == True:
            return Fraction(self.numerator, self.denominator)
        return None
    