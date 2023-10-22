#cree una lista vacia denominada aprendices y edades...
aprendices = []
edades = []

# Llenar las listas solicitando datos por teclado
numAprendices = int(input("Ingrese el número de aprendices: ")) #solicitar al usuario la cantidad de aprendices
for i in range(numAprendices):
    nombre = input(f"Ingrese el nombre del aprendiz {i + 1}: ")#solicitar el nombre del aprendiz
    edad = int(input(f"Ingrese la edad: "))#solicitar la edad del aprendiz
    aprendices.append(nombre) # Agregar el nombre a la lista de aprendices
    edades.append(edad) # Agregar la edad a la lista de aprendices

# Imprimir las listas
print("Lista de Aprendices:") #mostrara un subtitulo
for i in range(len(aprendices)):
    print(f"Nombre: {aprendices[i]}, Edad: {edades[i]} años")
# Iterar a través de la lista de aprendices y edades e imprimir los datos de cada aprendiz

print("----------------------------------------------------------------")

#mostrar el aprendiz con la mayor edad
mayorEdad = edades.index(max(edades)) #utilizo el max para buscar entre las edades el valor mas alto y asi imprimir
print(f"Aprendiz con la mayor edad: {aprendices[mayorEdad]} ({max(edades)} años)")

print("----------------------------------------------------------------")

# Insertar el nombre de la instructora en la posición 1
instructora = input("Ingrese el nombre de la instructora: ")
aprendices.insert(1, instructora) #solicita al usuario el nombre de la instructora se utiliza el insert y el uno lo cual indica que inserte el dato ingresado por el usuario en la posicion 1 y luego va el valor

print("----------------------------------------------------------------")

# Contar cuantos aprendices tienen 18 años
conteo18A = edades.count(18)# Utiliza el count para contar cuantos aprendices tienen una edad de 18 años en la lista
print(f"Número de aprendices con 18 años: {conteo18A}")

print("----------------------------------------------------------------")

# Agregar un aprendiz x al final de la lista
aprendizX = input("Ingrese el nombre del aprendiz X: ")
aprendices.append(aprendizX) #para agregar otro nombre a la lista se utiliza el append

print("----------------------------------------------------------------")

# Borrar el nombre de la instructora de la lista
if instructora in aprendices: #busca el nombre de la instructora
    aprendices.remove(instructora) # y si esta lo elimina, utiliza remove ya que elimina el primer elemento de la lista y esa es la posicion del nombre de la instructora
    
print("----------------------------------------------------------------")

# Indicar un dato a buscar en la lista de aprendices
buscar = input("Ingrese un nombre a buscar en la lista de aprendices: ") #solicita al usuario el nombre a buscar
if buscar in aprendices: #combrueba si el nombre ingresado esta en la lista
    print(f"{buscar} se encuentra en la lista de aprendices.") #si esta imprimira este mensaje
else:
    print(f"{buscar} no se encuentra en la lista de aprendices.") #si no esta imprimira este mensaje
    
print("----------------------------------------------------------------")

# Mostrar los primeros 10 aprendices de la lista
print("Primeros 10 aprendices:") #mostrar este subtitulo
for i in range(10): #itera 10 veces para los primeros 10
    if i < len(aprendices): #comprueba si es valido. len(longitud):se utiliza para asegurar de que solo se itere hasta la cantidad de aprendices que existen en la lista.
        print(aprendices[i]) #imprime los 10 primeros aprendices
        
print("----------------------------------------------------------------")

# Mostrar los 10 ultimos aprendices de la lista
print("Últimos 10 aprendices:") #muestra el subtitulo
for i in range(len(aprendices) - 10, len(aprendices)): #itera desde los ultimos 10 elemntos hasta el final de la lista
    if i >= 0: #comprueba
        print(aprendices[i]) #imprime los ultimos 10 aprendices
        
print("----------------------------------------------------------------")

# Mostrar del elemento 10 al elemento 20
print("Elementos del 10 al 20:") #subtitulo
for i in range(9, 19): #itera desde el elemnto 10 al 20
    if i < len(aprendices):#comprueba
        print(aprendices[i]) #imprime el nombre de cada aprendiz desde el 10 hasta el 20
        
#Maria Jose Perez Salazar
