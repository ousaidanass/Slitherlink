import fltk

# Menus


def sauvegarde_grille(jeu, grilledoc):
    """Fontion qui prend en paramétre le dictionnaire jeu et le fichier
    grilledoc et sauvegarde la liste des indices du jeu dans le fichier
    grilledoc

    :param jeu: dict
    :param grilledoc: file
    """
    grille = []
    for lignes in jeu["indices"]:
        ligne = []
        grille.append(ligne)
        for ind in lignes:
            if ind is None:
                ligne.append('_')
            else:
                ligne.append(str(ind))
    p = open(grilledoc, 'w')
    for i in grille:
        x = "".join(i)
        p.write(x + '\n')


def restauration_grille(jeu, grilledoc):
    """Fontion qui prend en paramétre le dictionnaire jeu et le fichier
    grilledoc puis restaure la liste des indices du jeu contenue dans le
    fichier grilledoc et de celle-ci initialise la hauteur et la largeur
    de la grille de jeu

    :param jeu: dict
    :param grilledoc: file
    """
    indices = []
    p = open(grilledoc, 'r')
    grille = []
    for ligne in p:
        grille.append(ligne)
    for lignes in grille:
        case = []
        indices.append(case)
        for s in lignes:
            if s == '\n':
                break
            elif s == '_':
                ind = None
            else:
                ind = int(s)
            case.append(ind)
    jeu["hauteur"] = len(indices)
    jeu["largeur"] = len(indices[0])
    jeu["indices"] = indices


def sauvegarde_etat(jeu, etatdoc):
    """Fontion qui prend en paramétre le dictionnaire jeu et le fichier
    etatdoc et sauvegarde le dictionnaire etat du jeu dans le fichier etatdoc

    :param jeu: dict
    :param etatdoc: file
    """
    lst_etat = []
    for lignes in jeu["etat"]:
        ligne = []
        seg = str(lignes)
        ligne.append(seg[2] + ' ' + seg[5] + ' ' + seg[10] + ' ' + seg[13] + ' ' + str(jeu["etat"][lignes]))
        lst_etat.append(ligne)
    p = open(etatdoc, 'w')
    for i in lst_etat:
        x = "".join(i)
        p.write(x + '\n')
    pass


def restauration_etat(jeu, etatdoc):
    """Fontion qui prend en paramétre le dictionnaire jeu et le fichier
    etatdoc et restaure le dictionnaire etat du jeu contenu dans le
    fichier etatdoc

    :param jeu: dict
    :param etatdoc: file
    """
    etat = {}
    p = open(etatdoc, 'r')
    lst_seg = []
    for lignes in p:
        lst_seg.append(lignes[:-1])

    for el in lst_seg:
        som1 = int(el[0]), int(el[2])
        som2 = int(el[4]), int(el[6])
        valeur = int(el[8:])
        etat[(som1, som2)] = valeur
    jeu["etat"] = etat


def nb_seg_trac_interd(etat):
    """Fonction prenant le dictionnaire "etat" et comptant le nombre des
    clés ayant -1  comme valeur (segments interdits) et le nombre des
    clés ayant 1  comme valeur (segments tracés)

    param etat : dict
    return Value : tuple
    """

    nb_seg_trac = 0
    nb_seg_interd = 0
    for segment in etat:
        if etat[segment] == 1:
            nb_seg_trac += 1
        else:
            nb_seg_interd += 1
    return nb_seg_trac, nb_seg_interd


def menu_choice(jeu):
    """Fonction gérant le menu de choix de la grille de jeu.

    param jeu : dict
    """

    fltk.texte(400, 80, 'CHOIX DE LA GRILLE', couleur="chartreuse",\
               taille=50, ancrage='center', tag='menu_jeu')
    fltk.rectangle(30, 30, 770, 130, couleur="blue", epaisseur=3, tag="menu_jeu")

    grille1 = [(100, 150), (300, 250)]
    fltk.rectangle(grille1[0][0], grille1[0][1], grille1[1][0], grille1[1][1],\
                   couleur="blue", remplissage="blue", epaisseur=3, tag="menu_jeu")
    fltk.texte(200, 200, 'GRILLE 6x6', couleur="chartreuse",\
               taille=20, ancrage='center', tag='menu_jeu')

    grille2 = [(500, 150), (700, 250)]
    fltk.rectangle(grille2[0][0], grille2[0][1], grille2[1][0], grille2[1][1], \
                   couleur="blue", remplissage="blue", epaisseur=3, tag="menu_jeu")
    fltk.texte(600, 200, 'GRILLE 5x5', couleur="chartreuse", \
               taille=20, ancrage='center', tag='menu_jeu')

    grille3 = [(50, 300), (350, 400)]
    fltk.rectangle(grille3[0][0], grille3[0][1], grille3[1][0], grille3[1][1], \
                   couleur="blue", remplissage="blue", epaisseur=3, tag="menu_jeu")
    fltk.texte(200, 350, 'GRILLE TRIVIALE 2x2', couleur="chartreuse", \
               taille=20, ancrage='center', tag='menu_jeu')

    grille4 = [(450, 300), (750, 400)]
    fltk.rectangle(grille4[0][0], grille4[0][1], grille4[1][0], grille4[1][1], \
                   couleur="blue", remplissage="blue", epaisseur=3, tag="menu_jeu")
    fltk.texte(600, 350, 'GRILLE VIDE 4x4', couleur="chartreuse", \
               taille=20, ancrage='center', tag='menu_jeu')

    grille5 = [(300, 450), (500, 550)]
    fltk.rectangle(grille5[0][0], grille5[0][1], grille5[1][0], grille5[1][1], \
                   couleur="blue", remplissage="blue", epaisseur=3, tag="menu_jeu")
    fltk.texte(400, 500, 'GRILLEDOC', couleur="chartreuse", \
               taille=20, ancrage='center', tag='menu_jeu')

    new_clic = fltk.attend_clic_gauche()
    lst_grilles = [grille1, grille2, grille3, grille4, grille5]
    grilles = ['grille1.txt', 'grille2.txt', 'grille-triviale.txt', 'grille-vide.txt', 'new-grille.txt']
    for i in range(len(lst_grilles)):
        if lst_grilles[i][0][0] <= new_clic[0] and new_clic[0] <= lst_grilles[i][1][0] and \
                lst_grilles[i][0][1] <= new_clic[1] and new_clic[1] <= lst_grilles[i][1][1]:
            grille = grilles[i]
            restauration_grille(jeu, grille)
            jeu['etat'] = {}
            fltk.ferme_fenetre()
            break
        else:
            if i == len(lst_grilles) - 1:
                fltk.ferme_fenetre()
                menu_start(jeu)


def menu_start(jeu, grilledoc="grilledoc.txt", etatdoc="etatdoc.txt"):
    """Fonction gérant le menu de démarrage du jeu donnant le choix à l'utilisateur de
    débuter une nouvelle partie ou de restaurer la partie sauvegardée

    param jeu : dict
    param grilledoc : file
    param etatdoc : file
    """
    fltk.cree_fenetre(800, 600)
    fltk.rectangle(0, 0, 1000, 800, couleur='white', remplissage='crimson', \
                   epaisseur=1, tag='menu_jeu')

    fltk.texte(400, 80, 'SLITHERLINK', couleur="chartreuse", \
               taille=50, ancrage='center', tag='menu_jeu')
    fltk.rectangle(150, 30, 650, 130, couleur="blue", epaisseur=3, tag="menu_jeu")

    Bouton_NouvellePartie = [(200, 200), (600, 300)]
    fltk.rectangle(Bouton_NouvellePartie[0][0], Bouton_NouvellePartie[0][1], \
                   Bouton_NouvellePartie[1][0], Bouton_NouvellePartie[1][1], couleur="blue", \
                   remplissage="blue", epaisseur=3, tag="menu_jeu")
    fltk.texte(400, 250, "Nouvelle Partie", couleur='yellow', taille=20, \
               ancrage='center', tag="menu_jeu")

    Bouton_Restauration_partie = [(200, 400), (600, 500)]
    fltk.rectangle(Bouton_Restauration_partie[0][0], Bouton_Restauration_partie[0][1], \
                   Bouton_Restauration_partie[1][0], Bouton_Restauration_partie[1][1], \
                   couleur="blue", remplissage="blue", epaisseur=3, tag="menu_jeu")
    fltk.texte(400, 450, "Restaurer Partie", couleur='yellow', taille=20, \
               ancrage='center', tag="menu_jeu")

    clique = fltk.attend_clic_gauche()
    jeu["taille_case"] = 100
    jeu["marge"] = 20

    if Bouton_NouvellePartie[0][0] <= clique[0] and clique[0] <= Bouton_NouvellePartie[1][0] and \
            Bouton_NouvellePartie[0][1] <= clique[1] and clique[1] <= Bouton_NouvellePartie[1][1]:
        fltk.efface_tout()
        menu_choice(jeu)

    elif Bouton_Restauration_partie[0][0] <= clique[0] and clique[0] <= Bouton_Restauration_partie[1][0] and \
            Bouton_Restauration_partie[0][1] <= clique[1] and clique[1] <= Bouton_Restauration_partie[1][1]:
        restauration_grille(jeu, grilledoc)
        restauration_etat(jeu, etatdoc)
        fltk.ferme_fenetre()


def menu_right(jeu):
    """Fonction affichant l'avancée du jeu

    param jeu : dict
    """

    center_right = jeu["taille_case"] * jeu["largeur"] + 2 * jeu["marge"] + 100
    y_fin = jeu["taille_case"] * jeu["hauteur"] + 2 * jeu["marge"]
    seg_trac, seg_inter = nb_seg_trac_interd(jeu["etat"])
    fltk.rectangle(center_right - 99, 0, center_right + 99, y_fin - 1,
                   couleur='white', remplissage='silver')
    fltk.texte(center_right, 20, "SLITHERLINK", couleur='cyan', ancrage='center',
               taille=20, tag='indices')
    fltk.texte(center_right, 80, f"Segments tracées : {seg_trac}", couleur='blue', ancrage='center',
               taille=10, tag='indices')
    fltk.texte(center_right, 110, f"segments interdits : {seg_inter}", couleur='red', ancrage='center',
               taille=10, tag='indices')

    fltk.rectangle(center_right - 90, y_fin - 60, center_right + 90, y_fin - 10, remplissage='white')
    fltk.texte(center_right, y_fin - 35, "Solveur", couleur='blue', ancrage='center',
               taille=20, tag='indices')


def menu_final(jeu):
    """Fonction affichant le menu final lors de la fin de la partie quand la grille et résolue

    param jeu : dict
    """
    center_right = jeu["taille_case"] * jeu["largeur"] + 2 * jeu["marge"] + 100
    y_fin = jeu["taille_case"] * jeu["hauteur"] + 2 * jeu["marge"]
    seg_trac, seg_inter = nb_seg_trac_interd(jeu["etat"])
    fltk.rectangle(center_right - 99, 0, center_right + 99, y_fin - 1,
                   couleur='white', remplissage='silver')
    fltk.texte(center_right, 20, "SLITHERLINK", couleur='cyan', ancrage='center',
               taille=20, tag='indices')
    fltk.texte(center_right, 60, "Grille résolue", couleur='blue', ancrage='center',
               taille=20, tag='indices')
    fltk.texte(center_right, 90, f"Segments tracées : {seg_trac}", couleur='blue', ancrage='center',
               taille=10, tag='indices')

    start = [(center_right - 90, y_fin - 120), (center_right + 90, y_fin - 70)]
    fltk.rectangle(start[0][0], start[0][1], start[1][0], start[1][1], remplissage='white')
    fltk.texte(center_right, y_fin - 95, "MENU PRINCIPAL", couleur='black', ancrage='center',
               taille=15, tag='indices')
    ferme = [(center_right - 90, y_fin - 60), (center_right + 90, y_fin - 10)]
    fltk.rectangle(ferme[0][0], ferme[0][1], ferme[1][0], ferme[1][1], remplissage='white')
    fltk.texte(center_right, y_fin - 35, "QUITTER", couleur='black', ancrage='center',
               taille=20, tag='indices')

    clic = False
    while not clic:
        x, y = fltk.attend_clic_gauche()
        if start[0][0] < x < start[1][0] and start[0][1] < y < start[1][1]:
            fltk.ferme_fenetre()
            menu_start(jeu)
            jeu["Game"] = False
            clic = True
        elif ferme[0][0] < x < ferme[1][0] and ferme[0][1] < y < ferme[1][1]:
            fltk.ferme_fenetre()
            clic = True
