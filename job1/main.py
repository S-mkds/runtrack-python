# Job print calcul
print("10 + 3 =", 10 + 3)
print("10 * 3 =", 10 * 3)
print("10 % 3 =", 10 % 3)
print("10 - 3 =", 10 - 3)
print("10 / 3 =", 10 / 3)
print("10 // 3 =", 10 // 3)

#  Job fonction Add


def Add(a, b):
    somme = a + b
    return somme


print(Add(2, 3))
print(Add(5, 7))
print(Add(11, 20))

# Job prenom
prenom = input("Rensegnez votre prénom : ")
print("Hello", prenom + " !")


# Job boucle qui rentre 5 nombres et les affiche dans l'ordre croissant
nombres = []

for i in range(5):
    nombre = int(input("Entrez un nombre entier : "))
    nombres.append(nombre)

nombres.sort()

print("Les nombres triés par ordre croissant sont : ")
for nombre in nombres:
    print(nombre)

# Job crée un rectangle


def draw_rectangle(width, height):
    # Dessine la première ligne avec des "-"
    print("-" * (width + 4))

    # Dessine les lignes du milieu avec "|", " " et "|"
    for i in range(height - 2):
        print("|   " + " " * (width - 2) + "   |")

    # Dessine la dernière ligne avec des "-"
    print("-" * (width + 4))


# Appelle la fonction draw_rectangle avec width=10 et height=3
draw_rectangle(10, 3)


#  Job triangle
def draw_triangle(height):
    # Dessine la première ligne avec un trait à droite
    print(" " * (height - 1) + "/")

    # Dessine les lignes du milieu avec des "\" et "/"
    for i in range(height - 2):
        print(" " * (height - i - 2) + "/" + " " * (2*i+1) + "\\")

    # Dessine la dernière ligne avec des traits à droite et à gauche
    print("/" + "_" * (2*height-3) + "\\")


# Appelle la fonction draw_triangle avec height=5
draw_triangle(5)


def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        elif note % 5 >= 3 and note >= 38:
            notes_arrondies.append(note + 5 - note % 5)
        else:
            notes_arrondies.append(note)
    return notes_arrondies


# Exemple d'utilisation
liste_notes = [38, 42, 67, 81, 77, 89]
notes_arrondies = arrondir_notes(liste_notes)
print(notes_arrondies)


#  Job input et boucle while pour trouver le modifié un mot
mot = input("Entrez un mot sans espace ni caractère spécial : ")
n = len(mot)

# Convertir le mot en une liste de caractères pour pouvoir les trier
liste_mot = list(mot)

# Trier les caractères par ordre alphabétique
liste_mot.sort()

# Rechercher le premier caractère différent dans le mot trié
i = 0
while i < n and mot[i] == liste_mot[i]:
    i += 1

if i < n:
    # Si le mot n'était pas déjà le dernier mot possible, échanger le caractère à la position i avec le premier caractère plus grand trouvé dans le mot trié
    j = i + 1
    while j < n and liste_mot[j] <= mot[i]:
        j += 1
    liste_mot[i], liste_mot[j] = liste_mot[j], liste_mot[i]

# Reconstituer le mot à partir de la liste de caractères modifiée
mot_modifie = "".join(liste_mot)

print("Le mot modifié est :", mot_modifie)
