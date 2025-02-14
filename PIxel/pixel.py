from PIL import Image #venv\Scripts\activate 

imagem=Image.open(r"C:\Users\henriquelucareli-ieg\Desktop\ProjetoCC\PIxel\imagens\antony.jpg")

print(imagem.getpixel((100, 100))) #Encontra a cor da imagem

imagem.show()