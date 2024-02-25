import subprocess

def porcentaje_espacio(particion):
    resultado = subprocess.run(['df', '-h', particion], capture_output=True, text=True)

    lineas = resultado.stdout.split('\n')
    datos = lineas[1].split()

    porcentaje_ocupado = float(datos[4].strip('%'))
    return porcentaje_ocupado

def main():
    particiones = ['/dev/sda2', '/dev/sda3']
    for particion in particiones:
        porcentaje_ocupado = porcentaje_espacio(particion)
        print(f"{particion} {porcentaje_ocupado:.1f}%")

if __name__ == "__main__":
    main()
