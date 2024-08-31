'''
Com base no texto abaixo faça um código para extrair o texto que está entre o primeiro (.) e a primeira (,)
Utilize a função find para localizar as posições do ponto e da virgula no texto e em seguida faça um laço for para gerar um texto novo com os caracteres entre o ponto e a virgula
'''

texto = """
Python é uma linguagem de programação poderosa e versátil.
É amplamente utilizada em desenvolvimento web, ciência de dados, 
inteligência artificial e muito mais.
"""

inicio = texto.find(".")
final = texto.find(",")

texto_extraido = ''

for i in range(inicio + 1, final):
    texto_extraido += texto[i]

print(texto_extraido.strip())


'''
Outra maneira de resolver seria utilizando a funcionalidade slice, que corta a string antes ou depois do indice especificado:

aux = texto[:final]
texto_extraido = aux[inicio:]

print(texto_extraido)
'''