from Enterprise import Enterprise

class Employee:

    _employee_number = 0

    def __init__(self, name, salary, enterprise):
        self._employee_number = Employee._employee_number + 1
        Employee._employee_number += 1
        self.name = name
        self.salary = salary
        self.enterprise = enterprise

    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary
    
    def get_employee_number(self):
        return self._employee_number
