"""#EJEMPLO DE
print("SISTEMA DE EVALUACIÓN")
print("si tu nota es 2.9 o menos pierdes la materia y si es 3.0 o mas ganas la materia")
nombre=input("ingresar el nombre del estudiante: ")
nota=input("escribe el grado: ")

materia1="Matematicas"
materia2="Castellano"
materia3="Ingles"
materia4="Artistica"
materia5="Edu.Fisica"

print("ingrese 3 notas de",materia1)
mate1=float(input("nota1: "))
mate2=float(input("nota2: "))
mate3=float(input("nota3: "))
suma1=mate1+mate2+mate3
promedio1=suma1/3
print("suma de las notas",suma1)
print("promedio de" , materia1,"es:" , promedio1)
print(materia1,":", promedio1)


print("ingrese 3 notas de",materia2)
matee1=float(input("nota1: "))
matee2=float(input("nota2: "))
matee3=float(input("nota3: "))
suma2=matee1+matee2+matee3
promedio2=suma2/3
print("suma de las notas",suma2)
print("promedio de" , materia2,"es: ", promedio2)


print("ingrese 3 notas de",materia3)
mateee1=float(input("nota1: "))
mateee2=float(input("nota2: "))
mateee3=float(input("nota3: "))
suma3=mateee1+mateee2+mateee3
promedio3=suma3/3
print("suma de las notas",suma3)
print("promedio de", materia3, "es: ", promedio3)

print("ingrese 3 notas de",materia4)
mateeee1=float(input("nota1: "))
mateeee2=float(input("nota2: "))
mateeee3=float(input("nota3: "))
suma4=mateeee1+mateeee2+mateeee3
promedio4=suma3/3
print("suma de las notas",suma4)
print("promedio de", materia4, "es: ", promedio4)


print("ingrese 3 notas de",materia5)
mateeeee1=float(input("nota1: "))
mateeeee2=float(input("nota2: "))
mateeeee3=float(input("nota3: "))
suma5=mateeee1+mateeee2+mateeee3
promedio5=suma3/3
print("suma de las notas",suma5)
print("promedio de", materia5, "es: ", promedio5)

print("NOTAS FINALES")
print(materia1,":", promedio1)
print(materia2,":", promedio2)
print(materia3,":", promedio3)
print(materia4,":", promedio4)
print(materia5,":", promedio5)

total_promedio=promedio1+promedio2+promedio3+promedio4+promedio5
promedio_final=total_promedio/5

#EJEMPLO DE .append

print("EJERCICIO1:productos en una bolsa")

productos=[]
produ1=input("ingresa el producto1: ")
productos.append(produ1)

produ2=input("ingresa el producto2: ")
productos.append(produ2)

produ3=input("ingresa el producto1: ")
productos.append(produ3)

print("lista de productos:" ,productos)

print("EJERCICIO2:precio de 3 articulos")
 
precios=[]
precio1=float(input("precio de articulo 1: "))
precios.append(precio1)

precio2=float(input("precio de articulo 2: "))
precios.append(precio2)

precio3=float(input("precio de articulo 3: "))
precios.append(precio3)
total=sum(precios)
print("suma total de los precios: ",total)

print("EJERCICIO3:numeros ingresados por el usuario")

numeros=[]
numero1=int(input("ingresa el primer numero: "))
numeros.append(numero1)

numero2=int(input("ingresa el segundo numero: "))
numeros.append(numero2)

numero3=int(input("ingresa el tercer numero: "))
numeros.append(numero3)

numero4=int(input("ingresa el primer numero: "))
numeros.append(numero4)

print("el numero mayor es:" , max(numeros))
print("el numero menor es:", min(numeros))"""

"""print("EJEPLO DE INSERT")
lista=[1,2,4]
lista.insert(2,3)
print(lista)"""

"""print("EJEMPLO DE REMOVE")
frutas=['banana', 'banana', 'naranja', 'banana']
frutas.remove('banana')
print(frutas)

print("EJEMPLO DE MAX")
print("letras")
letras=['ana','carlos','beatriz']
print(max(letras))

print("EJEMPLO DE MIN")"
numeros=[5,2,8,1,9]
minimo=min(numeros)
print("el valor minimo es:",minimo)

print("EJEMPLO DE.INDEX")
nombres=['Ana','Luis','Carlos','Luis']
print(nombres.index('Luis'))

print("EJEMPLO DE remove")
numeros=[1,2,3,2]
numeros[3]-4
numeros.remove(4)
print(numeros)

#OTRA FORMA
numeros=[1,2,3,2]
numeros.reverse()
numeros.remove(2)
numeros.reverse()
print(numeros)"""

print("EJEMPLO DE TUPLAS")
mi_tupla=(1,2,3,4,)
otra_tupla=("Hola","Como","estas","?")
"""clientes=["pedro","ana","carlos","isabela","carlos","ana","carlos,sofia,Lery,isabela,lery"]

clientes[0]=clientes[0].upper()
clientes[1]=clientes[1].upper()
clientes[2]=clientes[2].upper()
clientes[3]=clientes[3].upper()
clientes[4]=clientes[0].upper()
clientes[5]=clientes[1].upper()"""





