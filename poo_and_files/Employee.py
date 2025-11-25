from typing import final
from Enterprise import Enterprise

class Employee:

    _employee_number = 0

    def __init__(self, name, salary, enterprise):
        self._employee_number = Employee._employee_number + 1
        Employee._employee_number += 1
        self.name = name
        self.salary = salary
        self.enterprise = enterprise

    def __str__(self):
        return f"Empleado Nº: {self._employee_number}, Nombre: {self.name}, Salario: {self.salary}, Empresa: {self.enterprise}"

    def __eq__(self, value):
        if not isinstance(value, Employee):
            return False
        return self.name == value.name and self.salary == value.salary and self.enterprise == value.enterprise

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary
    
    def set_employee_number(self, employee_number):
        self._employee_number = employee_number

    def get_employee_number(self):
        return self._employee_number
    
    @final
    def raise_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

    def dimiss_employee(self):
        valid = self.enterprise.sack_employee(self.enterprise.locate_employee(self))

        if valid:
            print(f"{self.name} ha sido despedido de {self.enterprise.get_name()}.")
            self.enterprise = None
        else: 
            print(f"No se ha podido despedir a {self.name} de {self.enterprise.get_name()}.")
    
    
