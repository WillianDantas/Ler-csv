# -*- coding: utf-8 -*-
from Util import formattString
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np


cr = open("Arquivo\dados_5asec.csv", 'rb');
crlf = "\\r\\n";
vaLinhas = [];
conteudo = "";

for row in cr:
   if(str(row).find(crlf) != -1):
      valinha = str(row.decode('latin-1'));
      texto = valinha.split(';');
      if len(texto) >= 3:
        if texto[2].find("texto"):
            if formattString.remover_acentos(texto[0]) in ["5asec Jardim Marajoara"]:
                conteudo = conteudo + texto[2];

resultado  = ' '.join(char for char in conteudo.split() if char not in ['Q2', 'Q4', ':', '|']);
resultado = formattString.strFormatt(resultado.lower());


palavras = [];
contagem = [];

for ocorrencia in resultado.split():
    if palavras.count(ocorrencia) == 0:
        palavras.append(ocorrencia);
        contagem.append(resultado.count(ocorrencia));

print(palavras[:30]);
print(contagem[:30]);


palavras = palavras[:30];
contagem = contagem[:30];
"""

y_pos = np.arange(len(palavras))
plt.figure(1, figsize=(12, 12))
plt.bar(y_pos, contagem, align='center')
plt.xticks(y_pos, palavras, fontsize=10, rotation=65)
plt.ylabel('Usage', fontsize=5)
plt.xlabel('No of Movies', fontsize=5)
plt.title('Programming language usage')

plt.show()

"""


stopwords = set(STOPWORDS)
stopwords.update(['presidente', 'kkk', 'voce', 'nao', 'brasileiro','jair', 'bolsonaro'])


wordcloud = WordCloud(
    max_font_size=40,
    max_words=200,
    background_color="white",
    scale=3,
    random_state=1,
    stopwords=stopwords
).generate(resultado)



plt.figure(1, figsize=(12, 12))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()





