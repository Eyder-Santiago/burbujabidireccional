from random import randint
from time import time

lista = []

for i in range(0,100000):
    lista.append(randint(0, 9))

print(lista)

temp=0
tiempo_inicial=time()

for j in range(1, len(lista)):
    for i in range(0, len(lista)-j):
        if lista[i]>lista[i+1]:
            temp = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = temp
    
    for k in range(len(lista)-j,j,-1):
        if lista[k]<lista[k-1]:
            temp = lista[k]
            lista[k] = lista[k-1]
            lista[k+1] = temp

tiempo_final = time()

print(lista)
print("tiempo de ejecución " + str(tiempo_final-tiempo_inicial))




