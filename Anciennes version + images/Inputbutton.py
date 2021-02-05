# -*- coding: utf-8 -*-
"""
Lycée Saint Joseph PIERRE ROUGE
Spécialité ISN
Connexion à la base de données MySQL
Auteur Florian Vié
"""

import mysql.connector
from tkinter import *
def Exereq(req):
    cursor.execute(req)
    rows = cursor.fetchall()
    for row in rows:
        #print('Pseudo : {0} - Scores : {1}'.format(row[1], row[3]))
        #On met le résultat sous forme de liste tant on a des réponses
        Label(master, text="Pseudo : {0} - Scores : {1}".format(row[1], row[3])).grid(row=0, column=3)
        
        
def LecturebdPseudo(Pseudo):
    req = "SELECT * FROM table1 WHERE Pseudo='"+ str(Pseudo)+"'" #lecture par pseudo dans la base de données
    Exereq(req)

conn = mysql.connector.connect(host="localhost",user="root",password="", database="projet")
cursor = conn.cursor()

def lecbd(Pseudo):
    LecturebdPseudo(Pseudo.get())

def update(Pseudo, Pays):
    Score=input("score:")
    bd.Updatescore(Pseudo.get(), Score, Pays.get())
  

master = Tk()
Label(master, text="Pseudo").grid(row=0)
Label(master, text="Pays").grid(row=1)

Pseudo = Entry(master)
Pays = Entry(master)

Pseudo.grid(row=0, column=1)
Pays.grid(row=1, column=1)

Button(master, text='Quitter', command=master.quit).grid(row=2, column=2, sticky=W)
Button(master, text='Inscription/Update', command=lambda: update(Pseudo, Pays)).grid(row=1, column=2, sticky=W)
Button(master, text='Lecture par pseudo', command=lambda: LecturebdPseudo(Pseudo.get())).grid(row=0, column=2, sticky=W)
#Button(master, text='Lecture de toute la base', command=lambda: lecture )

mainloop()
