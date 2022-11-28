from BankAcc import BankAccount

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