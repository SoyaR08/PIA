def validate_seven_numeric_items(data):

    character = ","

    if not character in data:
        print("El separador debe ser una coma")
        return False
    
    splited_data = data.split(character)

    if len(splited_data) != 7:
        print("Debe haber exactamente 7 valores separados por comas")
        return False
    
    for item in splited_data:
        if not item.strip().isdigit():
            print("Los valores deben ser numéricos")
            return False
        
    return True

def validate_x_numeric_items(data, x):

    character = ","

    if not character in data:
        print("El separador debe ser una coma")
        return False
    
    splited_data = data.split(character)

    if len(splited_data) != x:
        print(f"Debe haber exactamente {x} valores separados por comas")
        return False
    
    for item in splited_data:
        if not item.strip().isdigit():
            print("Los valores deben ser numéricos")
            return False
        
    return True

def validate_is_a_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False