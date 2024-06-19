registro_pedidos = []
sectores = ["Centro", "Colina", "Industrias"]

def registar_pedidos():
    nombre_apellido = input("Ingrese nombre: ")
    direccion = input("Ingrese dirección: ")
    sector = input("Ingrese sector: ").lower()
    try:
        cil_5kg = int(input("Cil 5kg ¿Cuanta cantidad desea ?: "))
        cil_15kg = int(input("Cil 15kg ¿Cuanta cantidad desea?: "))
        cil_45kg = int(input("Cil 45kg ¿Cuanta cantidad desea?: "))
    except:
        print("Debe ingresar un cantidad (Número)")



    cliente = {
    "nombre y apellido" : nombre_apellido,
    "direccion" : direccion,
    "sector" : sector,
    "Cil. 5kg" : cil_5kg,
    "Cil. 15kg" : cil_15kg,
    "cil. 45kg" : cil_45kg
    }

    registro_pedidos.append(cliente)


def listar_pedidos():
    print("Lista de pedidos")
    for cliente in registro_pedidos:
        print(cliente)




def imprimir_hoja_de_ruta():
    print("imprimir")
    sector = input("Ingrese el sector para imprimir ruta: ").lower()
    while sector in sectores:
        with open("HOJA_RUTA.txt", "w") as archivo:
            for cliente in registro_pedidos:
                archivo.write(f"nombre y apellido: {cliente["nombre y apellido"]}\n")
                archivo.write(f"dirección: {cliente["direccion"]}\n")
                archivo.write(f"sector: {cliente["sector"]}\n")
                archivo.write(f"Cil. 5kg: {cliente["Cil. 5kg"]}\n")
                archivo.write(f"Cil. 15kg: {cliente["Cil. 15kg"]}\n")
                archivo.write(f"Cil. 45kg: {cliente["Cil. 45kg"]}\n")
                break
    else:
        print("No existe ese sector")




