from BankAcc import BankAccount
from inheritance import *
from method_res_inheritance import *

alex = BankAccount("alex", 500)
max = BankAccount("max")

print(f"Properties of alex: Holder: {alex.holder}, Balance: {alex.balance}")
print(f"Properties of max: Holder: {max.holder}, Balance: {max.balance}")

alex.deposit(100)
print(f"Properties of alex: Holder: {alex.holder}, Balance: {alex.balance}")
alex.withdraw(200)
print(f"Properties of alex: Holder: {alex.holder}, Balance: {alex.balance}")


max.withdraw(100)
print(f"Properties of alex: Holder: {max.holder}, Balance: {max.balance}")


print(alex)
print(max)

circle = Circle("blue", 1, (2,3), 5)

print(circle)
print(circle.area())

d1 = D()
# python uses BFS to search for methods
f1 = F()

j1 = J()
print(j1.y)