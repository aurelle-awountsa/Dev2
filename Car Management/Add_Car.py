#Importation des modules Tkinter et SQLite

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
from sqlite3 import Error
import os
import sys

from self import self

py = sys.executable

#Créer la fenêtre
class Voiture(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'Photos/logo.ico')
        self.configure(bg='dark grey')
        self.state('zoomed')
        self.title('Ajouter une voiture')
        carBrand = StringVar()  # Variable la marque de la voiture
        carNumber = StringVar()  # Variable pour le maticule de la voiture
        carStatus = StringVar()  # Variable pour le status d'une voiture
        carPhoto = StringVar()  # Variable pour le chemin du fichier image

        #upload la photo de la voiture
        def convertToBinaryData(filename):
            with open(filename, 'rb') as file:
                data = file.read()
            return data
        #entrer les information du véhicule

        def addCar(self):

                if len(carBrand.get()) < 1:
                    messagebox.showinfo("Oops, Veuillez entrer la marque de cette voiture")

                elif len(carNumber.get()) < 1:
                    messagebox.showinfo("Oops, veuilliez entre le numero de plaque de cette voiture")
                elif len(carStatus.get()) < 1:
                    messagebox.showinfo("Oops, veuilliez entre le status de disponibilité de cette voiture")

                elif len(carPhoto.get()) < 1:
                    messagebox.showinfo("Oops, veuilliez choisir une photo pour cette voiture")

                else:
                    try:
                        self.conn =  sqlite3.connect('CarDatabase.db')
                        self.myCursor = self.conn.cursor()
                        request = self.myCursor.execute("Insert into Cars('carBand','carNumber','carStatus','carPhoto') values (?,?,?,?)", [carBrand.get(), carNumber.get(), carStatus.get(), self.convertToBinaryData(carPhoto.get())])
                        self.conn.commit()

                        if request:
                            messagebox.showinfo("OK""Voiture ajoutée avec succès")
                            ask = messagebox.askyesno("Confirmer","Voulez vous ajouter une nouvelle voiture?")
                            if ask:
                                self.destroy()
                                os.system('%s %s' % (py, 'Add_Car.py'))
                            else:
                                self.destroy()
                        else:
                            messagebox.showerror("Erreur","Un problème est survenu lors de cette opération")
                        self.myCursor.close()
                        self.conn.close()
                    except Error:
                        messagebox.showerror("Erreur","Un problème est survenu lors de cette opération")

                #Créer le formulaire de remplissage de données

                entete = Label(self,text='Ajouter une voiture', fg='green', font=('Roboto', 20, 'bold')).pack()
                marque = Label(self, text='Marque de voiture:', font=('Roboto', 12, 'bold')).place(x=70, y=82)


Voiture().mainloop()