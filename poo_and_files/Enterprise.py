from Employee import Employee
class Enterprise:

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.employeeList = [None for _ in range(size)]

    def __eq__(self, value):
        if not isinstance(value, Enterprise):
            return False
        return self.name == value.name

    def get_name(self):
        return self.name
    
    def get_size(self):
        return self.size
    
    def _isFull(self):
        return len(self.employeeList) >= self.size
    
    def get_employee(self, index):
        if 0 <= index < len(self.employeeList):
            return self.employeeList[index]
        return None
    
    def hire_employee(self, employee_name, employee_salary):
        if not self._isFull():
            new_employee = Employee(employee_name, employee_salary, self)
            if self.locate_employee(new_employee) == -1:
                for i in range(len(self.employeeList)):
                    if self.employeeList[i] is None:
                        self.employeeList[i] = new_employee
                        return True
        
        return False

    def sack_employee(self, index):
        if 0 <= index < len(self.employeeList):
            self.employeeList[index] = None
            return True
        return False
    
    def locate_employee(self, employee):
        for i in range(len(self.employeeList)):
            if self.employeeList[i] is not None and self.employeeList[i]== employee:
                return i
        return -1