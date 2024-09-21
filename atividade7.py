import numpy as np

altura = np.array([1.65, 1.75, 1.80, 1.70, 1.68, 1.72, 1.78, 1.60, 1.85, 1.73, 1.69, 1.75, 1.62, 1.80, 1.77, 1.68, 1.79, 1.81, 1.76, 1.74])
peso = np.array([65, 70, 75, 80, 60, 68, 72, 58, 90, 72, 65, 70, 55, 78, 79, 62, 85, 88, 70, 75])

imc = np.zeros(20)

for x in range(len(altura)):
    a = altura[x]
    p = peso[x]
    i = round((p / (a**2)), 2)
    imc[x] = i

print(imc)

abaixo = np.sum(imc < 18.5)
normal = np.sum((imc >= 18.5) & (imc < 24.9))
sobrepeso = np.sum((imc >= 25) & (imc < 29.9))
obesidade = np.sum(imc >= 30)

print("Abaixo do peso: ", abaixo)
print("Peso normal: ", normal)
print("Sobrepeso: ", sobrepeso)
print("Obesidade: ", obesidade)