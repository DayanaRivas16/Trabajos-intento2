#Ejercicio 1:crear una tupla
tupla=(1,2,3,4,5)
print("tupla:",tupla)

#Ejercicio 2:acceder a un elemento
print("Segundo valor:" , tupla[1])

#Ejercicio 3:longitud 
print("Longitud de la tupla es:", len(tupla))

#Ejercicio 4:posicion de numero 4 usando index
print("posicion del numero 4: ", tupla.index(4))

#Ejercicio 5:Veces que aparece el numero 2 usando count
print("Las veces que aparece el 2:" , tupla.count(2))

#Ejercicio 6:Tupla con tipos mezclados
tupla_a_mezclada=("hola", 25, 8.75 )
print("tupla mezclada:", tupla_a_mezclada)


#Ejercicio 7:Tuplas anidadas
tupla_anidada=((300,500),"otro", 5)
print("primer valor de la tupla interna:", tupla_anidada [0][0])

print("TALLER DE TUPLAS")
#EJERCICIO1
tupla1=(3,7,11,15,19)
print(tupla1[0], tupla1[-1])

#EJERCICIO 2
lista=[0.5,1.25,2.25,3.5,4.8]
print(lista[1],lista[3])

#EJERCICIO 3
tupla2=(1,2,3)
x,y,z=tupla2
print(x,y,z)

#EJERCICIO 4
lista2=[6,12,18,24,30]
suma=sum(lista2)
print(lista2)

#EJERCICIO 5
tupla3=[1.5,2.5,4.0]
promedio=sum(tupla3)/len(tupla3)
print(promedio)

# EJERCICIO 6
lista6= [10, 20, 30, 40]
a, b, c, d= lista6
print(a, b, c, d)

# EJERCICIO 7
tupla7= (6, 7)
resultado= tupla7[0] * tupla7[1]
print(resultado)

# EJERCICIO 8
lista8= [10, 20, 30]
lista8.append(40)
print(lista8[0], lista8[-1])

# EJERCICIO 9
tupla9= (5, 10, 15, 20)
suma_dos= tupla9[0] + tupla9[1]
print(suma_dos)

# EJERCICIO 10
lista10= [100, 80, 60, 40, 20]
diferencia= lista10[1] - lista10[3]
print(diferencia)

# EJERCICIO 11
tupla11= (2, 4, 6, 8, 10)
producto= tupla11[0] * tupla11[-1]
print(producto)

# EJERCICIO 12
lista12 = [12, 6, 4]
division= lista12[0] / lista12[2]
print(division)

# EJERCICIO 13
tupla13= (1, 2, 3, 4)
print(tupla13[2])

# EJERCICIO 14
lista14= [1.5, 2.5, 3.0, 4.0, 5.5]
total= sum(lista14)
print(total)

# EJERCICIO 15
lista15 = [1, 2, 3, 4]
tupla15 = tuple(lista15)
print(tupla15)

# EJERCICIO 16
tupla16 = (7, 8, 9)
lista16 = list(tupla16)
lista16.append(10)
print(lista16)

# EJERCICIO 17
lista17 = [1, 2, 3, 4, 5]
tupla17 = tuple(lista17)
print(tupla17[2])

# EJERCICIO 18
tupla18 = (5, 10, 15)
lista18 = list(tupla18)
nuevo_numero= int(input("Ingresa un nuevo número: "))
lista18[1]= nuevo_numero
print(lista18)

# EJERCICIO 19
lista19 = [1, 2, 3, 4]
tupla19 = tuple(lista19)
print(len(tupla19))



# EJERCICIO 20
tupla20 = (10, 20, 30, 40, 50)
lista20 = list(tupla20)
lista20 = lista20[:-1]  
print(lista20)


"""numero1=int(input("Ingresa el numero 1"))
numero2=int(input("Ingresa el numero 2"))
numero3=int(input("Ingresa el numero 3"))
numero4=int(input("Ingresa el numero 4"))
numero5=int(input("Ingresa el numero 5"))
numero6=int(input("Ingresa el numero 6"))
numero7=int(input("Ingresa el numero 7"))
numero8=int(input("Ingresa el numero 8"))
numero9=int(input("Ingresa el numero 9"))
numero10=int(input("Ingresa el numero 10"))

#Lista con los numeros
numeros=[numero1,numero2,numero3,numero4,numero5,numero6,numero7,numero8,numero9,numero10]

#TUPLAS
tupla1=(numero1,numero1*2)
tupla2=(numero2,numero2*2)
tupla3=(numero3,numero3*2)
tupla4=(numero4,numero4*2)
tupla5=(numero5,numero5*2)
tupla6=(numero6,numero6*2)
tupla7=(numero7,numero7*2)
tupla8=(numero8,numero8*2)
tupla9=(numero9,numero9*2)
tupla10=(numero10,numero10*2)
Total_de_tuplas=[tupla1+tupla2+tupla3+tupla4+tupla5+tupla6+tupla7+tupla8+tupla9+tupla10]
Suma_de_numero=numero1+numero2+numero3+numero4+numero5+numero6+numero7+numero8+numero9+numero10
Promedio=Suma_de_numero/10
Promedio_mitad=Promedio/2"""



