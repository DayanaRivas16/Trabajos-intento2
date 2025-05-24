print("Taller 1")
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
print("TOTAL A PAGAR:", total_general)

print("Taller 3")