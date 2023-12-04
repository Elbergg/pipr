import copy 
class NotEnoughRestError(Exception):
    def __init__(hours_of_rest):
        super().__init__('The driver must still rest')

class DriverMustRestError(Exception):
    def __init__(hours_of_drive):
        super().__init__('The driver must rest')

class Delivery:
    def __init__(self):
        self.target = ''
        self.hours_of_drive = 0
        self.hours_of_rest = None
        self.distance = 0
        self.home_name = 'Warszawa'
        self.distance_to_home = 0
        self.destination_dictionary = {'Kraków': 290, 'Gdańsk': 340, 'Poznań': 312, 'Rzeszów': 330, 'Terespol': 197}
        
    def submit_order(self, target):
        self.hours_of_drive = 0
        if target == self.target or target not in self.destination_dictionary:
            raise ValueError
        self.target = target
        self.hours_of_rest = None
        self.distance = self.destination_dictionary.get(target)
        self.distance_to_home = copy.copy(self.distance)

    def drive(self, hours):
        distance_left = self.distance - hours*80
        self.distance -= hours*80
        if self.hours_of_rest:
            if self.hours_of_rest >= 3:
                self.hours_of_rest = None
        if self.hours_of_drive + hours > 3:
            raise DriverMustRestError
        self.hours_of_drive += hours
        if self.hours_of_rest:
            if self.hours_of_rest < 3:
                raise NotEnoughRestError
        if distance_left <= 0 and self.target == 'Warszawa':
            self.reset_after_return()
        elif distance_left <= 0:
            self.start_returning_home()

    def rest(self, hours):
        self.hours_of_rest = 0
        self.hours_of_rest += hours
        self.hours_of_drive = 0
    
    def start_returning_home(self):
        self.target = 'Warszawa'
        self.distance = copy.copy(self.distance_to_home)

    def reset_after_return(self):
        self.target = ''
        self.hours_of_drive = 0
        self.hours_of_rest = None
        self.distance = 0
        
    def __str__(self):
        return(f'The destination is {self.target}, there are {self.distance}km left, the driver can drive for {3-self.hours_of_drive} more hours.')