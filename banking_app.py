{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Account:\n",
    "    def __init__ (self,  account_number , account_holder , balance) :\n",
    "        self.account_number = account_number\n",
    "        self.account_holder = account_holder\n",
    "        self.balance = balance\n",
    "        \n",
    "    def deposit_money (self , deposit) :\n",
    "        self.balance += deposit\n",
    "        return self.balance\n",
    "        \n",
    "    def withdraw_money (self, withdraw) :\n",
    "        self.balance = self.balance - withdraw\n",
    "        return self.balance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class SavingsAccount (Account) :\n",
    "    \n",
    "    def Interest (Account) :\n",
    "        return Account.balance * (1/10)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Account Holder :  Justin\n",
      " Account Number :  101872654\n",
      " Account Balance :  4000\n",
      " Account Balance After Deposit :  4500\n",
      "Account Balance After Wihtdraw : 3800\n",
      "New Balance :  3800\n",
      "Bank Interest :  380.0\n"
     ]
    }
   ],
   "source": [
    "user1 = SavingsAccount(101872654 , \"Justin\" , 4000)\n",
    "print(\" Account Holder : \", user1.account_holder )\n",
    "print(\" Account Number : \", user1.account_number )\n",
    "print(\" Account Balance : \", user1.balance )\n",
    "\n",
    "user1.deposit_money(500)\n",
    "print(\" Account Balance After Deposit : \", user1.balance )\n",
    "user1.withdraw_money(700)\n",
    "print(\"Account Balance After Wihtdraw :\" , user1.balance)\n",
    "print(\"New Balance : \", user1.balance)\n",
    "print(\"Bank Interest : \", user1.Interest())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
