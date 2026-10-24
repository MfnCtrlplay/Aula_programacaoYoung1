import qrcode

texto = "Estou ensinando python para a melhor turma :D"

imagem = qrcode.make(texto)

imagem.save("qrcode.png")

