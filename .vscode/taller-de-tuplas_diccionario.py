"""print("Taller 1")
nombre_producto=input("Ingresar el nombre del producto")
precio_unitario=float(input("ingresar el precio"))
cantidad=int(input("Ingrese la cantidad comprada"))
Información=(nombre_producto,precio_unitario)
detalle=[Información,cantidad]
registro={"producto":detalle}
total=precio_unitario*cantidad
print("Resumen de su compra")
print("producto:",nombre_producto)
print("precio unitario:",precio_unitario)
print("cantidad:", cantidad)
print("costo total: ", total)

print("Taller 2")

nombre1 = input("Nombre del producto 1: ")
precio1 = float(input("Precio del producto 1: "))
cantidad1 = int(input("Cantidad del producto 1: "))

nombre2 = input("Nombre del producto 2: ")
precio2 = float(input("Precio del producto 2: "))
cantidad2 = int(input("Cantidad del producto 2: "))

nombre3 = input("Nombre del producto 3: ")
precio3 = float(input("Precio del producto 3: "))
cantidad3 = int(input("Cantidad del producto 3: "))


producto1 = [(nombre1, precio1), cantidad1]
producto2 = [(nombre2, precio2), cantidad2]
producto3 = [(nombre3, precio3), cantidad3]


factura = {
    "producto1": producto1,
    "producto2": producto2,
    "producto3": producto3
}


total1 = precio1 * cantidad1
total2 = precio2 * cantidad2
total3 = precio3 * cantidad3
total_general = total1 + total2 + total3


print("\n--- FACTURA ---")
print(nombre1, "por", cantidad1, "=", total1)
print(nombre2, "por", cantidad2, "=", total2)
print(nombre3, "por", cantidad3, "=", total3)
print("TOTAL A PAGAR:", total_general)"""

print("Taller 3")
# Ingreso del nombre del estudiante
nombre = input("Ingrese el nombre del estudiante: ")

# Materia 1
materia1_nombre = input("Ingrese el nombre de la primera asignatura: ")
nota1_1 = float(input("Ingrese la primera nota de " + materia1_nombre + ": "))
nota1_2 = float(input("Ingrese la segunda nota de " + materia1_nombre + ": "))
promedio1 = (nota1_1 + nota1_2) / 2
materia1 = [(materia1_nombre, promedio1), nota1_1, nota1_2]

# Materia 2
materia2_nombre = input("Ingrese el nombre de la segunda asignatura: ")
nota2_1 = float(input("Ingrese la primera nota de " + materia2_nombre + ": "))
nota2_2 = float(input("Ingrese la segunda nota de " + materia2_nombre + ": "))
promedio2 = (nota2_1 + nota2_2) / 2
materia2 = [(materia2_nombre, promedio2), nota2_1, nota2_2]

# Materia 3
materia3_nombre = input("Ingrese el nombre de la tercera asignatura: ")
nota3_1 = float(input("Ingrese la primera nota de " + materia3_nombre + ": "))
nota3_2 = float(input("Ingrese la segunda nota de " + materia3_nombre + ": "))
promedio3 = (nota3_1 + nota3_2) / 2
materia3 = [(materia3_nombre, promedio3), nota3_1, nota3_2]

# Diccionario del estudiante
estudiante = {
    "nombre": nombre,
    "materias": [materia1, materia2, materia3]
}

# Promedio final
promedio_final = (promedio1 + promedio2 + promedio3) / 3

# Mostrar boletín sin formatear
print("\n--- BOLETÍN DE CALIFICACIONES ---\n")
print("Nombre del estudiante:", estudiante["nombre"])
print()

print("Asignatura:", materia1[0][0])
print("  Nota 1:", materia1[1])
print("  Nota 2:", materia1[2])
print("  Promedio:", materia1[0][1])
print()

print("Asignatura:", materia2[0][0])
print("  Nota 1:", materia2[1])
print("  Nota 2:", materia2[2])
print("  Promedio:", materia2[0][1])
print()

print("Asignatura:", materia3[0][0])
print("  Nota 1:", materia3[1])
print("  Nota 2:", materia3[2])
print("  Promedio:", materia3[0][1])
print()

print("Promedio final del estudiante:", promedio_final)
