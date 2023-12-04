class BoundingBox:
    def __init__(self, left_bottom: tuple, right_top: tuple):
        self.left_bottom = left_bottom
        self.right_top = right_top
        for i in self.left_bottom:
            if i < 0 or i > 1024:
                raise ValueError
        for i in self.right_top:
            if i < 0 or i > 1024:
                raise ValueError

    def calculate_area(self):
        ywall = self.right_top[0] - self.left_bottom[0]
        xwall = self.right_top[1] - self.left_bottom[1]
        return ywall*xwall
    
    def calculate_intersection(self, other):
        if min([other.left_bottom[1] - self.right_top[1], other.right_top[1] - self.left_bottom[1]]) > 0:
            return 0
        interxwall = min([
            other.right_top[0] - self.left_bottom[0],
              self.right_top[0] - other.left_bottom[0]
            ])
        interywall = min([
            self.right_top[1]-other.left_bottom[1],
              other.right_top[1] - self.left_bottom[1]
            ])
        return interxwall*interywall 
    
    def calculate_sum(self, other):
        inter_area = self.calculate_intersection(other)
        return self.calculate_area() + other.calculate_area() - inter_area
    
    def calculate_int_over_un(self, other):
        return self.calculate_intersection(other)/self.calculate_sum(other)
    
    def calculate_f1(self, other):
        numerator = 2*self.calculate_intersection(other)
        denominator = self.calculate_area() + other.calculate_area()
        return numerator/denominator
    
    def __str__(self):
        return f'lewy dolny wierzcholek: {self.left_bottom}, prawy gorny wierzcholek {self.right_top}'
    

    