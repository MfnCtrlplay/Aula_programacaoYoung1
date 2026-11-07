
# codigo utilizado para criar e escrever um arquivo txt

""" with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Escrevendo um arquivo em Python!!!")
"""

#codigo utilizado para ler o arquivo

""" with open("dados.txt", "r") as arquivo:
    texto = arquivo.read();
    print(texto)
"""

#codigo para adicionar texto ao arquivo

with open("dados.txt", "a", encoding= "utf-8") as arquivo:
    arquivo.write("\n") #adicionando uma quebra de linha
    arquivo.write("Adicionando mais Texto")