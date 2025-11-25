from Employee import Employee
from Enterprise import Enterprise

def create_data():
    enterprise = Enterprise("RetroCorp", 10)

    enterprise.hire_employee("Alice", 50000)
    enterprise.hire_employee("Bob", 60000)
    enterprise.hire_employee("Charlie", 55000)
    enterprise.hire_employee("Diana", 70000)
    enterprise.hire_employee("Eve", 65000)

    return enterprise

def load_data():
    loaded_data = []
    with open("poo_and_files/MisEmpleados.dat", "r") as file:
        lines = file.read()
        
    if len(lines) > 0:
        lines = lines.split("===============================")
        for element in lines:
            if element != "" and element != "\n":
                cleaned_element = element.split()
                print(cleaned_element)
                enterprise, employees = cleaned_element[:1][0], cleaned_element[1:]
                e = Enterprise(enterprise.split(";")[0], int(enterprise.split(";")[1]))

                for emp in employees:
                    if emp != "None":
                        name, salary = emp.split(";")
                        e.hire_employee(name, float(salary))
                        
                loaded_data.append(e)
                

    else:
        loaded_data = [create_data()]

    return loaded_data

# Ejercicio 1
data = load_data()

for enterprise in data:
    print("================================")
    print(enterprise)
    print("Empleados:")
    for employee in enterprise.employeeList:
        if not isinstance(employee, type(None)):
            print(employee)
    print("================================")

# Ejercicio 2
data[0].hire_employee("Rafa", 72000, write_file=True, data=data)

# Ejercicio 3
data[0].sack_employee(1, write_file=True, data=data)