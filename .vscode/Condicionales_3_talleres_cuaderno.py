#SENTENCIAS
#EJEMPLO UNO
A=2+3
if A==4:
    print("A es igual a cuatro")
elif A==5:
    print("A es igual a cinco")
elif A==6:
    print("A es igual a seis")
else:
    print("no se cumplio con la condicion")
    

#CREDITO BANCARIO
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")


if edad >= 18:
    print("Credito aprobado: el cliente es mayor de edad.")
else:
    print("Credito rechazado: el cliente no es menor de edad.")
    
#ENTRADAS
edad = int(input("Ingrese la edad del cliente: "))
print("Edad ingresada:", edad)


if edad < 4:
    precio = 0
    print("Precio asignado:", precio)
    print("Entrada gratuita.")
elif edad <= 18:
    precio = 5
    print("Precio asignado:", precio)
    print("El precio de la entrada es de 5 euros.")
else:
    precio = 18
    print("Precio asignado:", precio)
    print("El precio de la entrada es de 18 euros.")
    
#CALCULADORA
print("Ingrese 's' para suma, 'r' para resta, 'm' para multiplicación, 'd' para división")

operacion = input("Seleccione la operación: ")

if operacion == 's':
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operacion == 'r':
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print("Resultado:", resultado)

elif operacion == 'm':
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operacion == 'd':
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = num1 / num2
        print("Resultado:", resultado)

else:
    print("Operación no válida")
    
    