#importando bibliotecas:
#import "nome da biblioteca"
#ou
#from "nome biblioteca" import "funcao especifica"
import matplotlib.pyplot as plt 
"""


dados_x = ["Personagem 1", "Personagem 2", "Personagem 3"]

dados_y = [1000, 1500, 20_000]



plt.title("Titulo do Gráfico")

plt.xlabel("Dados X")

plt.ylabel("Dados Y")

plt.bar(dados_x, dados_y)# bar = tipo do gráfico (gráfico de barras)

plt.show()


linguagens =["python","java","c++","javaScript"]
alunos = [15,10,12,8]

plt.bar(linguagens, alunos)

plt.title("Alunos por Linguagem")
plt.xlabel("Linguagem")
plt.ylabel("Quantidade de alunos")

plt.show()


import qrcode

texto = "Estou ensinando python para a melhor turma :D"

imagem = qrcode.make(texto)

imagem.save("qrcode.png")

"""

import cv2

image = cv2.imread("image.png")

image_cinza = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("image_cinza",image_cinza)

cv2.waitKey(0)

cv2.destroyAllWinsdows()

