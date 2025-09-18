# a company pays employees for hours worked. Standard wroking hours = 40.
# any hours worked above 40 are paid at a rate of 1.5 times the standard hourly rate.
# use a function to compute salary and a lambda for over time calculation.
# sample input
# ramesh
# 200
# 45
# employee : ramesh
# total salary: 9500.00
employee_name = input("Enter employee name: ")
hourly_rate = float(input("Enter hourly rate: "))
hours_worked = float(input("Enter hours worked: "))
overtime_rate = lambda rate: rate * 1.5
standard_hours = 40
if hours_worked > standard_hours:
    overtime_hours = hours_worked - standard_hours
    total_salary = (standard_hours * hourly_rate) + (overtime_hours * overtime_rate(hourly_rate))
else:
    total_salary = hours_worked * hourly_rate
print(f"Employee: {employee_name}")
print(f"Total salary: {total_salary:}")


'''format 
student_name: ganesh
marks: m1, m2, m3, m4, m5, m6
input
student_name: ganesh
marks: 90,85,80,96,92,85
ouput
student_name: ganesh
marks: 90,85,80,96,92,85
total: 528
average: 88.0
grade: A
use map function of marks data in one line
a= >90
75<b>89
51<c>75
fail<50'''
student_name = input("Enter student name: ")
marks = list(map(int, input("Enter marks (comma separated): ").split(',')))
total = sum(marks)
average = total / len(marks)
if average >= 90:
    grade = 'A'
elif 75 <= average < 90:
    grade ='B'
elif 51<=average>=74:
    garde ='c'
else:
    grade='fail'
print(f"student_name: {student_name}")
print(f"marks: {', '.join(map(str, marks))}")
print(f"total: {total}")
print(f"average: {average:.2f}")



# format
# product_name
# price
# quantity
# sample output
# laptop
# 25000
# 1
# total price: 25000
# discount: 10%
# final price: 22500
product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total_price = price * quantity
discount = total_price * 0.1  # Assuming discount is 10%
final_price = total_price - discount
print(f"product_name: {product_name}")
print(f"price: {price}")
print(f"quantity: {quantity}")
print(f"total price: {total_price}")
print(f"discount: {discount}")
print(f"final price: {final_price}")



class Engineer:
    def __init__(self):
        pass
    def work(self):
        print("Engineer is working............")
class SoftwareEngineer(Engineer):
    def __init__(self):
        super().__init__()
    def work(self):
        print("Software Engineer is coding...........")
class CivilEngineer(Engineer):
    def __init__(self):
        super().__init__()
    def work(self):
        print("Civil Engineer is building...........")
e=Engineer()
e.work()
se=SoftwareEngineer()
se.work()
ce=CivilEngineer()
ce.work()

# 4) Bank Account Simulation (deposit & withdraw)
# Problem statement:
# Simulate an account. Read customer name and initial balance
# (may be string → float). Accept a withdrawal amount and
# deposit amount (convert types). Implement deposit and
# withdraw via functions and create a BankAccount class
# with deposit() and withdraw() methods. Withdrawal
# should refuse if insufficient balance. Apply a 1% transaction
# fee on withdrawals implemented with a lambda.
# Input format:
# name
# initial_balance
# withdraw_amount
# deposit_amount
# Sample Input
# Ananya
# 5000
# 2000
# 3000
# Sample Output
# Account Holder: Ananya
# Final Balance: ₹6000.00
customer_name = input("Enter customer name: ")
initial_balance = float(input("Enter initial balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
deposit_amount = float(input("Enter deposit amount: "))
transaction_fee = lambda amount: amount * 0.01
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        fee = transaction_fee(amount)
        total_withdrawal = amount + fee
        if total_withdrawal > self.balance:
            print("Insufficient balance for this withdrawal.")
        else:
            self.balance -= total_withdrawal

    def get_balance(self):
        return self.balance
# Input
name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(name, initial_balance)
withdraw_amount = float(input("Enter withdrawal amount: "))
account.withdraw(withdraw_amount)
deposit_amount = float(input("Enter deposit amount: "))
account.deposit(deposit_amount)
# Output
print("Account Holder:", account.name)
print("Final Balance: ₹{:.2f}".format(account.get_balance()))



# duck typing program
class Duck:
    def speak(self):
        print("quack quack quack quack quack")

class Horse:
    def speak(self):
        print("neigh neigh neigh neigh neigh")

def myfunction(object):
    object.speak()
d = Duck()
myfunction(d)
h = Horse()
myfunction(h)


