from random import randint

#Code du jeu

def game (player):

    ###########
    #Fonctions#
    ###########
    #NOT WORKING
    # test si l'entrée et un nombre 0 et 100
    def chktype(player):
        try:
            val = int(player)
        except ValueError:
            player = input('Choisissez un nombre entier : ')

    # test de si le nombre est entre 0 et 100
    def chkbound(player):
        while int(player) < 0 or int(player) > 100:
            player = input('Choisissez un nombre entier : ')

    # fonction qui verifie si le nombre donne est trop grand ou trop petit
    def check(player):
        # si trop petit : nouvel essai
        if int(player) < goal:
            print('Trop petit')
            player2 = input('Nouvel essai : ')
            # appel recursif
            check(int(player2))

        # si trop grand : nouvel essai
        elif int(player) > goal:
            print ('trop grand')
            player2 = input('Nouvel essai : ')
            #appel recursif
            check(int(player2))

        # sinon : gagne
        else:
            print('Gagné ! Bravo. La réponse était bien ' + str(goal) + '.')


    ################
    #Implementation#
    ################

    # nombre a trouver, genere psedo-aleatoirement
    goal = randint(0, 100)

    chkbound(player)
    check(player)





#--------------------------#
#       Appel du jeu       #
#--------------------------#

print('________________________________________________________')
print('| Jeu de devinette : trouver le chiffre entre 0 et 100 |')
print('________________________________________________________\n')
a = input('Choisissez un nombre entier : ')
game(a)