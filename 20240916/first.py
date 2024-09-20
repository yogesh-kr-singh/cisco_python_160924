class Employee:
    def __ini10t__(self, name, address, code, salary):
        self.name = name
        self.address = address
        self.code = code
        self.salary = salary
    
    def __str__(self):
        return f'{self.name},{self.address},{self.code},{self.salary}'

Yogesh = Employee('Yogesh', 'Patna_801503', 'AB1234567890', 500000)
print(Yogesh)