from PIL import Image

def conversionImage2PDF(image_chemin, pdf):
    image = Image.open(image_chemin)
    image.convert('RGB')
    image.save(pdf)

"""
Assurez-vous d'avoir les fichiers dans le dossier du projet.
"""
# conversionImage2PDF("", "sortie.pdf")