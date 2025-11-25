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

    def __str__(self):
        return f"Empresa: {self.name}, Tamaño: {self.size}"

    def get_name(self):
        return self.name
    
    def get_size(self):
        return self.size
    
    def _isFull(self):
        freeSpace = False
        i = 0
        while not freeSpace and i < len(self.employeeList):
            if self.employeeList[i] is None:
                freeSpace = True
            i += 1
    
    def get_employee(self, index):
        if 0 <= index < len(self.employeeList):
            return self.employeeList[index]
        return None
    
    def hire_employee(self, employee_name, employee_salary, write_file=False, data=[]):
        if not self._isFull():
            new_employee = Employee(employee_name, employee_salary, self)
            if self.locate_employee(new_employee) == -1:
                for i in range(len(self.employeeList)):
                    if self.employeeList[i] is None:
                        self.employeeList[i] = new_employee

                        if write_file:
                            self._write_in_file(data)

                        return True
        
        return False

    def sack_employee(self, index, write_file=False, data=[]):
        if 0 <= index < len(self.employeeList):
            self.employeeList[index] = None
            if write_file:
                self._write_in_file(data)
            return True
        return False
    
    def locate_employee(self, employee):
        for i in range(len(self.employeeList)):
            if self.employeeList[i] is not None and self.employeeList[i]== employee:
                return i
        return -1
    
    def _write_in_file(self, data=[]):
        if len(data) == 0:
            string = f"{self.get_name()};{self.get_size()}"

            for employee in self.employeeList:
                if not isinstance(employee, type(None)):
                    string += f"\n{employee.get_name()};{employee.get_salary()}"
                else:
                                    string += f"\n{employee}"

            string += f"\n===============================\n"

        else: 
            string = ""

            for enterprise in data:
                string += f"{enterprise.get_name()};{enterprise.get_size()}"

                for employee in enterprise.employeeList:
                    if not isinstance(employee, type(None)):
                        string += f"\n{employee.get_name()};{employee.get_salary()}"
                    else:
                        string += f"\n{employee}"

                string += f"\n===============================\n"

        with open("poo_and_files/MisEmpleados.dat", "w") as file:
            file.write(string)
