# -*- coding:utf-8 -*-
import os
i=0
while i==0:
	annee = input("Saisissez une année : ") # On demande à l'utilisateur de saisir une année
	try : # On teste la valeur rentrée par ce dernier
		annee = int(annee) # On convertit la chaine de caractère en nombre entier si possible
		assert annee > 0
	except ValueError: # Si il saisit un caractère alphabétique
		print("Vous n'avez pas saisi un nombre.")
	except AssertionError: # Si il saisit une année inférieure ou égale à 0
		print("L'année saisie est inférieure ou égale à 0.")
	else: # Si la valeur saisie est bien un nombre strictement supérieur à zéro
		if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
		# Si l'année est un multiple de 400 ou un multiple de 4 mais pas de 100
			print ("L'année saisie est bissextile.")
		else: # Sinon 
			print ("L'année saisie n'est pas bissextile.")
	i=input("Saissez 0 pour recommencer ou autre chose pour quitter : ")
	# On demande à l'utilisateur si il veut tester une autre année ou non
	try : # On teste la valeur de i
		i=int(i) # On convertit la chaine de caractère en nombre entier si possible
		assert i==0 # On teste l'assertion i=0
	except AssertionError: # Si l'assertion est fausse
		print("Au revoir !")
	except ValueError: # Si la valeur saisie n'est pas un nombre
		print("Au revoir !")
os.system("pause")
