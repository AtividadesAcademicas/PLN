import re

texto = "Adorei o produto! Super recomendo 😍"

def pre_processamento(txt):
    txt.lower()
    texto_limpo = re.sub(r'[^a-zA-Z0-9\s]', '', texto.lower())
    lista_palavras = texto_limpo.split()
    return lista_palavras

print(pre_processamento(texto))