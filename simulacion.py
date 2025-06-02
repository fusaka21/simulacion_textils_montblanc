import os

# Colores para terminal
class Colores:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_titulo():
    print(Colores.OKCYAN + Colores.BOLD)
    print("=" * 40)
    print("      ALMACENES TEXTIL MONTBLANC")
    print("=" * 40 + Colores.ENDC)

def mostrar_recuento(base_de_datos):
    print(Colores.OKGREEN + "\n--- RECUENTO DE OBJETOS ---" + Colores.ENDC)
    if not base_de_datos:
        print("No se ha ingresado ningún objeto.")
    else:
        for objeto, cantidad in base_de_datos.items():
            print(f"{Colores.BOLD}{objeto}{Colores.ENDC}: {cantidad}")
    print()

def main():
    base_de_datos = {}

    while True:
        limpiar_pantalla()
        mostrar_titulo()
        print("Introduce objetos uno por uno.")
        print("Presiona ENTER vacío para ver el recuento y salir.\n")

        entrada = input(Colores.OKBLUE + "➤ Objeto: " + Colores.ENDC).strip()

        if entrada == "":
            limpiar_pantalla()
            mostrar_titulo()
            mostrar_recuento(base_de_datos)
            break

        base_de_datos[entrada] = base_de_datos.get(entrada, 0) + 1

    input(Colores.WARNING + "\nPresiona ENTER para finalizar..." + Colores.ENDC)

if __name__ == "__main__":
    main()
