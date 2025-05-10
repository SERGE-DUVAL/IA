
"""
#sert a creer un tableua 1D et precise le type avec dtype et si j'ajoute le ndmin c'est le nombre de domension
arr=np.array([1,2,3,4,9,10] ,dtype="i4")
#sert a changer de type
ne=arr.astype(str)
#sert a faire une copy du tableau
x=arr.copy()
#change la valeur du tableau mais la copie ne subit aucun changement mais s c'est la view ca vas changer
arr[0]=5
#sert a demander d'afficher la base
print(x.base)
print(ne)
print(arr)
#sert afficher le type
print(arr.dtype)
#affiche la taille du tableau en tuple
print(arr.shape)
#divise le tableau en 3 lignes 2 colonnes
print(arr.reshape(3,2))
"""
from tkinter import mainloop

"""
#iteration de tableau

#tableau 2D
arr2=np.array([[1,2,3],[4,5,6]])
#apprentissage parcour du tableau
for x in arr2:
    print(x)
#tableau 3D
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
#nditer perme de lire un as un
for x in np.nditer(arr3):
  print(x)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#pour enumerer le tableau avec l'index
for  idx,x in np.ndenumerate(a):
    print(idx,x)
"""
"""
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])
a=np.array([1,2,3,4,5])
#concatene
arr = np.concatenate((arr1, arr2),axis=1)
arr=np.stack((arr1,arr2),axis=1)
#condition
x=np.where(a==5)
print(x)
print(arr)
"""
"""
import tkinter as tk
from tkinter import messagebox
import numpy as np

# Fonction appelée quand on clique sur le bouton
def calculer_resultat():
    try:
        # Récupérer les notes depuis le champ d'entrée
        notes_str = entree_notes.get()
        notes = np.array([float(n) for n in notes_str.split(",")])
        moyenne = np.mean(notes)

        # Afficher le résultat
        if moyenne >= 10:
            resultat = f"Moyenne : {moyenne:.2f}\nRésultat : Admis "
        else:
            resultat = f"Moyenne : {moyenne:.2f}\nRésultat : Échoué "

        messagebox.showinfo("Résultat", resultat)

    except ValueError:
        messagebox.showerror("Erreur", "Entre des notes valides séparées par des espaces !")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Mini IA - Résultat Élève")

# Texte et champ d'entrée
label = tk.Label(fenetre, text="Entre tes notes (ex: 14 10 8) :", font=("Arial", 12))
label.pack(pady=10)

entree_notes = tk.Entry(fenetre, width=40)
entree_notes.pack(pady=5)

# Bouton pour lancer le calcul
bouton = tk.Button(fenetre, text="Vérifier le résultat", command=calculer_resultat)
bouton.pack(pady=15)

# Lancer la fenêtre
fenetre.mainloop()
"""
def calculdemoyenne():
    try:
        tr = True
        notes = []
        coefs = []
        print("je suis l'applie qui vous aide a calculer  votre moyenne en fonctionde coeff ou de credit")
        while tr == True:
            nombre = int(input("combien de matiere avez vous: "))
            for i in range(1, nombre + 1):
                note = float(input("entre votre note: "))
                coef = int(input("entre le coefficient ou le credit de votre matiere: "))
                notes.append(note)
                coefs.append(coef)
                print(f"voici les coef ou credit que vous avez entre dans l'ordre d'entrer {coefs}")

        scoef=0
        somme=0
        for j in range(0,nombre):
            somme=somme+(notes[j]*coefs[j])
            scoef=coefs[j]+scoef

        moy = somme / scoef
        print(f"votre moyenne est {moy}")

        decision=input("voulez vous enregistrer votre moyennedans un fichier pour la conserver? (oui ou non)(1 seule chance: ")
        if decision.lower() == "oui":
            nom=input("entreer votre nom: ")
            with open(f'{nom}.txt',"a") as fi:
                fi.writelines(f"la somme des note est {somme} \n")
                fi.writelines(f"la somme des coef est {scoef} \n")
                fi.writelines(f"la moyenne {nom} est de {moy} avec {nombre} matiere \n")
            print(f"il as ete enregistrer dans le fichier {nom}.txt")

        tr = None
        while tr == None:
            dec = input("voulez vous continuez? (oui ou non): ")
            if dec.lower() == "oui":
                tr = True
            elif dec.lower() == "non":
                tr = False
            else:
                print("entre un oui ou un non")
    except ValueError:
        print("entrer des valeur correcte",ValueError)
def vocal():
    from tkinter import simpledialog
    import tkinter as tk
    import speech_recognition as sr
    import pyttsx3
    import json
    import os

    # Initialiser la synthèse vocale
    moteur = pyttsx3.init()

    # Mémoire (base de données locale)
    fichier_memoire = "memoire.json"
    if os.path.exists(fichier_memoire):
        with open(fichier_memoire, "r",encoding="utf-8") as f:
            memoire = json.load(f)
    else:
        memoire = {}

    # Parler avec la synthèse vocale
    def parler(texte):
        moteur.say(texte)
        moteur.runAndWait()

    # Écouter avec le micro
    def ecouter():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            texte_recu.set("Je t'écoute...")
            fenetre.update()
            audio = recognizer.listen(source)
        try:
            question = recognizer.recognize_google(audio, language="fr-FR")
            texte_recu.set("Tu as dit : " + question)
            repondre(question)
        except sr.UnknownValueError:
            texte_recu.set("Je n'ai pas compris.")
        except sr.RequestError:
            texte_recu.set("Erreur de service de reconnaissance.")

    # Répondre à une question
    def repondre(question):
        question = question.lower()
        if question in memoire:
            reponse = memoire[question]
        else:
            reponse = f"Je ne sais pas répondre à '{question}'. Que dois-je dire ? Je ne suis qu'une petite ia en apprentissage"
            texte_recu.set(reponse)
            parler(reponse)
            reponse_utilisateur = simpledialog.askstring("Apprentissage", f"Réponse pour : {question}")
            if reponse_utilisateur:
                memoire[question] = reponse_utilisateur
                with open(fichier_memoire, "w",encoding="utf-8") as f:
                    json.dump(memoire, f, indent=4)
                reponse = reponse_utilisateur
        texte_recu.set("Réponse : " + reponse)
        parler(reponse)

    # Interface graphique
    fenetre = tk.Tk()
    fenetre.title("Assistant Vocal")
    fenetre.geometry("400x300")

    texte_recu = tk.StringVar()
    label = tk.Label(fenetre, textvariable=texte_recu, wraplength=380, font=("Arial", 12))
    label.pack(pady=20)

    bouton = tk.Button(fenetre, text="Parle-moi", command=ecouter, font=("Arial", 14))
    bouton.pack()

    fenetre.mainloop()


if __name__ == '__main__':
    a=int(input("entre 1 pour calculer la moyenne ou 2 pour l'assistant vocal: "))
    if a==1:
        calculdemoyenne()
    elif a==2:
        vocal()


