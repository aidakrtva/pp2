class Account:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance 

    def deposit (self, addedmoney) :
        self.addedmoney = addedmoney
        self.newmoney = self.balance + self.addedmoney

        if self.newmoney > 0:
            print (f"{self.owner}'s balance is = {self.newmoney} tg")
        elif self.balance == 0 :
            print (f"{self.owner} is broke, your balance is = 0")
        
    def withdraw (self , neededmoney):
        self.neededmoney = neededmoney
        print (f"{self.owner}, you withdrawn from account {self.neededmoney} tg")

        if (self.neededmoney > self.balance):
            print (f"{self.owner}, you dont have enought money ha-ha")
        else :
            print (f"{self.owner}'s balance now is {self.newmoney - self.neededmoney}")

account = Account("Bob", 1000000)
account.deposit(55555)
account.withdraw(100)