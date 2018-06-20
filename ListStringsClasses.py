import os
import pickle



ma_liste = [1, 3.5, "ceci nest pas une chaine", []]



##########
#Fichiers#
##########

#Aller au repo
os.chdir("files")

def clear():
    myfile = open("firstFile.lel", "w")
    myfile.close()

def writeStr():
    text = input("Ecrivez votre string : ")
    #creation du fichier
    myfile = open("firstFile.lel","a")
    myfile.write(str(text) + "\n")
    myfile.close()

def readFile():
    print("\n Affichage du contenu du fichier : \n")
    myfile = open("firstFile.lel","r")
    print(myfile.read())
    myfile.close()

def ecriture():
    i=""

    i = input("Wanna clear the file? y/n : ")
    if (i == "y" ):
        clear()

    while(i != "q"):
        writeStr()
        i = input("Arreter : q : ")

    i = input("Voir le contenu du fichier? o/n :")
    if (i == "o"):
        readFile()
    else : exit(10)

ecriture()