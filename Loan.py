#!/usr/bin/python3
'''
Loan class to help abstract initial loan balances and payments
'''


class Loan:
    def __init__(self, prin_balance, apr, unpaid_int=0, prin_paid=0, interest_paid=0):
        self.balance = prin_balance
        self.apr = apr
        self.interest = unpaid_int
        self.prin_paid = prin_paid
        self.interest_paid = interest_paid
        
    def pay(self, amount):
        princ_pay = amount - self.monthly_interest()
        self.balance -= princ_pay
        self.interest_paid += self.monthly_interest()

        #in case we over pay the last month
        over_paid = 0
        if (self.balance < 0 ):
            over_paid = princ_pay - self.balance
        return over_paid
        
    def monthly_interest(self):
        return self.balance * self.apr/12

    def is_zero(self):
        if (self.balance + self.interest) > 0:
            return False
        else:
            return True
