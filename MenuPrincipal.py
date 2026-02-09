import sys

from ConvertisseurImagePDF import conversionImage2PDF
from ConvertisseurTextePDF import text_to_pdf
from Fusion2pdf import merge_pdfs

def ajout_extensionPDF(nom_fichier):
    if not nom_fichier.lower().endswith('.pdf'):
        return nom_fichier +".pdf"
    return nom_fichier

def afficher_menu_principal():
    """
    Permet de donner un affichage dans le terminal pour que
    l'utilisateur puisse saisir ce qu'il veut faire avec son PDF.
    :return: Retourne le fichier/les fichiers en fonction de l'option choisie.
    """
    print("---------------------")
    print("----- MENU ----------")
    print("Veuillez saisir une des options disponibles :")
    print("1. Conversion d'une image en PDF.")
    print("2. Conversion d'un texte en PDF.")
    print("3. Fusion de 2 PDF en 1 seul PDF.")
    print("4. Quitter")


def main():
    while True:
        afficher_menu_principal()
        choix = input("choix : ")

        match choix:

            case "1":
                    print("Conversion d'une image en PDF : ")
                    fichier_source = input("Donnez le chemin du fichier : ")
                    fichier_destination = input("Donnez le nom du fichier PDF de sortie : ")
                    destination = ajout_extensionPDF(fichier_destination)
                    conversionImage2PDF(fichier_source, destination)
                    print("Conversion de l'image en PDF finie !")
                    print("Merci de votre utilisation !")

            case "2" :
                    print("Conversion d'un texte en PDF : ")
                    texte_source = input("Donnez le texte à convertir : ")
                    texte_destination = input("Donnez le nom du texte PDF de sortie : ")
                    destination = ajout_extensionPDF(texte_destination)
                    text_to_pdf(texte_source, destination)
                    print("Conversion d'un texte en PDF finie !")
                    print("Merci de votre utilisation !")
            case "3" :
                    print("Conversion d'un texte en PDF : ")
                    fichier = input("Donnez le nom du fichier (séparé par une virgule) : ")
                    conversion_liste = [nom.strip() for nom in fichier.split(",")]
                    sortie = input("Donnez le nom du sortie : ")
                    nom_sortie = ajout_extensionPDF(sortie)
                    merge_pdfs(conversion_liste, nom_sortie)
                    print("Conversion d'un texte en PDF finie !")
                    print("Merci de votre utilisation !")

            case "4" :
                print("Fermeture du programme")
                print("Merci de votre utilisation !")
                sys.exit()

            case _:
                print("Option invalide, veuillez saisir une option valide.")

if __name__ == "__main__":
    main()
