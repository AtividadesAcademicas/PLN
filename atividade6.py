import numpy as np

dados_meteorologicos = [25, 26, 27, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12]

print("Temperatura média: ", np.mean(dados_meteorologicos), "°C")
print("Temperatura máxima: ", np.max(dados_meteorologicos), "°C")
print("Temperatura mínima: ", np.min(dados_meteorologicos), "°C")
print("Desvio padrão da temperatura: ", round(np.std(dados_meteorologicos), 1) , "°C")