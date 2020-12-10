from math import inf
from copy import copy, deepcopy
from random import randrange
#from TSP import main

if __name__ == "__main__":
    print("Favor de ejecutar el archivo 'main.py'")
    #costs = [[0, 2, 1, 5], [2, 0, 6, 1], [1, 6, 0, 5], [5, 1, 5, 0]]
    #solution = [ 2, 0, 3, 1 ]
    #genetic(costs, solution)
    #nxt = [0, 3, 2, 1]
    #print( calculate_cost( costs, nxt ) )

# Calcular el costo de la solución actual
def calculate_cost( costs, nxt ):
    i = 0
    cost = 0
    while nxt[i] != 0:
        added = costs[i][nxt[i]]
        cost += added
        i = nxt[i]
    cost += costs[i][0]
    return cost

# Envía a llamar los algoritmos "Nearest Neighbor" y "genetic"
def find_solution( costs ):
    solution = nearest_neighbor( deepcopy(costs) )
    solution = genetic(costs, solution)
    return solution

# Encontrar solución usando "Nearest Neighbor" (no muestral)
def nearest_neighbor( data ):
    i = 0
    arr = [ None ] * len(data)
    for n in range( len(data)-1 ):
        for j in range(len(data)):
            data[j][i] = inf
        
        least, index = data[i][0], 0
        for j in range(len(data)):
            if data[i][j] < least:
                least, index = data[i][j], j
        arr[i] = i = index

    arr[i] = 0
    return arr

# Refinar solución usando algoritmo genético
def genetic(costs, solution):
    for i in range(50):
        other_sol = copy(solution)

        index1 = randrange(0, len(other_sol), 1)
        while solution[index1] == 0:
            index1 = randrange(0, len(other_sol), 1)
        
        index2 = randrange(0, len(other_sol), 1)
        while solution[index2] == 0 or index1==index2:
            index2 = randrange(0, len(other_sol), 1)
        
        # Solo funciona si el primero va antes en la lista que el segundo
        if other_sol.index(index1) > other_sol.index(index2):
            index1, index2 = index2, index1

        # Cambiar a las posiciones correspondientes
        prev_index2 = other_sol.index(index2)
        other_sol[prev_index2] = other_sol[index2]
        other_sol[index2] = other_sol[index1]
        other_sol[index1] = index2

        cost1 = calculate_cost(costs, solution)
        cost2 = calculate_cost(costs, other_sol)
        ### DEBUG
        #print("Solution", solution)
        #print("Other solution", other_sol)
        #print(f"Index 1: {index1}\tIndex 2: {index2}")
        #print(f"Cost 1: {cost1}\tCost 2: {cost2}")
        if cost2 < cost1:
            solution = other_sol

    print(min(cost1, cost2))

    return solution





    