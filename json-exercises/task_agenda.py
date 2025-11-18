import json
import random as rd
import datetime as dt

def insertData(data):
    tasks_names = ["Testear código", "Tomarse un café", "Actualizar Jira", "Documentar", "Documentar x2", 
                "Documentar x3", "Elegir una playlist para trabajar", "Sacar al perro", "Limpiar el baño",
                "Hacer la cena"]
    tasks_dates = range(17, 31)
    tasks_status = ["pendiente", "completada"]

    for i in range(10):
        description = rd.choice(tasks_names)
        tasks_names.remove(description)
        task = {
            "descripcion": description,
            "vencimiento": f"2025-11-{rd.choice(tasks_dates)}",
            "estado": rd.choice(tasks_status)
        }

        data.append(task)

def addNewTask(data):

    newTaskDescription = input("Inserte descripción de la nueva tarea: ")
    newTaskState = "pendiente"
    newTaskLimitDate = dt.date.today().strftime("%Y-%m-%d")

    newTask = {
        "descripcion": newTaskDescription,
        "vencimiento": newTaskLimitDate,
        "estado": newTaskState
    }

    data.append(newTask)
    return newTask

def findTaskByDescription(data, taskDescription):
    product = list(filter(lambda x: taskDescription.lower() in x["descripcion"].lower() , data))
    return product[0] if len(product) > 0 else -1

def updateTaskState(data, taskName, newState):
    task = findTaskByDescription(data, taskName)
    task["estado"] = newState

    return f"Tarea actualizada: {task}"

def filterTasksByState(data, state):
    filtered_tasks = list(filter(lambda x: state.lower() in x["estado"].lower(), data))
    return filtered_tasks

file = open("jsons/tasks_agenda.json", "rt")

json_string = file.read()

data = json.loads(json_string)


insertData(data["tareas"])
print(addNewTask(data["tareas"]))
print(updateTaskState(data["tareas"], "Estudiar Python", "completada"))
print(filterTasksByState(data["tareas"], "completada"))