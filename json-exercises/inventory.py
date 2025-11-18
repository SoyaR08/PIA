import json
import random as rd

def findProductByName(data, productName):
    product = list(filter(lambda x: productName.lower() in x["nombre"].lower() , data))
    return product[0] if len(product) > 0 else -1

def findByCategory(data, category):
    filtered_list = list(filter(lambda x: x["categoria"].lower() == category.lower(), data))
    return filtered_list if len(filtered_list) > 0 else "Categoría inexistente"

def calculateInventoryTotalValue(data):
    return sum(x["precio"] * x["stock"] for x in data)

def updateStock(data, productName):
    product = findProductByName(data, productName)

    if not isinstance(product, int):
        try:
            newStock = int(input("Introduce el nuevo stock del producto: "))
        except Exception:
            while not isinstance(newStock, int):
                newStock = int(input("Eso no es un número. Introduce el nuevo stock del producto: "))
        finally:
            product["stock"] = newStock
            return product
    else:
        return "No se ha podido actualizar el stock"

file = open("jsons/products_inventory.json", "rt")
json_string = file.read()

data = json.loads(json_string)

products_name = ["Ratón Gamer", "Monitor", "Alfombrilla", 
                 "Silla", "Escritorio", "Torre", "Tarjeta Gráfica", "Cascos", 
                 "Flexo", "Posits"]

products_price = [199.99, 49.99, 29.99, 1.99, 19.99]
products_stock = [100, 200, 50, 20, 300]
products_category = ["Electrónica", "Oficina", "Accesorios"]

for i in range(10):
    product = {
        "nombre": rd.choice(products_name),
        "categoria": rd.choice(products_category),
        "precio": rd.choice(products_price),
        "stock": rd.choice(products_stock)
    }

    data["productos"].append(product)

# Filtrar por categoría

category_to_search = input("Inserte nombre de la categoría a buscar: ")

print(findByCategory(data["productos"], category_to_search))
print(f"El valor total del inventario es de: {calculateInventoryTotalValue(data['productos'])}€")
print(updateStock(data["productos"], "laptop"))

