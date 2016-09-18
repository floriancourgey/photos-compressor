#!/usr/bin/python
# -*- coding: utf-8 -*-

# imports
from __future__ import print_function
import os, sys
from PIL import Image
try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk

# constantes
titre = "Photo compressor"
dossierActuel = os.getcwd();

# presentation

print("##############################################")
print("#                                            #")
print("#    "+titre+" par Florian Courgey    #")
print("#                                            #")
print("##############################################")
print()

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
def compress(nom_fichier):
    v("compression de " + nom_fichier)
    global nombre_compressions
    nombre_compressions += 1
    outfile = nom_fichier_sortie
    outfile = outfile.replace("{nom}", os.path.splitext(nom_fichier)[0])
    outfile = outfile.replace("{#}", str(nombre_compressions))
    try:
        # check poids
        poids = os.path.getsize(nom_fichier)/1000
        if(poids < poids_max):
            print(nom_fichier+" deja inférieur à la taille limite ("+str(poids)+"kb < "+str(poids_max)+" kb)\n")
            return;
        # ouverture
        v("\touverture")
        im = Image.open(nom_fichier)
        # resize
        v("\tredimensionnement")
        im.thumbnail((largeur, hauteur))
        # save en jpg de moindre qualite
        v("\tenregistrement")
        qua = qualite
        im.save(outfile, "JPEG", quality=qua)
        poids = os.path.getsize(outfile)/1000
        while(poids > poids_max and qua>1):
            qua = qua - 5
            if(qua < 5):
                break;
            print("\tFichier trop gros ("+str(poids)+"kb > "+str(poids_max)+"kb), descente de qualite en "+str(qua)+"%")
            im.save(outfile, "JPEG", quality=qua)
            poids = os.path.getsize(outfile)/1000
        v("compression de " + nom_fichier + " > "+outfile+" terminee")
    except IOError as e:
        print("impossible de compresser "+ nom_fichier+ " (",e,")")
    print()


if(len(sys.argv) > 1):
    if(sys.argv[1] == "-options"):
        largeur = int(input("Largeur de l'image compressée ("+str(largeur)+") ") or str(largeur))
        hauteur = int(input("Hauteur de l'image compressée ("+str(hauteur)+") ") or str(hauteur))
        nom_fichier_sortie = input("Nom du fichier compresse ("+nom_fichier_sortie+") ") or nom_fichier_sortie

print_resume()

reponse = raw_input('Continuer ? (o/n) ')
if not reponse or reponse[0].lower() != 'o':
    print("fin")
    sys.exit(0)

# lancement des bails
for root, dirs, fichiers in os.walk('.'):
    for fichier in fichiers:
        print(fichier)
        compress(fichier)
# compress(".\\attachment-img-1000x200.c.c.jpg");
# compress("attachment-img-1000x200.jpg");
# compress("attachment-img-1000x200.c.jpg");
# compress("BYOD2.jpg");
# compress("color00.jpg");


# print(im.format, im.size, im.mode)
# im.show();
