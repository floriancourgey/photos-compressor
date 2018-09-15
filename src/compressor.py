#! /usr/bin/env python3
# coding: utf-8

class Compressor:
    '''
    @param filename a relative path or a PIL image
    '''
    def compress(self, filename):
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
            # keep orientation
            v("\torientation")
            im = rotate_selon_orientation(im)
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
    def rotate_selon_orientation(image):
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation]=='Orientation':
                    break
            exif=dict(image._getexif().items())

            if exif[orientation] == 3:
                image=image.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image=image.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image=image.rotate(90, expand=True)

        except (AttributeError, KeyError, IndexError):
            pass

        return image
    def v(texte):
        verbose = True
        if(verbose):
            print(texte)
