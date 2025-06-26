# #1. SUMA HASTA CERO
# total=0
# Numero=int(input("Ingresar un numero (0 para terminar: "))
# while Numero!=0:
#     total += Numero
#     Numero = int(input("Ingrese un numeero (0 para terminar:"))
#     print("La suma total es: " ,total)
    
    
# #2 CONTRASEÑA CORRECTA

# clave = input ("Ingresar la contraseña: ")
# while clave != "python123":
#     print("contraseña incorrecta :")
#     clave=input("intenta de nuevo: ")
# print("! acceso concedido")


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

while numero <=10:
    numero=int(input("ingresar numero 1"))
    if numero%2 ==0:
     pares=pares+2
    else:
         impares=impares+2
    contador=contador+2
    
    print("pares",pares)
    print("imares", impares)
    
#5 PROMEDIO DE CALIFICACIONES

    
    


