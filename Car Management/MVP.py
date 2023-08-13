import sqlite3
from sqlite3 import Error

class Cars:

    def __init__(self, matricule, marque, modele, libre):
        """ cette fonction crée un objet voiture
             PRE: matricule de la voiture  , marque de la voiture ,modele de la voiture,  libre dit si la voiture est disponible ou pas
             POST: un objet voiture
        """

        self._matricule = matricule
        self._marque = marque
        self._modele= modele
        self._libre= libre
        @property
        def matricule(self):
         return self._matricule

    @property
    def marque(self):
        return self._marque

    @property
    def modele(self):
        return self._modele

    def __str__(self):
         """cette fonction retourne le représentation d'une chambre

             PRE : recoit un objet chambre
             POST : retourne la représentation d'une chambre
         """
         return f' Matricule: {self.matricule}, marque: {self.marque}, modele: {self.modele}, libre: {self.libre}'

    while (True):
        welcomeMsg = '''\n ====== Gestion de stocke de voitures ======
       
         Veuillez choisir une option:
         1. Ajouter une nouvelle voiture 
         
         '''
        print(welcomeMsg)
        a = int(input("Entrer votre choix: "))


        """====== Ajouter une voiture ======"""


        if a == 1:
            matricule = input(' Entrer le matricule de la voiture ')
            marque = input("Entrer la marque de la voiture")
            modele = input("Entrer le modele  de la voiture ")
            libre = input("libre oui ou non")


            conn = sqlite3.connect('database.db')
            myCursor = conn.cursor()
            myCursor.execute("insert into Cars values (?,?,?,?)",[matricule,marque,modele,libre])
            conn.commit()
            print( 'ajouter avec succes')
            conn.close()

