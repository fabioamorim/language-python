from person import Person

class Employee(Person):

    def __init__(self, name, age, re):
        super().__init__(name, age)
        self._re = re 

    @property
    def re(self):
        return self._re 
    
    @re.setter
    def re(self, re):
        self._re = re 

    def __str__(self):
        return f'{self._name} - {self._age} - {self._re}'
    
    def about(self):
        print("This is about this employee")