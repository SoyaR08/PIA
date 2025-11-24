class Enterprise:

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.employeeList = [None for _ in range(size)]

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
            for i in range(len(self.employeeList)):
                if self.employeeList[i] is None:
                    self.employeeList[i] = {
                        'name': employee_name,
                        'salary': employee_salary
                    }
                    return True
        
        return False

    def sack_employee(self, index):
        if 0 <= index < len(self.employeeList):
            self.employeeList[index] = None
            return True
        return False