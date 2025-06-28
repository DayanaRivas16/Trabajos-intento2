#1. SUMA HASTA CERO
total=0
Numero=int(input("Ingresar un numero (0 para terminar: "))
while Numero!=0:
    total += Numero
    Numero = int(input("Ingrese un numeero (0 para terminar:"))
    print("La suma total es: " ,total)
    
    
#2 CONTRASEÑA CORRECTA

clave = input ("Ingresar la contraseña: ")
while clave != "python123":
    print("contraseña incorrecta :")
    clave=input("intenta de nuevo: ")
print("! acceso concedido")


#3 LISTA DE COMPRAS
Lista=[]
producto = input("Ingresar un producto (Escribir fin para terminar): ")
while producto.lower() != "fin":
    Lista.append(producto)
    producto = input("Ingresar un producto (Escribir fin para terminar): ")
print(f"lista de compra: {Lista} ")

#4 CONTADOR DE PARES E IMPARES
contador=0
pares=0
impares=0

while contador <=10:
    numero=int(input("ingresar numero "))
    if numero%2 ==0:
     pares+=1
    else:
         impares+=1
    contador+=1
    
    print("Cantidad de pares",pares)
    print("Cantidad de imares", impares"
    
#5 PROMEDIO DE CALIFICACIONES
notas=[]
entrada=input("Ingresa una nota (o escribe Salir para terminar)")
while entrada !="Salir":
    nota=float(entrada)
    if 0 <= nota <=5:
        notas.append(nota)
    else:
        print("Nota esta fuera del rango tiene que estar adentro de 0 y 5")
    entrada=input("ingresar otra nota (o ponga Salir)")
       
if len (notas)>0:
    promedio=sum(notas) / len (notas)
    print("El promedio de las notas: ",promedio)
else:
    print("No se ingresaron ninguna nota valida")
    
#6TABLAS DE MULTIPLICAR
numerito=int(input("Ingresa un numero para multiplicar"))
contador=1
while contador <=10:
    resultado=numerito*contador
    print(numerito, "x", contador, "=", resultado)
    contador += 1     

#7ADIVINA EL NUMERO
numero_secreto = 17
intento = int(input("Adivina el número: "))

while intento != numero_secreto:
    if intento < numero_secreto:
        print("Es mayor.")
    else:
        print("Es menor.")
    intento = int(input("Intenta otra vez: "))

print("¡Correcto! Adivinaste el número.")

#8TUPLA DE FRUTAS
frutas = ("manzana", "pera", "mango", "uva", "banana")
adivinanza = input("Adivina una fruta: ").lower()

while adivinanza not in frutas:
    adivinanza = input("Incorrecto. Intenta otra fruta: ").lower()

print("¡Acertaste! Esa fruta está en la lista.")

#9DICCIONARIO DE TRADUCCIÓN
diccionario = {
    "hola": "hello",
    "gracias": "thank you",
    "perro": "dog",
    "gato": "cat",
    "casa": "house"
}

palabra = input("Escribe una palabra en español: ").lower()

while palabra != "salir":
    if palabra in diccionario:
        print("Traducción:", diccionario[palabra])
    else:
        print("Esa palabra no está en el diccionario.")
    palabra = input("Escribe otra palabra (o 'salir' para terminar): ").lower()
    
    #10 CALCULADORA BASICA
    while True:
    print ("\nMenú:")
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Hasta luego.")
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", num1 + num2)
    elif opcion == "2":
        print("Resultado:", num1 - num2)
    elif opcion == "3":
        print("Resultado:", num1 * num2)
    elif opcion == "4":
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("No se puede dividir por cero.")
    else:
        print("Opción no válida.")
        
        
#11REGISTRO DE EDADES
personas = {}

while True:
    nombre = input("Escribe el nombre (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    personas[nombre] = edad

print("Diccionario completo:", personas)

#12 BUSCAR EN LISTA
colores = ["rojo", "azul", "verde", "amarillo", "negro"]
intento = input("Escribe un color: ").lower()

while intento not in colores:
    intento = input("No está. Intenta con otro color: ").lower()

print("¡Correcto! Ese color está en la lista.")

#13 POTENCIAS DE UN NUMERO
numero = int(input("Escribe un número: "))
potencia = 1

while potencia <= 5:
    print(f"{numero}^{potencia} = {numero ** potencia}")
    potencia += 1
    
#14 LISTA DE CUADROS
cuadrados = []
contador = 0

while contador < 5:
    num = int(input(f"Escribe el número {contador + 1}: "))
    cuadrados.append(num ** 2)
    contador += 1

print("Lista de cuadrados:", cuadrados)

#15 DICCIONARIO DE ESTUDIANTES
estudiantes = {}

while True:
    nombre = input("Nombre del estudiante (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    nota = float(input(f"Nota final de {nombre}: "))
    estudiantes[nombre] = nota

print("Estudiantes registrados:", estudiantes)
             

        
            



    
    


