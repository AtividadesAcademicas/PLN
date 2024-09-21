import numpy as np

floats = np.random.random((300, 200, 3))
print(floats)
print(floats.shape)

notas = np.random.randint(1, 11, (20, 3))
print(notas)

array1 = np.arange(1, 13, 1)
print(array1.shape, ": ", array1)
matriz1 = array1.reshape(3, 4)
print(matriz1.shape, ": ", matriz1)
matriz2 = matriz1.transpose()
print(matriz2.shape, ": ", matriz2)

array1 = array2 = np.arange(1, 11, 1)
print("array 1: ", array1,"\narray 2: ", array2)
print("Soma dos arrays: ", array1 + array2)
print("Subtração dos arrays: ", array1 - array2)
print("Multiplicação dos arrays: ", array1 * array2)
print("Divisão dos arrays: ", array1 / array2)

array1 = np.arange(1, 21, 1)
print(array1)
# indexação
array_pares = array1[array1 %2 == 0]
print("Pares: ", array_pares)
# fatiamento
del array_pares
array_pares = array1[1::2]
print("Pares: ", array_pares)

array1 = np.random.randint(1,101,(50))
print("array:", array1)
array50 = array1[array1 > 50]
print("Maiores que 50:", array50)

array1 = np.random.randint(1,101,(10))
print("array: ", array1)
print("Média: ", array1.mean())
print("Mediana: ", np.median(array1))
print("Desvio padrão: ", array1.std())