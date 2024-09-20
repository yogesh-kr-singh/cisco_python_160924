class Account:
    def __init__(self, number, name, intitial_amount=1000) :
        self._number = number
        self._name = name
        self._balance = intitial_amount
        
    def __repr__(self) -> str:
        return f'[number={self._number},{self._name},{self._balance}]'
    
    def __str__(self) -> str:
        return self.__repr__()

    def deposit(self, amount) -> str:
        self._balance += amount
    
    def withdraw(self, amount) -> str:
        if amount <= self._balance:
            print('- - - - No Enough Balance - - - -')
            return
        self._balance -= amount

    # end def
# end class

rohit_ac = Account(name = 'Rohit', number='12345678901', intitial_amount=50000)
print(rohit_ac)

rohit_ac.deposit(2000000)
print(rohit_ac)

rohit_ac.withdraw(567890)
print(rohit_ac)

# print(rohit_ac.__dict__)
# print(rohit_ac._balance)

rohit_ac.withdraw(500000000)
print(rohit_ac)



