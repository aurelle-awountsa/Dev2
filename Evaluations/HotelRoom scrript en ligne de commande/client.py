from main import *
class Client:
    def __int__(self, name, contact):
        """
          this function allows you to create a new student
          PRE: receive a name and contact
          POST: a student object
        """

        self._name = name
        self._contact = contact

    @property
    def name(self):
        return self._name

    @property
    def contact(self):
        return self._contact

    def requestRoom(self):
        try:
            self.numero = input("Entrer le numéro de la chambre à louer: ")
            return self.numero
            self.etage = input("Entrer l'étage où se trouve la chambre à louer: ")
            return self.etage
            self.categorie = input("Entrer la catégode la chambre à louer: ")
            return self.categorie
        except (ValueError, AttributeError):
            print('Choix incorrect de la salle')


def returnRoom(self):

    self.numero = input("Enter le numero de la chambre que vous souhaitez retourner: ")
    return self.numero


if __name__ == "__main__":
    chambre1 = Chambres('Chambre1','Etage 2', 'Luxieuse' 'Flore Fosso')
    chambre2 = Chambres('Chambre2','Etage 5', 'Suite nuptial' 'Roger Christophe')
    list_room = [chambre1, chambre2]
    listeChambre = Chambres(list_room)
    while (True):
        welcomeMsg = '''\n ====== Location de chambres ======
         Bienvenue Dans Notre Hotel

         Veuillez choisir une option:
         1. Ajouter une nouvelle livre chambre
         2. Afficher les chambres disponibles
         3. Afficher les chambres louées
         4. Louer une chambre
         5. Fin de location
         6. Terminer
         '''
        print(welcomeMsg)
        a = int(input("Entrer votre choix: "))
        if a == 1:
            numero = input(' Entrer le numero de la chambre ')
            etage = input("Entrer le numero d'étage où se touve la chambre ")
            categorie = input("Entrer la catégorie de la chambre ")

            chambre = Chambres(numero, etage, categorie)
            listeChambre.AjoutChambre(chambre)
        elif a == 2:
            listeChambre.AfficherChambre()

        elif a == 3:
           listeChambre.afficherChambresLouées()
        elif a == 4:
            name = input('''Entrer le nom du client ''')
            contact = input(''' Entrer le contact du client ''')
            client = Client(name, contact)
            listeChambre.louerChambre(client.requestRoom(), client)
        elif a == 5:
            client1 = input('''Entrer le nom du client ''')
            listeChambre.finLocation(client.returnRoom(), client1)
        elif a == 6:
            print("A tres bientot !")
            exit()