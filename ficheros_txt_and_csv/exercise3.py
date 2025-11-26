import csv
import os

def create_dict(data):

    requested_dict = {"Nombre": [], "Final": [], "Máximo": [], "Mínimo": [], "Volumen": [], "Efectivo": []}

    cleaned_data = data[1:]

    for line in cleaned_data:
        line = line.strip()

        name, final, max, min, volume, efective = line.split(";")

        requested_dict["Nombre"].append(name)
        requested_dict["Final"].append(float(final.replace(",", ".")))
        requested_dict["Máximo"].append(float(max.replace(",", ".")))
        requested_dict["Mínimo"].append(float(min.replace(",", ".")))
        requested_dict["Volumen"].append(int(volume.replace(".", "")))
        requested_dict["Efectivo"].append(float(efective.replace(",", ".").replace(".", "")))

    
    return requested_dict

def write_in_csv(data_dict):
    with open("ficheros_txt_and_csv/stats.csv", "a", encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(data_dict["Nombre"])):
            writer.writerow([
                data_dict["Nombre"][i],
                data_dict["Final"][i],
                data_dict["Máximo"][i],
                data_dict["Mínimo"][i],
                data_dict["Volumen"][i],
                data_dict["Efectivo"][i]
            ])

if not os.path.exists("ficheros_txt_and_csv/stats.csv"):
    with open("ficheros_txt_and_csv/stats.csv", "w", encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre", "Final", "Máximo", "Mínimo", "Volumen", "Efectivo"])

with open("ficheros_txt_and_csv/cotizacion.csv", "r", encoding='utf-8') as csvfile:
    
    data = csvfile.readlines()
    
requested_dict = create_dict(data)

write_in_csv(requested_dict)