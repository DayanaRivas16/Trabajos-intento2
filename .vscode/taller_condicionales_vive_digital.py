
# 1. Verificar si un número es positivo, negativo o cero
numero100 = int(input("Ingrese un número: "))
if numero100 > 0:
    print("El número es positivo.")
elif numero100 < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
# 2. Calcular el mayor de dos números
numero2 = int(input("Ingrese el primer número: "))
numero3 = int(input("Ingrese el segundo número: "))
if numero2 > numero3:
    print("El mayor es:", numero2)
elif numero3 > numero2:
    print("El mayor es:", numero3)
else:
    print("Ambos números son iguales.")
# 3. Determinar si un número es par o impar
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
    
# 4. Verificar si un número está entre 10 y 20 
NUM12 = int(input("Ingrese un número: "))
if NUM12 >= 10:
    if NUM12 <= 20:
        print("El número SI está entre 10 y 20.")
    else:
        print("El número NO está entre 10 y 20.")
else:
    print("El número NO está entre 10 y 20.")
# 5. Encontrar el mayor de tres números 
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a >= b:
    if a >= c:
        print("El mayor es:", a)
    else:
        print("El mayor es:", c)
else:
    if b >= c:
        print("El mayor es:", b)
    else:
        print("El mayor es:", c)
# 6. Calcular precio final con 10% de descuento si el total es mayor a $100
precio = float(input("Ingrese el total de la compra: "))
if precio > 100:
    descuento = precio * 0.10
    precio = precio - descuento
print("El precio final es:", precio)

# 7. Verificar si una persona puede votar
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Puede votar.")
else:
    print("No puede votar.")
# 8. Descuento del 20% para clientes VIP 
precio = float(input("Ingrese el precio del producto: "))
tipo = input("¿Es cliente VIP o normal?: ")
if tipo == "VIP":
    descuento = precio * 0.20
    precio = precio - descuento
else:
    if tipo == "vip":
        descuento = precio * 0.20
        precio = precio - descuento
print("El precio final es:", precio)



