from enum import Enum

class Type(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"

class CuentaBancaria:

    def __init__(self, titular, amount, type = Type.AHORROS):
        self.titular = titular
        self.amount = amount
        self.type = type

    def show_info(self):
        return f"Monto actual: {self.amount}"

    def deposit_money(self, amount):
        if amount > 0:
            self.amount += amount
            return f"Depósito exitoso. Nuevo saldo: {self.amount}"
        else:
            return "El monto a depositar debe ser positivo."
        
    def withdraw_money(self, amount):

        if amount < 0:
            return "El monto a retirar debe ser positivo."

        if amount > self.amount:
            return "Fondos insuficientes para retirar."
        
        self.amount -= amount
        return f"Retiro exitoso. Nuevo saldo: {self.amount}"
        
