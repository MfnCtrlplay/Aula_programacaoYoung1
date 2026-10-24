import cv2

image = cv2.imread("image.png")

print("1 - Tons de cinza")
print("2 - Desfoque")
print("3 - Negativo")

opcao = input("Escolha um filtro entre 1 e 3: ")

if opcao == "1":
    image_filtro = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
elif opcao == "2":
    image_filtro = cv2.GaussianBlur(image, (15, 15), 0)
elif opcao == "3":
    image_filtro = cv2.bitwise_not(image)
else:
    print("Opção inválida.")
    image_filtro = image

cv2.imshow("Imagem com filtro", image_filtro)

cv2.waitKey(0)

cv2.destroyAllWindows()
