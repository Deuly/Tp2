"""code creer par Justin-Deuly Dybka-Spies
creer le (29-09-2022)
Tp2 """






from random import *

def jeu_devinette():
    jeu = True
    print("Voici un jeu de devinette.\n Vous allez devoir devinez un nombre entre 0 et 100")
    jouer_1 = str(input("Voulez vous jouez (oui ou non):"))

    if jouer_1 == "oui" or "Oui" or "O":
        nbr_max = int(input("entrer la limite pour le nombre maximale que voudrez devinez:"))
        nbr_min = int(input("entrer la limite pour le nombre minimale que voudrez devinez:"))

        nbr_esais = 1
        nbr_dev = randint(nbr_max,nbr_min)

        not_found = True
        while not_found:
            nbr_cherche = int(input("Devinez un nombre:"))



jeu_devinette()

"""while jeu_dev:
essai_1 = int(input("")"""
        
    
    
    


"""nb_essaie = 0

jouer = True
def main():
    global jouer, nb_essaie
    while jouer:
        random_number = randint(0, 100)

        not_found = True
        while not_found:

            user_guess = int(input("deviner un numéro \n"))
            nb_essaie += 1
            if user_guess < random_number:
                print("Vôtre numéro est trop petit")

            elif user_guess > random_number:
                print("Vôtre numéro est trop grand.")

            elif user_guess == random_number:
                print(f"Bravo! Vous avez devinez le numéro en {nb_essaie} essaies.")
                rejouer = input("Voulez-vous rejouer? (y/n)")
                not_found = False

                if rejouer == "y":
                    jouer = True

                elif rejouer == "n":
                    print("Au revoir")
                    jouer = False """

