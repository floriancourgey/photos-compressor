#! /usr/bin/env python3
# coding: utf-8

# imports
from __future__ import print_function
import os, sys
from PIL import Image, ExifTags
try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk
import wx
import wx.lib.inspection

from src.mainFrame import MainFrame

if __name__ == '__main__':
    """Run the application."""
    app = wx.App()
    # wx.lib.inspection.InspectionTool().Show()
    main_frame = MainFrame()
    app.MainLoop()
exit()

# options
largeur = 1920
hauteur = 1080
verbose = True
nom_fichier_sortie = "{nom} - compresse.jpg"
poids_max = 200 # kb
qualite = 85

# variables
nombre_compressions = 0;

# fonctions
# verbose
def v(texte):
    if(verbose):
        print(texte)
# resume
def print_resume():
    print("==================================================")
    print(titre+" lancé dans le dossier "+dossierActuel)
    nbImages = 0
    for root, dirs, fichiers in os.walk('.'):
        for fichier in fichiers:
            try:
                im = Image.open(fichier)
            except IOError as e:
                continue
            nbImages += 1
    print("Nombre d'images détectées : "+str(nbImages))
    print("Résumé des options :")
    print("\tLargeur de l'image compressée : "+str(largeur))
    print("\tHauteur de l'image compressée : "+str(hauteur))
    print("\tNom du l'image compressée : "+nom_fichier_sortie)
    print("\tQualite max du l'image compressée : "+str(qualite)+"%")
    print("\tPoids max du l'image compressée : "+str(poids_max)+" kb")
    print("==================================================")
    print()
# fonction principale




if(len(sys.argv) > 1):
    if(sys.argv[1] == "-options"):
        largeur = int(input("Largeur de l'image compressée ("+str(largeur)+") ") or str(largeur))
        hauteur = int(input("Hauteur de l'image compressée ("+str(hauteur)+") ") or str(hauteur))
        nom_fichier_sortie = input("Nom du fichier compresse ("+nom_fichier_sortie+") ") or nom_fichier_sortie

print_resume()


# lancement des bails
for root, dirs, fichiers in os.walk('.'):
    for fichier in fichiers:
        print(fichier)
        compress(fichier)
