import os

for i in range(1, 6):
    folder_name = f"folder{i}"
    os.makedirs(folder_name, exist_ok=True)

    for j in range(1, 11):
        file_name = f"{folder_name}/fichero{j}.txt"
        with open(file_name, 'w') as file:
            file.write(f"Este es el contenido del fichero {j}")