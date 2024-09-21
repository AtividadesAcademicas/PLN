corpus = """rato roeu a roupa do rei de Roma,
O rato roeu a roupa do rei da Rússia,
O rato roeu a roupa do RodovaIho...
O rato a roer roía"""

corpus_limpo = corpus.lower().translate(str.maketrans('.,\n','   '))
print(corpus_limpo)

tokens = corpus_limpo.split(" ")
print(tokens)

tokens_limpo = []

stop_words = ['a', 'o', 'da', 'do', 'e', 'que', 'com', 'se', 'de']

for token in tokens:
    if token != '' and token not in stop_words:
        tokens_limpo.append(token)
print("\nTokens: ",tokens_limpo)

vocabulario = list(set(tokens_limpo))
print("\nVocabulário: ", vocabulario)

bag_of_words = {}

for token in tokens_limpo:
    if token in bag_of_words:
        bag_of_words[token] = bag_of_words[token] + 1
    else:
        bag_of_words[token] = 1
print("\nBag of Words: ", bag_of_words)

from matplotlib import pyplot as plt

lista_palavras = []
lista_ocorrencias = []

for item in bag_of_words.items():
    lista_palavras.append(item[0])

plt.bar(bag_of_words.keys(), bag_of_words.values())
plt.show()

from wordcloud import WordCloud