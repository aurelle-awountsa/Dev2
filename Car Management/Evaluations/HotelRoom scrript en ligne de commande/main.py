class Chambres:

    def __init__(self, numero, etage, categorie, libre=True):
        """ cette fonction crée un objet chambre
             PRE: numero numero de chambre  , etage etage où se trouve la chambre,categorie pour la categorie de la chambre libre dit si la chambre est disponible
             POST: un objet Chambre
        """

        self._numero = numero
        self._etage = etage
        self._categorie = categorie
        self.libre = libre

    @property
    def numero(self):
        return self._numero

    @property
    def etage(self):
        return self._etage

    @property
    def categorie(self):
        return self._categorie

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

             PRE : receive a book Object
             POST :  returns a textual representation of the book oject
         """
        return f' Numéro de chambre: {self.numero}, Etage: {self.etage}, Catégorie: {self.categorie}'

class Hotel:

    def __init__(self, listOfRooms):

        """Return a textual representation of the reduced form of the fraction

            PRE : reçoit l'objet chambre
            POST : retourne une représentation textuelle de l'objet chambre
        """

        self.listOfRooms = listOfRooms

    def ajoutChambre(self, chambre):
        """
          cette fonction permet d'ajouter une nouvelle chambre
            PRE : reçoit deux objets, l'objet la liste des chambres  et l'objet chambre que nous voulons ajouter.
            POST:nouvelle liste de chambres
        """

        self.listOfRooms.append(chambre)
        return self.listOfRooms

    def AfficherChambre(self):
        """
           cette fonction permet de voir toutes les chambres disponible
            PRE: reçoit l'objet liste de chambre
            POST: nouvelle liste de chambre disponible dans la liste
        """

        chambresLibres = []

        for chambre in self.listOfRooms:
            if chambre.libre:
                chambresLibres.append(chambre)
        if len(chambresLibres) > 0:
            print("Les chambre suivantes sont disponible:")
            for chambreLibre in chambresLibres:
                print(chambreLibre)
        else:
            print("Désolé!!! Aucune chambre n'est actuellement disponble")

    def afficherChambresLouées(self):

        """
            cette fonction permet d'afficher toutes les chambres louées
            PRE: reçoit un objet liste de chambre
            POST: nouvelle liste de chambre louée
        """
        chambresLouees = []

        for chambre in self.listOfRooms:
            if not chambre.libre:
                chambresLouees.append(chambre)
        if len(chambresLouees) > 0:
            print("les chambres suivantes sont actuellement louées: ")
            for chambrelouee in chambresLouees:
                print(chambrelouee)
        else:
            print('pas de chambres louées')

    def louerChambre(self, numero, etage, categorie, client):
        """
           cette fonction permet de louer une chambre
            PRE: reçoit un objet liste de chambre, numero,etage, categorie et client qui souhaite loué la chambre
            POST: confirmation de location
        """
        found = False
        for chambre in self.listOfRooms:
            if numero == chambre.numero and etage == chambre.etage and categorie == chambre.categorie:
                if chambre.libre:
                    print(f" La {numero}  de l'étage {etage} de cathégorie {categorie} a été louée par {client.name} ")

                else:
                    print("Desole!!! Cette chambre a deja été louée par quelqu'un d'autre. veuillez choisir une autre")
                    return False
                found = True

                chambre.libre = False
                break
        if not found:
            print('entrer le bon numero')

    def finLocation(self, numero, etage, categorie, client):
        """
            Cette fonction permet d'introduire une fin de location
            PRE: reçoit un objet liste de chambre, numero,etage, categorie et client qui souhaite loué la chambre
            POST: confirmation de location

        """

        for chambre in self.listOfRooms:
            if numero == chambre.numero and etage == chambre.etage and categorie == chambre.categorie:
                chambre.libre = True
        print(f" La {numero}  de l'étage {etage} de cathégorie {categorie} a été retournée par {client.name} ")


class Client:
    def __init__(self, name, contact):
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
    chambre1 = Chambres('Chambre1','Etage 2', 'Luxieuse','Flore Fosso')
    chambre2 = Chambres('Chambre2','Etage 5', 'Suite nuptial', 'Roger Christophe')
    list_room = [chambre1, chambre2]

    listeChambre = Hotel(list_room)
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
            listeChambre.ajoutChambre(chambre)
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


