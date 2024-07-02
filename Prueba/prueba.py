ede = 3
import json
import os
archivo_datos = "registros_estudiantes.json"
def slash():
    datos = {}
    if os.path.exists(archivo_datos):
        with open(archivo_datos, 'r') as f:
            datos = json.load(f)
    return datos
def recibir(datos):
    with open(archivo_datos, 'w') as f:
        json.dump(datos, f, indent=4)
def malenia():
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    nota1 = float(input("Ingrese la nota de Matemáticas del estudiante: "))
    nota2 = float(input("Ingrese la nota de Ciencias del estudiante: "))
    nota3 = float(input("Ingrese la nota de Historia del estudiante: "))
    promedio = (nota1 + nota2 + nota3) / 3
    estudiante = {
        'nombre': nombre,
        'apellido': apellido,
        'matematicas': nota1,
        'ciencias': nota2,
        'historia': nota3,
        'promedio': promedio
    }
    datos = slash()
    datos[nombre.lower()] = estudiante
    recibir(datos)
    print(f"\nEstudiante {nombre} {apellido} registrado correctamente.\n")
def miquella():
    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ").lower()
    datos = slash()
    if nombre_buscar in datos:
        estudiante = datos[nombre_buscar]
        print("\nInformación del estudiante encontrado:")
        print(f"Nombre: {estudiante['nombre']} {estudiante['apellido']}")
        print(f"Notas: Matemáticas: {estudiante['matematicas']}, Ciencias: {estudiante['ciencias']}, Historia: {estudiante['historia']}")
        print(f"Promedio: {estudiante['promedio']}\n")
    else:
        print(f"No se encontró ningún estudiante con el nombre '{nombre_buscar}'.\n")
def messmer():
    datos = slash()
    if datos:
        print("\nLista de estudiantes registrados:")
        for estudiante in datos.values():
            print(f"Nombre: {estudiante['nombre']} {estudiante['apellido']}, Promedio: {estudiante['promedio']}")
        print()
    else:
        print("\nNo hay estudiantes registrados.\n")
while ede >= 0:
    print ("Registro de notas escolares.")
    print ("----------------------------")
    print ("Menu de opciones.")
    print (" .1|Registrar estudiante|")
    print (" .2|Buscar estudiante por nombre|")
    print (" .3|Mostrar lista de estudiante|")
    print (" .4|Salir de la aplicacion|")
    print ("----------------------------")
    dedos = input("¿Que opcion desea realizar?(1,2,3,4): ")
    if dedos == '1':
        malenia()
    if dedos == '2':
        miquella()
    if dedos == '3':
        messmer()
    if dedos == '4':
        print ("Gracias por utilizar el programa. Hasta luego.")
        break