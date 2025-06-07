
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

# 9. Verificar si un numero es multiplo de 3 y de 5
numero400 = int(input("Ingrese un número: "))
if numero400 % 3 == 0:
    if numero400 % 5 == 0:
        print("Es múltiplo de 3 y de 5.")|1111
    else:
        print("No es múltiplo de 3 y de 5.")
else:
    print("No es múltiplo de 3 y de 5.")
 # 10. Verificar si un número es divisible entre dos números dados
numerooo = int(input("Ingrese un número: "))
d1 = int(input("Ingrese el primer divisor: "))
d2 = int(input("Ingrese el segundo divisor: "))
if numerooo % d1 == 0:
    if numerooo % d2 == 0:
        print("Es divisible entre ambos.")
    else:
        print("No es divisible entre ambos.")
else:
    print("No es divisible entre ambos")
    
    
    

# 11. Ingresar 5 números y verificar el tercero
numeros = []

print("Ingresa 5 números:")

numeroo1 = int(input("Número 1: "))
numeros.append(numeroo1)

numeroo2 = int(input("Número 2: "))
numeros.append(numeroo2)

numeroo3 = int(input("Número 3: "))
numeros.append(numeroo3)

numeroo4 = int(input("Número 4: "))
numeros.append(numeroo4)

numeroo5 = int(input("Número 5: "))
numeros.append(numeroo5)


if numeros[2] > 10:
    print("Mayor a 10")
else:
    print("Menor o igual a 10")
    
 # 12. Ver si el número 7 está en la lista

# lista = [3, 5, 7, 9]

# if lista[0] == 7:
#     print("Está en la lista")
# else:
#     if lista[1] == 7:
#         print("Está en la lista")
#     else:
#         if lista[2] == 7:
#             print("Está en la lista")
#         else:
#             if lista[3] == 7:
#                 print("Está en la lista")
#             else:
#                 print("No está en la lista")
# # 13. Sumar los dos primeros elementos de la lista y verificar la suma
# lista = [4, 6, 2, 8]
# suma = lista[0] + lista[1]
# if suma > 10:
#     print("Suma alta")
# else:
#     print("Suma baja")
# # 14. Mostrar el último nombre y verificar si es "Marta"
# nombres = ["Ana", "Luis", "Pedro", "Marta"]
# ultimo = nombres[3]  

# if ultimo == "Marta":
#     print("Nombre correcto")
# else:
#     print("Nombre diferente")
# # 15. Cambiar el segundo color si es "azul"
# colores = ["rojo", "azul", "verde"]
# if colores[1] == "azul":
#     colores[1] = "amarillo"
# print(colores)

# # 16. Comparar primer y último valor de una tupla
# valores = (5, 8, 12, 20)
# if valores[0] < valores[3]:
#     print("Orden ascendente")
# else:
#     print("Orden descendente")
# # 17. Verificar si el segundo valor de la tupla es mayor a 30
# edades = (25, 32, 28)
# if edades[1] > 30:
#     print("Edad mayor a 30")
# else:
#     print("Edad menor o igual a 30")
    
# # 18. Convertir tupla a lista, cambiar valor si es igual a 2, volver a tupla
# tupla = (1, 2, 3)
# lista = list(tupla)

# if lista[1] == 2:
#     lista[1] = 10

# nueva_tupla = tuple(lista)
# print(nueva_tupla)
# # 19. Acceder al segundo valor y verificar si es mayor que 5
# coordenadas = (4, 9)
# if coordenadas[1] > 5:
#     print("Coordenada alta")
# else:
#     print("Coordenada baja")
# # 20. Comparar si dos tuplas son iguales
# tupla1 = (3, 4)
# tupla2 = (3, 5)
# if tupla1 == tupla2:
#     print("Tuplas iguales")
# else:
#     print("Tuplas diferentes")
# # 21. Verificar si la edad es mayor o igual a 18
# persona = {"nombre": "Juan", "edad": 17}
# if persona["edad"] >= 18:
#     print("Adulto")
# else:
#     print("Menor de edad")
# # 22. Cambiar la edad si es mayor a 18
# persona = {"nombre": "Lucía", "edad": 20}
# if persona["edad"] > 18:
#     persona["edad"] = 21
# print(persona)
# # 23. Agregar la clave “ciudad” si no existe, sin usar "not in"
# persona = {"nombre": "Carlos"}

# if "ciudad" in persona:
#     pass  # No hacemos nada si ya existe
# else:
#     persona["ciudad"] = "Bogotá"

# print(persona)
# # 24. Verificar si una clave existe en el diccionario
# producto = {"producto": "pan", "precio": 1200}
# if "precio" in producto:
#     print(producto["precio"])
# else:
#     print("No hay precio")

# # 25. Verificar si "pan" está en el diccionario y mostrar precio
# precios = {"pan": 1200, "leche": 2000}
# if "pan" in precios:
#     print(precios["pan"])
# else:
#     print("Producto no disponible")



