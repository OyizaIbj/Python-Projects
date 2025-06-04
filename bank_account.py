{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "68d5b195-800a-4ce3-9017-6c114404bac4",
   "metadata": {},
   "source": [
    "## Bank Account Creation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "861ae2ba-9383-477d-82ec-60cd8856add8",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Account:\n",
    "    def __init__(self, account_number: str, account_holder: str, account_balance: float = 0.00):\n",
    "        \"\"\"\n",
    "        Initialize an Account object.\n",
    "        \"\"\"\n",
    "        self.account_number = account_number\n",
    "        self.account_holder = account_holder\n",
    "        self.account_balance = account_balance\n",
    "    \n",
    "    def deposit(self, amount: float):\n",
    "        \"\"\"\n",
    "        Deposit money into the account.\n",
    "        \"\"\"\n",
    "        if amount > 0:\n",
    "            self.account_balance += amount\n",
    "            print(f\"${amount:.2f} has been deposited into {self.account_number}. \\nNew balance: ${self.account_balance:.2f}\\n\")\n",
    "        else:\n",
    "            print(\"Invalid deposit amount.\\n\")\n",
    "    \n",
    "    def withdraw(self, amount: float):\n",
    "        \"\"\"\n",
    "        Withdraw money from the account if balance is sufficient enough.\n",
    "        \"\"\"\n",
    "        if 0 < amount <= self.account_balance:\n",
    "            self.account_balance -= amount\n",
    "            print(f\"${amount:.2f} has been withdrawn from {self.account_number}. \\nNew balance: ${self.account_balance:.2f}\\n\")\n",
    "        elif amount <= 0:\n",
    "            print(\"Invalid withdrawal amount.\\n\")\n",
    "        else:\n",
    "            print(\"Insufficient balance for withdrawal.\\n\")\n",
    "    \n",
    "    def check_balance(self):\n",
    "        \"\"\"\n",
    "        Return the current account balance.\n",
    "        \"\"\"\n",
    "        print(f\"{self.account_number}, your account balance is: ${self.account_balance:.2f}\\n\")\n",
    "        return self.account_balance\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ae8fbf1f-b8f4-400a-a44d-ee5058368e8c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$2000.00 has been deposited into 987654321. \n",
      "New balance: $5000.00\n",
      "\n",
      "$1500.00 has been withdrawn from 987654321. \n",
      "New balance: $3500.00\n",
      "\n",
      "987654321, your account balance is: $3500.00\n",
      "\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    \n",
    "    my_account = Account(\"987654321\", \"Oyiza Ibj\", 3000.00)   # Creating an account instance\n",
    "    \n",
    "    my_account.deposit(2000)         # Deposit $2,000\n",
    "    my_account.withdraw(1500)        # Withdraw $1,500\n",
    "    my_account.check_balance()       # Check balance\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "94a25628-b86c-45dc-bde2-c4748e1f1cbc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Insufficient balance for withdrawal.\n",
      "\n",
      "$500.00 has been deposited into 123456789. \n",
      "New balance: $1500.00\n",
      "\n",
      "123456789, your account balance is: $1500.00\n",
      "\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    \n",
    "    second_account = Account(\"123456789\", \"Ibj Oyiz\", 1000.0)   # Creating another account instance\n",
    "    \n",
    "    second_account.withdraw(1500)   # Attempting to withdraw more than balance\n",
    "    second_account.deposit(500)      # Deposit $500\n",
    "    second_account.check_balance()   # Check balance"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
