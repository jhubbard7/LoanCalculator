'''
This is the main driver which is used on the command line

'''
import argparse
import Loan

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--principal',
                        help='Principal amount on loan',
                        required=True,
                        type=float,
                        metavar='P')
    parser.add_argument('-n','--name',
                        help='Name for specific Loan. (car, student, house)',
                        required=False,
                        type=str,
                        metavar='N',
                        default='')
    parser.add_argument('-i','--interest',
                        help=r'''Interest rate on loan in terms of decimal. 
                        If it's 5.00%% enter .05''',
                        required=True,
                        type=float,
                        metavar='I')
    parser.add_argument('-m','--monthly',
                        help='Monthly payment on loan',
                        required=True,
                        type=float,
                        metavar='M')
    
    args = parser.parse_args()

    loan1 =  Loan.Loan(args.principal, args.interest)
    months = 0
    monthly_pay = args.monthly
    while(not loan1.is_zero()):
        months += 1
        loan1.pay(monthly_pay)
    message = 'Time to pay off {}loan: {} years and {} months'.format(args.name+' ', months//12, months % 12)
    print(message)
    message = 'Total interest paid over time: ${:,.2f}'.format(loan1.interest_paid)
    print(message)
        



