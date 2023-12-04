import copy
class Complex_Number:
    def __init__(self, rpart, ipart):
        if isinstance(rpart, int) or isinstance(rpart, float):
            self.rpart = copy.copy(rpart)
        else:
            raise ValueError
        if isinstance(ipart, int) or isinstance(ipart, float):
            self.ipart = copy.copy(ipart)
        else:
            raise ValueError

    def __str__(self):
        print(f'{self.rpart} + {self.ipart}j')
    
    def __add__(self, other):
        return Complex_Number(round(self.rpart + other.rpart), round(self.ipart + other.ipart))
    
    def __sub__(self, other):
        return Complex_Number(round(self.rpart - other.rpart), (self.ipart - other.ipart))
    
    def __mul__(self, other):
        nrpart = self.rpart * other.rpart - self.ipart * other.ipart
        nipart = self.rpart * other.ipart + self.ipart * other.rpart
        return Complex_Number(nrpart, nipart)
    
    def __rmul__(self, other):
        nrpart = self.rpart * other.rpart - self.ipart * other.ipart
        nipart = other.rpart * other.ipart + self.ipart * other.rpart
        return Complex_Number(nrpart, nipart)
    
    def couple(self):
        return Complex_Number(self.rpart, -self.ipart)
    
    def __truediv__(self, other):
        div = other.rpart**2 + other.ipart**2
        rpart = ((self*(other.couple())).rpart)
        ipart = ((self*(other.couple())).ipart)
        return Complex_Number(rpart/div, ipart/div)
    
    def module(self):
        return (self.rpart**2 + self.ipart**2)**(1/2)