class Bank:
    bank_name = 'SBI'
    def __init__(self,name,age,bal):
        self.user_name = name
        self.age = age
        self.user_balance = bal

    def display(self):
        print(f"User Name: {self.user_name}, User Age: {self.age}, User Balance: {self.user_balance} for Bank {Bank.bank_name}")

b1 = Bank('Pooja',26,55555)
b1.display() # User Name: Pooja, User Age: 26, User Balance: 55555 for Bank SBI
print(b1.bank_name) #SBI
print(Bank.bank_name) #SBI

        
