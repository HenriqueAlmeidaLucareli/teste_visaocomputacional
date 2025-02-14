from PIL import Image, ImageFilter #venv\Scripts\activate 
import os

data_dir=os.path.join('filtros','data')

imagem=Image.open(os.path.join(data_dir,r"C:\Users\henriquelucareli-ieg\Desktop\ProjetoCC\Filtro\imagem\download.jpg"))

filtro=imagem.filter(ImageFilter.CONTOUR)

filtro.show()
# imagem.show()