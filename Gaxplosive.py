import funcion as fn

clientes = []

while True:
    print("Gaxplosive")
    print("1. Registrar pedido")
    print("2.Listar todos los pedidos")
    print("3. imprimir hoja de ruta")
    print("4. Salir del programa")
    try:
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
                    fn.registar_pedidos()
        elif opcion == 2:
                    fn.listar_pedidos()
        elif opcion == 3:
                    fn.imprimir_hoja_de_ruta()
        elif opcion == 4:
                print("Saliendo...")
                break

        else:
            print("Opción invalida. Porfavor ingrese opción del 1 al 5")
    except:
        print("Opción no valida")
