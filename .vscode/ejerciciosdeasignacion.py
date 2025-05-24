'''D="ASIGNACIÓN"

rojo,verde,azul=3,8,0
print(rojo)
print(verde)
print(azul)
x,y,z=1,4,8
print(x)
print(y)
print(z)

x=y=z=0
print(x,y,z)

x=10
x=x+5
print(x)

n=10
n+=5
print(n)

op="Hola Mundo"
op+=" Que"
op+=" Tal"
print(op)

Lery="Rivas"
Lery+=" Contestee"
Lery+=" tengase"
print(Lery)

op="Hola "
op+="Mundo "
print(op)
op*=2
print(op)

D="CONCATENACIÓN"
texto1="Hola"
texto2=" Mundo"
resultado=texto1+""+texto2
print(resultado)

D="BUSQUEDA"
Mensaje="Hola Mundoo"
buscar=Mensaje.find("Hola")
print(buscar)

mensaje="Yo tengo cinco helados"
buscar=mensaje.find("cinco")
print(buscar)

D="EXTRACCIÓN"
saludo="hola mundo"
extracción=saludo[0:5]
print(extracción)
mensaje="Yo quiero tener mucha plata"
buscar=mensaje.find("u")
extraer=mensaje [4:5]
print(buscar)
print(extraer)

var1=5
var2=55
print(var1==var2)


d="EJERCICIO CON CONCATENACIÓN"
Frase="El conocimiento es poder"
print(Frase.find("conocimiento"))
print(Frase.find("poder"))

Frase="La práctica hace al maestro"
print(Frase.find("práctica"))
print(Frase.find("maestro"))

D="ejercicio de CONCATENACION Y INTERACCION"

frase=input("Ingresa una frase ")
palabra=input("ingresa una palabra")
print(frase.find(palabra))'''



texto="Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges"

print(texto.find("Sabia"))
print(texto.find("Caminaba"))
print(texto.find("falanges"))
print(texto[459:655])

texto:"El oeste de Texas divide la frontera entre Mexico y Nuevo México. Es muy bella pero aspera, llena de cactus, en esta region se encuentran las Davis Mountains. Todo el terreno esta lleno de piedra caliza, torcidos arboles de mezquite y espinosos nopales. Para admirar la verdadera belleza desertica, visite el Parque Nacional de Big Bend, cerca de Brownsville. Es el lugar favorito para los excurcionistas, acampadores y entusiastas de las rocas. Pequeños pueblos y ranchos se encuentran a lo largo de las planicies y cañones de esta region. El area solo tiene dos estaciones, tibia y realmente caliente. La mejor epoca para visitarla es de Diciembre a Marzo cuando los dias son tibios, las noches son frescas y florecen las plantas del desierto con la humedad en el aire."


print(texto.find("florecen"))
print(texto.find("nopales"))
print(texto.find("Davis"))

print(texto.find("Sabia"))
print(texto.find("Caminaba"))
print(texto.find("falanges"))
print(texto[459:655])

nombre=input("Ingrese el nombre del estudiante")
nota1=float(input("ingrese la nota 1(20%)"))
nota2=float(input("ingrese la nota 2(30%)"))
nota3=float(input("ingrese la nota 2(50%)"))
notafinal=(nota1*0.2)+(nota2*0.3)+(nota3*0.5)   
notafinal2=nota1*nota2*nota3
print("La nota final es", notafinal )
