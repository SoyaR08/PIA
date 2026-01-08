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