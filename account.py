'''Create a class Account with the below attributes:

account_no of type

Number account_name of type

String account_baIance of type Number

Create the finite method which takes all parameters in the above sequence and sets the value of the attributes inside the method.

Create a method depositAmnt inside the Account class which takes a number value as input parameter. The number value represents the amount to be deposited into the Account. The method updates the balance of the Account i.e. adds the given amount to the existing balance of the Account object.

Create another method withdrawAmnt inside the Account class which takes a number value as the input parameter. The number value represents the amount to be withdrawn from the Account. The method deducts the amount from the existing balance of the Account object.

However, the minimum balance of the Account object is to be maintained as 1000. i.e. withdrawal of the given amount will be possible only if the balance of the Account object is greater than or equal to 1000 after the amount is withdrawn. The method returns 1 if the withdrawal is possible; else returns 0 if the withdrawal is not possible.

To test the code against your customized input through the console, the input data needs to be entered in the below order( as shown below in the sample input).

The first three lines in the below sample input represent the input for three variables of the account object

i.e. account no. (account_no), account name (account_name), and account balance (account_baIance), with which the Account object will be created.

The fourth line in the sample input is the input for the amount to be deposited in the account object and the fifth line is the input for the amount to be withdrawn from the account object'''


class Account:
    def __init__(self,accnt_no,accnt_name,accnt_bal):
        self.account_number=accnt_no
        self.account_name=accnt_name
        self.account_balance=accnt_bal
    
    def deposit(self,num):
        self.account_balance+=num
    
    def withdraw(self,num):
        if self.account_balance-num<1000:
            return 0
        else:
            self.account_balance-=num
            return 1
            
accnt_no=int(input())
accnt_name=input()
accnt_bal=int(input())
dep_amnt=int(input())
withdraw_amt=int(input())

obj=Account(accnt_no,accnt_name,accnt_bal)

obj.deposit(dep_amnt)
print("Balance after deposit=",obj.account_balance)

res=obj.withdraw(withdraw_amt)
if res==0:
    print("Insufficient Balance")
else:
    print("Balance after withdraw=",obj.account_balance)
