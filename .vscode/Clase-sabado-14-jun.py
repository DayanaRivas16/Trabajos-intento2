
print ("EJEMPLO DE While")
contador=1
while contador <= 100:
    print("Contador:",  contador)
    contador += 1
    
print("------------------------------------")




#while true: codigo que se repite para siempre
while True:

texto=input("Escribe algo (o escribe 'salir' para terminar): ")

if texto == "salir":
    break

print("Escribiste:", texto)

#break= break detiene inmediatamente un ciclo (while o for), 
# aunque la condición del ciclo siga siendo verdadera