from os import system
from datetime import timedelta, date

#Estructuras a utilizar
num_reserva = 3
cabanias = [{"num":"1", "costo_diario":100}, {"num":"2", "costo_diario":50}, {"num":"3", "costo_diario":70}, {"num":"4", "costo_diario":80}, {"num":"5", "costo_diario":150}]
reservas = [{"num_reserva": 1, "cabania": cabanias[0], "checkin": date(2020, 7, 30), "checkout": date(2020,8,10)},
{"num_reserva": 2, "cabania": cabanias[1], "checkin": date(2020, 8, 2), "checkout": date(2020,8,5)},
{"num_reserva": 3, "cabania": cabanias[2], "checkin": date(2020, 8, 10), "checkout": date(2020,8,20)}]


def mostrar_menu():
    system("cls") 
    print("Menú")
    print("1 - Registrar Cabaña")
    print("2 - Alquiler de cabaña")
    print("3 - Facturación en una fecha dada")
    print("4 - Mostrar cabañas")
    print("0 - Salir")

def mostrar_cabanias():
    system("cls") 
    print("Listado de Cabañas")
    for cabania in cabanias:
        print("Cabaña ",cabania["num"], " - ", "Costo diario USD: ", cabania["costo_diario"])

def buscar_cabania(num_cabania):
    buscado = None
    indice = 0
    while indice<len(cabanias) and buscado == None:
        cab = cabanias[indice]
        if cab["num"] == num_cabania:
            buscado = cab
        indice +=1
    
    return buscado


def registrar_cabania():
    system("cls")
    num_cabania = input("Ingrese número de cabania: ")
    cabania = buscar_cabania(num_cabania)
    if cabania != None:
        print("El número de cabaña ingresado ya existe.")

    else:
        costo_diario = int(input("Ingrese costo diario en USD: "))
        cab = {"num": num_cabania, "costo_diario": costo_diario}
        cabanias.append(cab)
        print("La cabaña se registró correctamente")

def solicitar_fecha():
    dia = int(input("Ingrese día: "))
    mes = int(input("Ingrese mes: "))
    anio = int(input("Ingrese año: "))

    return date(anio,mes,dia)


def disponibilidad(checkin, checkout):
    cabanias_libres = cabanias.copy()
    for r in reservas:
        if (checkin <= r["checkin"] <= checkout) or (checkin <= r["checkout"] <= checkout) or (r["checkin"]<=checkin<=checkout<=r["checkout"]):
            if r["cabania"] in cabanias_libres:    #Puede haber dos reservas para una misma habitación en el período
                cabanias_libres.remove(r["cabania"])
    
    return cabanias_libres


def alquilar_cabania():
    system("cls")
    global num_reserva
    checkin = solicitar_fecha()
    checkout = solicitar_fecha()
    cabanias_libres = disponibilidad (checkin,checkout)

    print("Cabañas libres")
    print(cabanias_libres)
    
    num_cabania = input("Ingrese número de cabaña: ")
    cab = buscar_cabania(num_cabania)
    
    if cab != None:

        if cab in cabanias_libres:
            num_reserva += 1
            reserva = {"num_reserva": num_reserva, "cabania": cab, "checkin": checkin, "checkout": checkout}
            reservas.append(reserva)
            print("La cabaña se reservó correctamente")
        else:
            print("Ya existen reservas en esa fecha.  Seleccione otra fecha o elija otra cabaña")
            input("")
            alquilar_cabania()
    else:
        print("El número de cabaña ingresado no existe")


def ver_facturacion():
    system("cls")
    fecha = solicitar_fecha()
    monto_total = 0
    for r in reservas:
        if r["checkin"] <= fecha <= r["checkout"]:
            monto_total += r["cabania"]["costo_diario"]

    print("El monto facturado en el día es de: ", monto_total)


#INICIO DEL PROGRAMA
mostrar_menu()
print()

opcion = input("Ingrese una opción: ")
while opcion !="0":
    if opcion == "1":
        registrar_cabania()
    if opcion =="2":
        alquilar_cabania()     
    if opcion == "3":
        ver_facturacion()
    if opcion == "4":
        mostrar_cabanias()
    
    print()
    input("Ingrese enter para volver al menú")
    mostrar_menu()
    print()
    opcion = input("Ingrese una opción: ")