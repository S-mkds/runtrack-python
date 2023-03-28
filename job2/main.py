# Job1
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print(f"Je m'appelle {self.prenom} {self.nom}")

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, prenom):
        self.prenom = prenom


p1 = Personne("Dupont", "Jean")
p1.SePresenter()

p2 = Personne("Martin", "Sophie")
p2.SePresenter()

p1.set_nom("Durand")
p1.SePresenter()

print(p1.get_nom())
print(p2.get_prenom())


# Job 2
print("***********")


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre)


class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        print("Oeuvre de :", self.nom, self.prenom)
        for livre in self.oeuvre:
            print(livre.titre)

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        return livre


auteur = Auteur("Hugo", "Victor")
livre1 = auteur.ecrireUnLivre("Les Misérables")
livre2 = auteur.ecrireUnLivre("Notre-Dame de Paris")

livre1.print()
livre2.print()

auteur.listerOeuvre()

# Job 3
print("***********")


class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        print(f"Liste des livres écrits par {self.nom} {self.prenom}:")
        for livre in self.oeuvre:
            print(livre.titre)

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        return livre


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return self.titre


class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        print(f"Liste des livres en possession de {self.nom} {self.prenom}:")
        for livre in self.collection:
            print(livre.titre)


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                if titre in self.catalogue:
                    self.catalogue[titre] += quantite
                else:
                    self.catalogue[titre] = quantite
                print(
                    f"{quantite} exemplaire(s) du livre '{titre}' de l'auteur {auteur.nom} ont été ajouté(s) au catalogue de la bibliothèque.")
                return
        print(
            f"Le livre '{titre}' de l'auteur {auteur.nom} n'existe pas dans son oeuvre.")

    def inventaire(self):
        print(f"Catalogue de la bibliothèque '{self.nom}':")
        for livre, quantite in self.catalogue.items():
            print(f"{livre}: {quantite} exemplaires")

    def louer(self, client, titre):
        if titre in self.catalogue and self.catalogue[titre] > 0:
            self.catalogue[titre] -= 1
            livre = Livre(titre, None)
            client.collection.append(livre)
            print(f"{client.nom} {client.prenom} a loué le livre '{titre}'.")
        else:
            print(f"Le livre '{titre}' n'est pas disponible en ce moment.")

    def rendreLivres(self, client):
        for livre in client.collection:
            if livre.titre in self.catalogue:
                self.catalogue[livre.titre] += 1
            else:
                self.catalogue[livre.titre] = 1
        print(f"{client.nom} {client.prenom} a rendu tous ses livres.")


class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        for livre in self.oeuvre:
            print(livre.titre)

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        return livre


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre)


class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        for livre in self.collection:
            print(livre.titre)


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                if titre in self.catalogue:
                    self.catalogue[titre] += quantite
                else:
                    self.catalogue[titre] = quantite
                return True
        return False

    def inventaire(self):
        for titre, quantite in self.catalogue.items():
            print(titre, quantite)

    def louer(self, client, titre):
        if titre in self.catalogue and self.catalogue[titre] > 0:
            livre = Livre(titre, self)
            self.catalogue[titre] -= 1
            client.collection.append(livre)
            return True
        else:
            return False

    def rendreLivres(self, client):
        for livre in client.collection:
            if livre.titre in self.catalogue:
                self.catalogue[livre.titre] += 1
            else:
                self.catalogue[livre.titre] = 1
        client.collection.clear()


# Création d'auteurs et de leurs livres
auteur1 = Auteur("Martin", "George R. R.")
livre1 = auteur1.ecrireUnLivre("Game of Thrones")
livre2 = auteur1.ecrireUnLivre("A Clash of Kings")

auteur2 = Auteur("Rowling", "J.K.")
livre3 = auteur2.ecrireUnLivre("Harry Potter and the Philosopher's Stone")
livre4 = auteur2.ecrireUnLivre("Harry Potter and the Chamber of Secrets")

# Création de bibliothèques
biblio1 = Bibliotheque("Bibliothèque municipale")
biblio2 = Bibliotheque("Bibliothèque universitaire")

# Achat de livres par les bibliothèques
biblio1.acheterLivre(auteur1, "Game of Thrones", 5)
biblio1.acheterLivre(auteur1, "A Clash of Kings", 3)
biblio2.acheterLivre(auteur2, "Harry Potter and the Philosopher's Stone", 2)
biblio2.acheterLivre(auteur2, "Harry Potter and the Chamber of Secrets", 1)

# Création de clients
client1 = Client("Dupont", "Jean")
client2 = Client("Durand", "Marie")

# Location de livres par les clients
biblio1.louer(client1, "Game of Thrones")
biblio1.louer(client1, "A Clash of Kings")
biblio2.louer(client2, "Harry Potter and the Philosopher's Stone")
biblio2.louer(client2, "Harry Potter and the Chamber of Secrets")

print("nombre de livre à rendre", len(
    client1.collection) + len(client2.collection))
biblio1.rendreLivres(client1)
biblio2.rendreLivres(client2)

print("nombre de livres total dans les bibliothèques", biblio1.catalogue["Game of Thrones"] + biblio1.catalogue["A Clash of Kings"] +
      biblio2.catalogue["Harry Potter and the Philosopher's Stone"] + biblio2.catalogue["Harry Potter and the Chamber of Secrets"])
biblio1.inventaire()
biblio2.inventaire()


client1.inventaire()
client2.inventaire()

# Job 4
print("***********")


class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.board = [['O' for _ in range(j)] for _ in range(i)]

    def play(self, col, color):
        if col < 0 or col >= self.j:
            print("Colonne invalide, veuillez choisir une colonne entre 0 et 6")
            return False
        for row in range(self.i-1, -1, -1):
            if self.board[row][col] == 'O':
                self.board[row][col] = color[0]
                return True
        print("Colonne pleine !!")
        return False

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def check_win(self, color):
        # check horizontal
        for row in range(self.i):
            for col in range(self.j-3):
                if self.board[row][col] == color[0] and self.board[row][col+1] == color[0] and self.board[row][col+2] == color[0] and self.board[row][col+3] == color[0]:
                    return True

        # check vertical
        for row in range(self.i-3):
            for col in range(self.j):
                if self.board[row][col] == color[0] and self.board[row+1][col] == color[0] and self.board[row+2][col] == color[0] and self.board[row+3][col] == color[0]:
                    return True

        # check diagonal
        for row in range(self.i-3):
            for col in range(self.j-3):
                if self.board[row][col] == color[0] and self.board[row+1][col+1] == color[0] and self.board[row+2][col+2] == color[0] and self.board[row+3][col+3] == color[0]:
                    return True
                if self.board[row+3][col] == color[0] and self.board[row+2][col+1] == color[0] and self.board[row+1][col+2] == color[0] and self.board[row][col+3] == color[0]:
                    return True

        return False


board = Board(6, 7)  # créer un plateau de 6 lignes et 7 colonnes
current_player = 'rouge'  # le joueur rouge commence la partie
winner = None  # variable pour stocker le gagnant de la partie

while not winner:
    # demander à l'utilisateur de saisir une colonne
    col = int(input(
        f"{current_player}, dans quelle colonne voulez-vous insérer votre jeton ? de 0 à 6 "))

    # insérer le jeton sur le plateau
    if board.play(col, current_player):
        board.print()  # afficher l'état actuel du plateau
        # vérifier si le joueur a gagné
        if board.check_win(current_player):
            winner = current_player
        # passer le tour au joueur suivant
        current_player = 'jaune' if current_player == 'rouge' else 'rouge'

# afficher le gagnant
print(
    f"Félicitations, {winner} a gagné la partie voici le chèque 100.000 euros !")
