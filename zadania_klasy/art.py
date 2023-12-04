class Artist:
    def __init__(self, name="", birthday=0) -> None:
        self._name = name
        if self._name == "":
            self._name = 'unknown'
        if not isinstance(name, str):
            raise ValueError
        self._birthday = birthday
        if self._birthday == 0:
            self._birthday = 'unknown'
        if not isinstance(birthday, int):
            raise ValueError
    
    def name(self):
        return self._name
    
    def bday(self):
        return self._birthday

    def __str__(self) -> str:
        return f'The artists name is {self._name} and his/her date of birth is {self._birthday}'
    
    def set_name(self, new_name):
        if not new_name:
            raise ValueError
        self._name = new_name

    def set_birthday(self, new_age):
        self._birthday = new_age
        