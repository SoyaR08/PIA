from classes import CuentaBancaria, Type
# Ejercicio 3

print("============= Ejercicio 3 =============")

account = CuentaBancaria("Ana Pérez", 1000, Type.AHORROS)

print(account.deposit_money(500))
print(account.show_info())
print(account.withdraw_money(1700))
print(account.show_info())
print(account.withdraw_money(1400))
print()