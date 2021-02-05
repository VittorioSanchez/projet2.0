# -*- coding: utf-8 -*-
"""
Lycée Saint Joseph PIERRE ROUGE
Spécialité ISN
Fonctions pour les actions sur la base de données MySQL
Auteur Florian Vié
"""

import mysql.connector
from tkinter import *

#Execution de la requête
def Exereq(req, fenetre):
    cursor.execute(req)
    rows = cursor.fetchall()
    n=0
    for row in rows:
        #print('Pseudo : {0} - Scores : {1}'.format(row[1], row[3]))
        #On met le résultat sous forme de liste tant on a des réponses puis on l'affiche dans l'interface
        Label(fenetre, text="Pseudo : {0} - Scores : {1}".format(row[1], row[3])).grid(row=n, column=3)
        n+=1
        
        
#Lecture de la totalité de la bd
def Lecturebd(fenetre):
    req = "SELECT * FROM table1"    # Lecture de toute la base de données
    Exereq(req, fenetre)

#Renvoi la liste des meilleurs joueurs
def meilleurscore(fenetre):
     req = "SELECT * FROM table1 ORDER BY Scores DESC, Pseudo LIMIT 10"    
     Exereq(req, fenetre)
     #cursor.execute(req)
     #rows = cursor.fetchall()
     #return rows
    
#Lecture bd sélective sur le pseudo
def LecturebdPseudo(Pseudo, fenetre):
    req = "SELECT * FROM table1 WHERE Pseudo='"+ str(Pseudo)+"'" # Lecture par pseudo dans la base de données
    Exereq(req, fenetre)
    
# Ecriture base de données
def Ecriturebd(Pseudo, Scores, Pays, fenetre):
    req = "SELECT COUNT(*) FROM table1 WHERE Pseudo='"+ str(Pseudo)+"'"
    cursor.execute(req)
    rows = cursor.fetchall()
    if rows[0][0]>0:            #Test pour éviter un doublon dans la base de données
        Label(fenetre, text="ERREUR Le Pseudo existe déjà").grid(row=1, column=3)
        #print('ERREUR Le Pseudo existe déjà')
    else:                       #Ecriture dans la base de données
        champ = (Pseudo,str(Scores), Pays)
        cursor.execute("""INSERT INTO table1 (Pseudo, Scores, Pays) VALUES(%s,%s,%s)""", champ)

# Calcul du score maximum après une partie
def Maxscore(Pseudo, Scores):
    req = "SELECT * FROM table1 WHERE Pseudo='"+ str(Pseudo)+"'"
    cursor.execute(req)
    scorebd = cursor.fetchall()
	# On renvoi le score maximum
    return max(Scores, int(scorebd[0][3]))
    

# Mise a jour du score
def Updatescore(Pseudo, Scores, fenetre, Pays=''):
    req = "SELECT COUNT(*) FROM table1 WHERE Pseudo='"+ str(Pseudo)+"'"
    cursor.execute(req)
    rows = cursor.fetchall()
    if rows[0][0]>0:            #Test pour éviter un doublon dans la base de données
        cursor.execute("UPDATE table1 SET Scores = "+str(Maxscore(Pseudo, Scores))+" WHERE Pseudo = '" + str(Pseudo)+"'")
    else:                       #Ecriture dans la base de données
        Label(fenetre, text="C'est bon vous êtres inscrit").grid(row=0, column=3)
        #print("vous n'êtes pas inscrit faites le maintenant")
        Ecriturebd(Pseudo, Scores, Pays, fenetre)

# Connexion à la base de données
#conn = mysql.connector.connect(host="172.17.21.125",user="florian",password="", database="projet")
#conn = mysql.connector.connect(host="192.168.43.25",user="florian",password="", database="projet")
conn = mysql.connector.connect(host="localhost",user="florian",password="", database="projet")
cursor = conn.cursor()

# Interface pour la base de données
def Interface(Scores):
    fenetre = Tk()
    
    fenetre.title("The shoot'em up")
    
    Label(fenetre, text="Pseudo").grid(row=0)
    Label(fenetre, text="Pays").grid(row=1)
    Label(fenetre, text="Votre score actuel :" + str(Scores)).grid(row=1, column=3)
    
    Pseudo = Entry(fenetre)
    Pays = Entry(fenetre)
    
    Pseudo.grid(row=0, column=1)
    Pays.grid(row=1, column=1)
    
    Button(fenetre, text='Quitter', command=fenetre.destroy).grid(row=2, column=0, sticky=W)
    Button(fenetre, text='Inscription/Update', command=lambda: Updatescore(Pseudo.get(), Scores, fenetre, Pays.get())).grid(row=2, column=1, sticky=W)
    Button(fenetre, text='Lecture par pseudo', command=lambda: LecturebdPseudo(Pseudo.get(),fenetre)).grid(row=0, column=2, sticky=W)
    Button(fenetre, text='Lecture de toute la base', command=lambda: Lecturebd(fenetre)).grid(row=1, column=2, sticky=W)
    Button(fenetre, text='Les 10 meilleurs scores', command=lambda: meilleurscore(fenetre)).grid(row=2, column=2, sticky=W)
    
    fenetre.mainloop()