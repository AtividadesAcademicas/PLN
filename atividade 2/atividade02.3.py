import re

comentario_1 = {
    "Autor": "João",
    "Comentario": "Estou tão feliz hoje!",
    "Sentimento": "Positivo"
}
comentario_2 = {
    "Autor": "Maria",
    "Comentario": "Este filme é tão triste.",
    "Sentimento": "Negativo"
}
comentario_3 = {
    "Autor": "Carlos",
    "Comentario": "Que dia chuvoso entediante...",
    "Sentimento": "Positivo"
}
comentario_4 = {
    "Autor": "Ana",
    "Comentario": "Adorei a nova música da banda!",
    "Sentimento": "Negativo"
}
comentario_5 = {
    "Autor": "Roberto",
    "Comentario": "Eureka, consegui resolver este problema",
    "Sentimento": "Positivo"
}

lista_comentarios = [comentario_1, comentario_2, comentario_3, comentario_4, comentario_5]

comentarios_positivos = 0

for i in lista_comentarios:
    if i['Sentimento'] == "Positivo":
        comentarios_positivos += 1

comentarios_negativos = len(lista_comentarios) - comentarios_positivos

print(f"De {len(lista_comentarios)} comentários, {comentarios_positivos} foram positivos e {comentarios_negativos} negativos.")
print(f"As proporções de comentários positivos e negativos é {comentarios_positivos/len(lista_comentarios):.2f}, {comentarios_negativos/len(lista_comentarios):.2f}, respectivamente. Ou seja, 60% dos comentários são positivos e 40% negativos.")

print("\nComentários positivos:")
for i in lista_comentarios:
    if i['Sentimento'] == "Positivo":
        print(i["Comentario"], " - ", i["Autor"])

for i in lista_comentarios:
    if i["Sentimento"] == "Positivo":
        i["Sentimento_Valor"] = 1
    else:
        i["Sentimento_Valor"] = 0

for i in lista_comentarios:
    print(i)