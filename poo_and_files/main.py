from Enterprise import Enterprise
from Employee import Employee

e1 = Employee("Alice", 50000, "TechCorp")
e2 = Employee("Bob", 60000, "TechCorp")
e3 = Employee("Bob", 60000, "TechCorp")

print(e1.get_employee_number()," ",e3.get_employee_number())