import re

texto = "Vc eh mt bom, recomendo mto!!!"

dicionario = {
    "vc":"você",
    "eh":"é",
    "mt":"muito",
    "mto":"muito"
}

def normaliza(txt):
    for abreviacao in dicionario:
        txt = re.sub(r'\b' + re.escape(abreviacao) + r'\b', dicionario[abreviacao], txt)
    return txt

print(normaliza(texto))