class Price:
    def __init__(self, value, currency, currencies = {'eur': 5, 'usd': 4, 'pln': 1}):
        self.value = value
        self.currency = currency
        self.currencies = currencies
   # def __add__(self, other, currency = 'pln'):

    def convert(self, new_currency):
        pln_value = self.currencies.get(self.currency)*self.value
        new_value = int((pln_value/self.currencies.get(new_currency)))
        self.value = new_value
        self.currency = new_currency         

    def add(self, other, currency = 'pln'):
        self.convert(currency)
        other.convert(currency)
        return Price(self.value + other.value, currency)
    
    def sub(self, other, currency = 'pln'):
        self.convert(currency)
        other.convert(currency)
        return Price(self.value - other.value, currency)

    def __mul__(self, constant):
        self. value = self.value*constant
    def __rmul__(self, constant):
        self. value = self.value*constant

    def __str__(self):
        return f'{self.value//100}.{self.value%100:02} {self.currency}'