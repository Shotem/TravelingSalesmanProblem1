import os
from logic import find_solution, calculate_cost
#from TSP import main

if __name__ == "__main__":
    print("Favor de ejecutar el archivo 'main.py'")

# El archivo debe estar guardado al lado de 
def read_from_file():
    filename = input("Ruta relativa del archivo (Ej. '\\tests\\test1.txt') ")
    cities, costs = read_file(filename)
    print_solution( cities, costs, find_solution( costs ) )

# Ejecuta los tests diseñados para probar el algoritmo
def testing_mode():
    num_tests = 4       # Actualizar este número para que se lean todos los archivos de la carpeta tests
    for i in range (1, num_tests + 1):
        print(f"Test #{i}")
        cities, costs = read_file(f"\\tests\\test{i}.txt")
        print_solution( cities, costs, find_solution( costs ) )

# Lee los contenidos del archivo
# La primera linea debe incluir los nombres de N ciudades separadas por ', '
# Las siguientes N lineas deben contener las distancias de cada ciudad a cada otra
# Las distancias deben estar separadas por espacio y deben ser números flotantes
# Las lineas N+2 en adelante no se leen y sirven a modo de comentario
# Un ejemplo de cómo funcionan los comentarios es el archivo test4.txt
#   en la carpeta tests
def read_file(filename):
    try:
        file = open( os.getcwd() + filename )
    except Exception as e:
        print(e)
        return [],[]
    else:
        lines = file.read().split("\n")
        cities = lines[0].split(", ")
        distances = [ ]
        for line in lines[1:len(cities)+1]:
            distances.append( line.split(" ") )
        # Convertir elementos de distances de str a int
        for line in distances:
            for i in range(len(line)):
                line[i] = float(line[i])
        return cities, distances

# Imprime la solución en un formato estándar
def print_solution( cities, costs, nxt ):
    i = 0
    for n in range(len(cities)):
        print( cities[i] + " -(" + str(costs[i][nxt[i]]) + ")-> " , end="" )
        i = nxt[i]
    print( cities[0] )
    print( "El costo es:", calculate_cost(costs=costs, nxt=nxt) )
