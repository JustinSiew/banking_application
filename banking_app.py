class Account:
    def __init__ (self,  account_number , account_holder , balance) :
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit_money (self , deposit) :
        self.balance += deposit
        return self.balance
        
    def withdraw_money (self, withdraw) :
        self.balance = self.balance - withdraw
        return self.balance
    
class SavingsAccount (Account) :
    
    def Interest (Account) :
        return Account.balance * (1/10)
    
user1 = SavingsAccount(101872654 , "Justin" , 4000)
print(" Account Holder : ", user1.account_holder )
print(" Account Number : ", user1.account_number )
print(" Account Balance : ", user1.balance )

user1.deposit_money(500)
print(" Account Balance After Deposit : ", user1.balance )
user1.withdraw_money(700)
print("Account Balance After Wihtdraw :" , user1.balance)
print("Bank Interest : ", user1.Interest())