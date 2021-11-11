import doctest
import math
import fltk
import menu

# Variables globales

JEU = {}

# Fonctions d'accès


def est_trace(etat, segment):
    """Fonction prenant en paramètre un dictionnaire "etat"
    et un tuple de tuples "segment" et renvoyant un booléen.
    - si "segment" est tracé, c'est-à-dire si c'est une clé de "etat"
      et que sa valeur est 1, la fonction renvoie True
    - sinon elle renvoie False

    param etat : dict
    param segment : tuple
    return Value : Bool

    >>> est_trace({((1, 1), (2, 1)): 1}, ((1, 1), (2, 1)))
    True
    >>> est_trace({((2, 1), (3, 1)): -1}, ((2, 1), (3, 1)))
    False
    >>> est_trace({}, ((0, 0),(0, 1)))
    False
    """

    if segment in etat:
        if etat[segment] == 1:
            return True
        return False
    return False


def est_interdit(etat, segment):
    """Fonction prenant en paramètre un dictionnaire "etat"
    et un tuple de tuples "segment" et renvoyant un booléen.
    - si "segment" est interdit, c'est-à-dire si c'est une clé de "etat"
      et que sa valeur est -1, la fonction renvoie True
    - sinon elle renvoie False

    param etat : dict
    param segment : tuple
    return Value : Bool

    >>> est_interdit({((2, 1), (3, 1)): -1}, ((2, 1), (3, 1)))
    True
    >>> est_interdit({((1, 1), (2, 1)): 1}, ((1, 1), (2, 1)))
    False
    >>> est_interdit({}, ((0, 0),(0, 1)))
    False
    """

    if segment in etat:
        if etat[segment] == -1:
            return True
        return False
    return False


def est_vierge(etat, segment):
    """Fonction prenant en paramètre un dictionnaire "etat"
    et un tuple de tuples "segment" et renvoyant un booléen.
    - si "segment" est dans état, c'est-à-dire si c'est une clé de "etat",
      la fonction renvoie False
    - sinon elle renvoie True

    param etat : dict
    param segment : tuple
    return Value : Bool

    >>> est_vierge({((1, 1), (2, 1)): 1, ((2, 1), (3, 1)): -1}, ((0, 0), (1, 0)))
    True
    >>> est_vierge({((1, 1), (2, 1)): 1, ((2, 1), (3, 1)): -1}, ((1, 1), (2, 1)))
    False
    >>> est_vierge({}, ((0, 0),(0, 1)))
    True
    """
    if segment not in etat:
        return True
    return False


def tracer_segment(etat, segment):
    """Fonction prenant en paramètre un dictionnaire "etat"
    et un tuple de tuples "segment" puis modifiant "etat" afin de représenter
    le fait que segment est maintenant tracé, c'est-à-dire que "segment"
    devienne une clé de "etat" avec 1 comme valeur.
    On vérifiera que "segment" est bien ordonné avant de l'entrer comme clé.

    param etat : dict
    param segment : tuple
    """

    som1, som2 = segment
    if som1[0] > som2[0] or som1[1] > som2[1]:
        etat[(som2, som1)] = 1
    else:
        etat[segment] = 1


def interdire_segment(etat, segment):
    """Fonction prenant en paramètre un dictionnaire "etat"
    et un tuple de tuples "segment" puis modifiant "etat" afin de représenter
    le fait que segment est maintenant interdit, c'est-à-dire que "segment"
    devienne une clé de "etat" avec -1 comme valeur.
    On vérifiera que "segment" est bien ordonné avant de l'entrer comme clé.

    param etat : dict
    param segment : tuple
    """

    som1, som2 = segment
    if som1[0] > som2[0] or som1[1] > som2[1]:
        etat[(som2, som1)] = -1
    else:
        etat[segment] = -1


def effacer_segment(etat, segment):
    """Fonction prenant en paramètre un dictionnaire "etat"
    et un tuple de tuples "segment" puis modifiant "etat" afin de représenter
    le fait que segment est maintenant vierge, c'est-à-dire que "segment"
    sera supprimé de "etat" s'il s'y trouve.
    On vérifiera que "segment" est bien ordonné avant de modifier "etat".

    param etat : dict
    param segment : tuple
    """

    som1, som2 = segment
    if som1[0] > som2[0] or som1[1] > som2[1]:
        if (som2, som1) in etat:
            del etat[(som2, som1)]
    else:
        if segment in etat:
            del etat[segment]


def segments_traces(etat, sommet):
    """Fonction prenant en paramètre un dictionnaire "etat"
    et un tuple "sommet" puis renvoyant la liste des segments tracés
    adjacents à "sommet" dans "etat", c'est-à-dire la liste des clés de "etat"
    dont "sommet" est un des éléments et la valeur dans "etat" est 1.

    param etat : dict
    param sommet : tuple
    return Value : list

    >>> segments_traces({((1, 1), (2, 1)): 1, ((2, 1), (3, 1)): 1}, (2, 1))
    [((1, 1), (2, 1)), ((2, 1), (3, 1))]
    >>> segments_traces({((1, 1), (1, 2)): -1, ((2, 1), (3, 1)): 1}, (3, 1))
    [((2, 1), (3, 1))]
    >>> segments_traces({((1, 1), (2, 1)): -1, ((2, 1), (3, 1)): -1}, (0, 0))
    []
    """

    i, j = sommet
    lst_seg_adj = [((i - 1, j), (i, j)), ((i, j - 1), (i, j)), ((i, j), (i + 1, j)), ((i, j), (i, j + 1))]
    lst_seg_trac = list()
    for segment in lst_seg_adj:
        if segment in etat:
            if etat[segment] == 1:
                lst_seg_trac.append(segment)
    return lst_seg_trac


def segments_interdits(etat, sommet):
    """Fonction prenant en paramètre un dictionnaire "etat"
    et un tuple "sommet" puis renvoyant la liste des segments interdits
    adjacents à "sommet" dans "etat", c'est-à-dire la liste des clés de "etat"
    dont "sommet" est un des éléments et la valeur dans "etat" est -1.

    param etat : dict
    param sommet : tuple
    return Value : list

    >>> segments_interdits({((1, 1), (2, 1)): -1, ((2, 1), (3, 1)): 1}, (2, 1))
    [((1, 1), (2, 1))]
    >>> segments_interdits({((1, 1), (1, 2)): -1, ((2, 1), (3, 1)): 1}, (3, 1))
    []
    >>> segments_interdits({((0, 0), (1, 0)): -1, ((0, 0), (0, 1)): -1}, (0, 0))
    [((0, 0), (1, 0)), ((0, 0), (0, 1))]
    """

    i, j = sommet
    lst_seg_adj = [((i - 1, j), (i, j)), ((i, j - 1), (i, j)), ((i, j), (i + 1, j)), ((i, j), (i, j + 1))]
    lst_seg_interd = list()
    for segment in lst_seg_adj:
        if segment in etat:
            if etat[segment] == -1:
                lst_seg_interd.append(segment)
    return lst_seg_interd


def segment_dans_grille(segment):
    """
     Fonction qui prend en paramétre une liste de listes "indices" et un tuple de tuples
     "segment" puis il renvoie un booléen qui indique si le segment est bien dans la grille "indices".
    :param indices: list
    :param segment: tuple
    :return: Bool
    """
    for sommet in segment:
        ligne = 0 <= sommet[0] <= JEU["hauteur"]
        colonne = 0 <= sommet[1] <= JEU["largeur"]
        if not ligne or not colonne:
            return False
    return True


def segments_vierges(etat, sommet):
    """Fonction prenant en paramètre une liste de listes "indices" et un
    dictionnaire "etat" et un tuple "sommet" puis renvoyant la liste
    des segments vierge adjacents à "sommet" dans "etat", c'est-à-dire
    la liste des tuples (segment) qui ne sont pas dans etat et dont "sommet"
    est un des éléments.

    param etat : dict
    param sommet : tuple
    return Value : list
    """
    i, j = sommet
    lst_seg_adj = [((i - 1, j), (i, j)), ((i, j - 1), (i, j)), ((i, j), (i + 1, j)), ((i, j), (i, j + 1))]
    lst_seg_vierge = list()
    for segment in lst_seg_adj:
        if segment not in etat and segment_dans_grille(segment) is True:
            lst_seg_vierge.append(segment)
    return lst_seg_vierge


def statut_case(indices, etat, case):
    """Fonction recevant la liste de listes "indices", un dictionnaire "etat"
    et un tuple "case" (les coordonnées d’une case(pas d’un sommet !))
    et renvoyant:
    - None si cette case ne porte aucun indice c'est-à-dire à la position
    de la "case" dans "indices c'est None l'élément;
    – 0 si l’indice est satisfait c'est-à-dire que le nombre de segments
    tracés autour de cette case est égale à l'élément à la position de
    la "case" dans "indices";
    – 1 s’il est encore possible de satisfaire l’indice en traçant
    des segments autour de la case ;
    – -1 s’il n’est plus possible de satisfaire l’indice parce que
    trop de segments sont déjà tracés ou interdits autour de la case.

    param indices : list
    param etat : dict
    param case : tuple
    return Value :  None ou int
    >>> statut_case([[2, 3, None], [1, None, None], [None, 0, 1]], {((1, 1), (2, 1)): 1, ((2, 1), (3, 1)): -1}, (1, 0))
    0
    >>> statut_case([[2, 3, None], [0, None, None], [None, 0, 1]], {((1, 1), (2, 1)): 1, ((2, 1), (3, 1)): -1}, (1, 0))
    -1
    >>> statut_case([[2, 3, None], [3, None, None], [None, 0, 1]], {((1, 1), (2, 1)): 1, ((2, 1), (3, 1)): -1}, (1, 0))
    1
    """
    i, j = case
    indice = indices[i][j]
    if indice is None:
        return None
    else:
        lst_seg_adj = [((i, j), (i, j + 1)), ((i, j), (i + 1, j)), ((i + 1, j), (i + 1, j + 1)),
                       ((i, j + 1), (i + 1, j + 1))]
        cmp_val_trac = 0
        cmp_val_vierge = 0
        for segment in lst_seg_adj:
            if segment in etat:
                if etat[segment] == 1:
                    cmp_val_trac += 1
            else:
                cmp_val_vierge += 1
        if cmp_val_trac == indice:
            return 0
        elif cmp_val_trac < indice and cmp_val_trac + cmp_val_vierge >= indice:
            return 1
        else:
            return -1


# Conditions de victoire

def indices_satisfaits(indices, etat):
    """Fonction prenant la liste de listes "indices" et le dictionnaire "etat"
    en paramètre puis éffectuant le rôle de la fonction 'statut_case'
    sur toutes les cases de la grille et renvoyant un booléen:
    - True si toutes les cases sont satisfaites
    - False sinon

    param indices : list
    param etat : dict
    return Value : Bool

    >>> indices_satisfaits([[2, 3, None], [3, None, None], [None, 0, 1]], {((1, 1), (2, 1)): 1, ((2, 1), (3, 1)): -1})
    False
    >>> indices_satisfaits([[0, 0, None], [1, None, None], [None, 0, 0]], {((1, 1), (2, 1)): 1, ((2, 1), (3, 1)): -1})
    True
    >>> indices_satisfaits([[1, 0, None], [1, None, None]], {((0, 0), (0, 1)): 1, ((1, 1), (2, 1)): 1})
    True
    """

    for ligne in range(len(indices)):
        for colonne in range(len(indices[ligne])):
            satisfaction = statut_case(indices, etat, (ligne, colonne))
            if satisfaction == 1 or satisfaction == -1:
                return False
    return True


def construction_boucle(etat, depart, precedent, courant, nb_seg=1):
    """Fonction récursive prenant le dictionnaire "etat", trois tuples
    "depart", "precedent", "courant", et un compteur "nb_seg" en paramètre
    et renvoyant:
    - None si le tracé des segments ne forme pas une boucle
    - "nb_seg" si il forme bien une boucle, "nb_seg" serait alors
      dans ce cas le nombre de segments constituant cette boucle.

    param etat : dict
    param depart : tuple
    param precedent : tuple
    param courant : tuple
    param facultatif nb_seg : int
    return Value : None ou int
    >>> etat = {((1, 0), (2, 0)): 1,
    ...          ((1, 0), (1, 1)): 1,
    ...          ((2, 0), (2, 1)): 1,
    ...          ((1, 1), (1, 2)): 1,
    ...          ((2, 1), (2, 2)): 1,
    ...          ((1, 2), (2, 2)): 1}
    >>> construction_boucle(etat, (1, 0), (1, 0), (2, 0), nb_seg=1)
    6
    """

    if depart == courant:
        return nb_seg
    else:
        seg_trac = segments_traces(etat, courant)
        if len(seg_trac) != 2:
            return None
        else:
            for seg in seg_trac:
                if precedent not in seg:
                    sommet1, sommet2 = seg
                    if sommet1 == courant:
                        precedent = courant
                        courant = sommet2
                    else:
                        precedent = courant
                        courant = sommet1
            return construction_boucle(etat, depart, precedent, courant, nb_seg + 1)


def longueur_boucle(etat, segment):
    """Fonction prenant le dictionnaire "etat" et un tuple de tuples "segment"
    et renvoyant None si le segment n’appartient pas à une boucle,
    et la longueur de la boucle à laquelle il appartient sinon

    param etat : dict
    parm segment : tuple
    return Value : None ou int

    >>> etat = {((1, 0), (2, 0)): 1,
    ...          ((1, 0), (1, 1)): 1,
    ...          ((2, 0), (2, 1)): 1,
    ...          ((1, 1), (1, 2)): 1,
    ...          ((2, 1), (2, 2)): 1,
    ...          ((1, 2), (2, 2)): 1}
    >>> longueur_boucle(etat, ((1, 0), (2, 0)))
    6
    """

    depart, courant = segment
    return construction_boucle(etat, depart, depart, courant)


def nb_segment_trace(etat):
    """Fonction prenant le dictionnaire "etat" et comptant le nombre des
    clés ayant 1  comme valeur (segments tracés) puis renvoyant ce nombre
    et le dernier des clés avec la valeur 1

    param etat : dict
    return Value : tuple (int, tuple de tuples)
    >>> etat = {((1, 0), (2, 0)): 1,
    ...          ((1, 0), (1, 1)): 1,
    ...          ((2, 0), (2, 1)): 1,
    ...          ((1, 1), (1, 2)): 1,
    ...          ((2, 1), (2, 2)): 1,
    ...          ((1, 2), (2, 2)): 1}
    >>> nb_segment_trace(etat)
    (6, ((1, 2), (2, 2)))
    >>> nb_segment_trace({((1, 1), (2, 1)): -1, ((2, 1), (3, 1)): 1})
    (1, ((2, 1), (3, 1)))
    >>> nb_segment_trace({((1, 1), (2, 1)): -1, ((2, 1), (3, 1)): 1, ((0, 0), (0, 1)): 1})
    (2, ((0, 0), (0, 1)))
    """

    nb_seg = 0
    for segment in etat:
        if etat[segment] == 1:
            nb_seg += 1
            seg_depart = segment
    return nb_seg, seg_depart


def fin_partie(indices, etat):
    """Fonction prenant en parametre la liste de listes "indices" et
    le dictionnaire "etat" et vérifie si la partie est finie en renvoyant
    un booléen.
    Elle affiche aussi un message sur la console indiquant le statut
    de chacune des deux conditions de victoires à chaque boucle de jeu.

    param indices : list
    param etat : dict
    return Value : Bool

    >>> etat = {((1, 0), (2, 0)): 1,
    ...          ((1, 0), (1, 1)): 1,
    ...          ((2, 0), (2, 1)): 1,
    ...          ((1, 1), (1, 2)): 1,
    ...          ((2, 1), (2, 2)): 1,
    ...          ((1, 2), (2, 2)): 1}
    >>> indices = [[1, None], [3, 3]]
    >>> fin_partie(indices, etat)
    Indices satisfaits : True.
    Boucle unique: True.
    True
    """
    allsatisfaction = indices_satisfaits(indices, etat)
    nb_seg_trac, segment = nb_segment_trace(etat)
    longueur_boucl = longueur_boucle(etat, segment)
    if not allsatisfaction:
        print("Indices satisfaits : False.")
        if longueur_boucl is None:
            print("Boucle unique: False.")
        if longueur_boucl == nb_seg_trac:
            print("Boucle unique: True.")
    else:
        print("Indices satisfaits : True.")
        if longueur_boucl is None:
            print("Boucle unique: False.")
        if longueur_boucl == nb_seg_trac:
            print("Boucle unique: True.")
            return True
    return False


# Interface graphique

# DETECTE DES CLICS
def coord_som(indice, jeu):
    """Fonction prenant un entier indice et un dictionnaire "jeu"
    et renvoyant une coordonnée correspondante dans la grille

    param indice : int
    param jeu : dict
    return Value : int

    >>> coord_som(3, {'taille_case': 100, 'marge': 20})
    320
    >>> coord_som(0, {'taille_case': 50, 'marge': 10})
    10
    """
    return indice * jeu["taille_case"] + jeu["marge"]


def index_som(coord, jeu):
    """Fonction prenant un entier coord et un dictionnaire "jeu"
    et renvoyant un float selon la taille des cases et la marge de la grille

    param indice : int
    param jeu : dict
    return Value : float

    >>> index_som(320, {'taille_case': 100, 'marge': 20})
    3.0
    >>> index_som(10, {'taille_case': 50, 'marge': 10})
    0.0
    >>> index_som(246, {'taille_case': 100, 'marge': 20})
    2.26
    """
    return (coord - jeu["marge"]) / jeu["taille_case"]


def distance(sommet1, sommet2):
    """Fonction prenant des tuples sommet1 et sommet2 représentant des points
    puis calculant la distance entre ces deux points avant de le retourner

    param sommet1 : tuple
    param sommet2 : tuple
    return Value : float
    """
    carre = math.pow(sommet1[0] - sommet2[0], 2) + math.pow(sommet1[1] - sommet2[1], 2)
    return math.sqrt(carre)


def proximite(x, y, jeu):
    """Fonction prenant en paramètre deux entiers x, y (symbolisant
    les coordonnés d'un clic),  le dictionnaire jeu puis vérifie si
    le clic a été fait aux alentours d'un sommet de la grille. et si oui,
    renvoie une liste dont le premier element est ce sommet et le second
    la liste des sommets potentiels correspondant au segment recherché.

    param x : int
    param y : int
    param jeu: dict
    return value : list or None
    """
    dx = index_som(x, jeu)
    rdx = round(dx)
    dy = index_som(y, jeu)
    rdy = round(dy)
    if 0 > rdy or rdy > jeu["hauteur"] or 0 > rdx or rdx > jeu["largeur"]:
        return None
    proche_vert = -0.2 <= dx - rdx <= 0.2
    proche_hori = -0.2 <= dy - rdy <= 0.2

    if proche_vert and abs(dx - rdx) < abs(dy - rdy):
        return [(rdy, rdx), [(rdy - 1, rdx), (rdy + 1, rdx)]]

    elif proche_hori and abs(dy - rdy) < abs(dx - rdx):
        return [(rdy, rdx), [(rdy, rdx - 1), (rdy, rdx + 1)]]

    else:
        return None


def clic_left(x, y, jeu):
    """Fonction prenant en paramètre deux entiers x, y (symbolisant
    les coordonnés d'un clic),  le dictionnaire jeu et se chargeant de
    modifier la clé 'etat' de 'jeu' en y ajoutant ou en retirant un segment
    selon le vouloir de l'utilisateur si son clic est aux environs du segment

    param x : int
    param y : int
    param jeu : dict
    """
    proximitee = proximite(x, y, JEU)
    if proximitee is not None:
        sommet1 = proximitee[0]
        voisins_logiques = proximitee[1]
        for sommet2 in voisins_logiques:
            if 0 > sommet2[0] or sommet2[0] > jeu["hauteur"] or 0 > sommet2[1] or sommet2[1] > jeu["largeur"]:
                continue
            elif distance((y, x), (coord_som(sommet2[0], jeu), coord_som(sommet2[1], jeu))) < jeu["taille_case"] + 2:
                if sommet1[0] > sommet2[0] or sommet1[1] > sommet2[1]:
                    segment = (sommet2, sommet1)
                else:
                    segment = (sommet1, sommet2)

                if segment in jeu["etat"]:
                    effacer_segment(jeu["etat"], segment)
                else:
                    tracer_segment(jeu["etat"], segment)
                break


def clic_right(x, y, jeu):
    """Fonction prenant en paramètre deux entiers x, y (symbolisant
    les coordonnés d'un clic),  le dictionnaire jeu et se chargeant de
    modifier la clé 'etat' de 'jeu' en y ajoutant ou en retirant un segment
    selon le vouloir de l'utilisateur si son clic est aux environs du segment

    param x : int
    param y : int
    param jeu : dict
    """
    proximitee = proximite(x, y, JEU)
    if proximitee is not None:
        sommet1 = proximitee[0]
        voisins_logiques = proximitee[1]
        for sommet2 in voisins_logiques:
            if 0 > sommet2[0] or sommet2[0] > jeu["hauteur"] or 0 > sommet2[1] or sommet2[1] > jeu["largeur"]:
                continue
            elif distance((y, x), (coord_som(sommet2[0], jeu), coord_som(sommet2[1], jeu))) < jeu["taille_case"] + 2:
                if sommet1[0] > sommet2[0] or sommet1[1] > sommet2[1]:
                    segment = (sommet2, sommet1)
                else:
                    segment = (sommet1, sommet2)

                if segment in jeu["etat"]:
                    effacer_segment(jeu["etat"], segment)
                else:
                    interdire_segment(jeu["etat"], segment)
                break


def dessine_pts_grille(jeu):
    """Fonction prenant en paramètre le dictionnaire jeu et dessinant les
    points de la grille sur la fenêtre
    """
    for m in range(jeu["hauteur"] + 1):
        for n in range(jeu["largeur"] + 1):
            fltk.point(coord_som(n, jeu), coord_som(m, jeu), couleur="black", epaisseur=2)


def dessine_indice(jeu):
    """Fonction prenant en paramètre le dictionnaire jeu et dessinant les
    indices dans leur case respectif avec une couleur spécifique selon le
    statut de la case dans l'avancée du jeu sur la fenêtre.
    cette couleur est:
    - Noire si la case a encore la possibilité d'être satisfaite en traçant
      des segments autour dela case
    - Bleu si elle est satisfaite
    - Rouge si s’il n’est plus possible de satisfaire l’indice parce que
      trop de segments sont déjà tracés ou interdits autour de la case

    param jeu : dict
    """
    for m in range(len(jeu["indices"])):
        for n in range(len(jeu["indices"][m])):
            case = m, n
            statut = statut_case(jeu["indices"], jeu["etat"], case)
            if statut is None:
                continue
            elif statut == 0:
                fltk.texte(coord_som(n, jeu) + jeu["taille_case"] / 2, coord_som(m, jeu) + jeu["taille_case"] / 2,
                           f"{jeu['indices'][m][n]}", couleur='blue', ancrage='center',
                           taille=30, tag='etat')
            elif statut == 1:
                fltk.texte(coord_som(n, jeu) + jeu["taille_case"] / 2, coord_som(m, jeu) + jeu["taille_case"] / 2,
                           f"{jeu['indices'][m][n]}", couleur='black', ancrage='center',
                           taille=30, tag='etat')
            elif statut == -1:
                fltk.texte(coord_som(n, jeu) + jeu["taille_case"] / 2, coord_som(m, jeu) + jeu["taille_case"] / 2,
                           f"{jeu['indices'][m][n]}", couleur='red', ancrage='center',
                           taille=30, tag='etat')


def dessine_segments(jeu):
    """Fonction prenant le dictionnaire jeu et dessinant les segments tracés
    et interdits contenus dans le dictionnaire 'etat' de 'jeu'

    param jeu : dict
    """
    for seg in jeu["etat"]:
        som1, som2 = seg
        if jeu["etat"][seg] == 1:
            fltk.ligne(coord_som(som1[1], jeu), coord_som(som1[0], jeu), coord_som(som2[1], jeu),
                       coord_som(som2[0], jeu), epaisseur=5, tag='etat')
        else:
            point = (coord_som((som1[0] + som2[0]) / 2, jeu), coord_som((som1[1] + som2[1]) / 2, jeu))
            fltk.texte(point[1], point[0], 'x', couleur='red', ancrage='center', taille=10, tag='etat')


def dessine_grille(jeu):
    """Fonction gérant l'affichage de toutes les éléments de la grille de jeu

    param jeu : dict
    """
    dessine_pts_grille(jeu)
    dessine_indice(jeu)
    dessine_segments(jeu)


# SOLVEUR

def exces_indice(indices, etat):
    """
    verifie qu’il n’y a pas un excés de segments dans la grille ("pour toutes les cases de la grille")
    :param indices: list
    :param etat: dict
    :return: Bool
    """
    for ligne in range(len(indices)):
        for colonne in range(len(indices[ligne])):
            satisfaction = statut_case(indices, etat, (ligne, colonne))
            if satisfaction == -1:
                return True
    return False


def cherche_sommets(indices):
    """
    La fonction qui renvoie les sommets de depart de l'algoritme et si il n'y a pas d'indices dans la grille il renvoie "None".
    :param indices: list
    :return: list or None
    """
    for ligne in range(len(indices)):
        for colonne in range(len(indices[ligne])):
            if indices[ligne][colonne] == 3:
                return [(ligne, colonne)]
            elif indices[ligne][colonne] == 2 or indices[ligne][colonne] == 1:
                return [(ligne, colonne), (ligne + 1, colonne + 1)]
    return None


def cherche_solution(indices, etat, sommet):
    """
    Fonction qui implemente l'algorithme du solveur en commencant d'un sommet et à chaque fois dessiner des segments jusqu'à arriver à une boucle unique fermer et il renvoie un booléan qui indique si on peut arriver à faire une boucle fermer en satisfaisant tous les cases.
    :param indices: list
    :param etat: dict
    :param sommet: tuple
    :return: Bool
    """
    lst_seg_trac = segments_traces(etat, sommet)
    if len(lst_seg_trac) == 2:
        if indices_satisfaits(indices, etat) is True:
            return True
        else:
            return False
    elif len(lst_seg_trac) > 2:
        return False
    elif len(lst_seg_trac) < 2:
        for segment in segments_vierges(etat, sommet):
            tracer_segment(etat, segment)

            if exces_indice(indices, etat) is True:
                effacer_segment(etat, segment)
                continue
            if sommet == segment[0]:
                appel = cherche_solution(indices, etat, segment[1])
            else:
                appel = cherche_solution(indices, etat, segment[0])
            if appel is True:
                dessine_solveur(etat)
                return appel
            elif appel == 'escape':
                return appel
            else:
                effacer_segment(etat, segment)

            ev = fltk.attend_ev()
            if fltk.touche(ev) == 'Escape':
                return 'escape'
            elif fltk.touche(ev) == 'space':
                dessine_solveur(etat)
            else:
                continue


def si_grille_valide(indices, etat):
    """
    Fonction qui renvoie un booléan qui indique si la grille et valide ou pas en utilisant les fonctions d'avant
    :param indices: list
    :param etat: dict
    :return: Bool
    """
    sommets = cherche_sommets(indices)
    if sommets is None:
        return False
    for sommet in sommets:
        solution = cherche_solution(indices, etat, sommet)
        if solution is True:
            print(etat)
            return True
    return False


def dessine_seg_solveur(solveur):
    """Fonction qui reçoit un dictionnaire qui ressemble à celui de la variable "etat" qui définit le jeu mais
    dans ce cas il definit celui du solveur, et en fonction de la valeur associer à chaque segment il trace soit un
    segment tracé soit un segment interdit dans l'interface graphique

    :param solveur: dict
    """
    for seg in solveur:
        som1, som2 = seg
        if solveur[seg] == 1:
            fltk.ligne(coord_som(som1[1], JEU), coord_som(som1[0], JEU), coord_som(som2[1], JEU),
                       coord_som(som2[0], JEU), epaisseur=5)
        else:
            point = (coord_som((som1[0] + som2[0]) / 2, JEU), coord_som((som1[1] + som2[1]) / 2, JEU))
            fltk.texte(point[1], point[0], 'x', couleur='red', ancrage='center', taille=10)


def draw_indice_solveur(jeu):
    """Fonction qui reçoit un dictionnaire "jeu" contenant toutes les informations du jeu inclus la listes des indices,
    et en fonction de chaque indice de la grille il il détecte s’il est satisfait pour le tracé en Bleu, et s'ils n'est
    pas encore satisfait pour le tracé  en Noir, et en rouge s'ils n'est plus possible de le satisfaire.

    :param jeu: dict
    """
    for m in range(len(jeu["indices"])):
        for n in range(len(jeu["indices"][m])):
            case = m, n
            statut = statut_case(jeu["indices"], jeu["Solveur"], case)
            if statut is None:
                continue
            elif statut == 0:
                fltk.texte(coord_som(n, jeu) + jeu["taille_case"] / 2, coord_som(m, jeu) + jeu["taille_case"] / 2,
                           f"{jeu['indices'][m][n]}", couleur='blue', ancrage='center',
                           taille=30, tag='solveur')
            elif statut == 1:
                fltk.texte(coord_som(n, jeu) + jeu["taille_case"] / 2, coord_som(m, jeu) + jeu["taille_case"] / 2,
                           f"{jeu['indices'][m][n]}", couleur='black', ancrage='center',
                           taille=30, tag='solveur')
            elif statut == -1:
                fltk.texte(coord_som(n, jeu) + jeu["taille_case"] / 2, coord_som(m, jeu) + jeu["taille_case"] / 2,
                           f"{jeu['indices'][m][n]}", couleur='red', ancrage='center',
                           taille=30, tag='solveur')


def dessine_solveur(solveur):
    """Fonction qui reçoit le dictionnaire etat du "solveur" et qui appelle toutes les fonctions nécessaire pour tracé les
    segments du solveur et les indices de la grille dans l'interface graphique

    :param solveur: dict
    """
    fltk.efface_tout()
    dessine_grille(JEU)
    menu.menu_right(JEU)
    fltk.efface('etat')
    dessine_seg_solveur(solveur)
    draw_indice_solveur(JEU)
    fltk.mise_a_jour()


# ============================================================================
if __name__ == '__main__':
    print(doctest.testmod())

    # =========================================GAME===========================

    JEU["Game"] = False  # Variable initialisant la boucle du jeu
    JEU["Solveur"] = {}
    menu.menu_start(JEU)

    # Variables servant à l'affichage du menu des informations
    center_right = JEU["taille_case"] * JEU["largeur"] + 2 * JEU["marge"] + 100
    y_fin = JEU["taille_case"] * JEU["hauteur"] + 2 * JEU["marge"]
    Solveur = [(center_right - 90, y_fin - 60), (center_right + 90, y_fin - 10)]

    # création de la fenêtre de jeu
    fltk.cree_fenetre(JEU["largeur"] * JEU["taille_case"] + 2 * JEU["marge"] + 200, \
                      JEU["hauteur"] * JEU["taille_case"] + 2 * JEU["marge"])

    while not JEU["Game"]:

        dessine_grille(JEU)
        menu.menu_right(JEU)
        fltk.mise_a_jour()
        ev = fltk.attend_ev()
        ty = fltk.type_ev(ev)

        if ty == 'ClicGauche':
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)

            if Solveur[0][0] < x < Solveur[1][0] and \
               Solveur[0][1] < y < Solveur[1][1]:  # lancement du solveur
                JEU["Grille"] = si_grille_valide(JEU["indices"], JEU["Solveur"])
                print(JEU["Grille"])  # True si grille valide, False sinon
                if JEU["Grille"]:
                    print(JEU["Solveur"])
                    # Affichage des segments de la validation de la grille

                ev = fltk.attend_ev()
                while fltk.touche(ev) != 'Return':
                    ev = fltk.attend_ev()

            clic_left(x, y, JEU)  # tracer ou supprimer un segment

        elif ty == 'ClicDroit':
            x, y = fltk.abscisse(ev), fltk.ordonnee(ev)

            clic_right(x, y, JEU)  # interdire ou supprimer un segment

        elif ty == 'Quitte':  # Abandon de la partie

            fltk.ferme_fenetre
            menu.sauvegarde_etat(JEU, "etatdoc.txt")
            menu.sauvegarde_grille(JEU, "grilledoc.txt")
            break

        if len(JEU["etat"]) >= 1:  # vérification de la grille
            JEU["Game"] = fin_partie(JEU["indices"], JEU["etat"])
        fltk.efface_tout()

        if JEU["Game"]:  # Jeu terminée, Boucle de segments formée
            dessine_grille(JEU)
            menu.menu_final(JEU)

            if not JEU["Game"]:
                print("new JEU : ", JEU)
                center_right = JEU["taille_case"] * JEU["largeur"] + 2 * JEU["marge"] + 100
                y_fin = JEU["taille_case"] * JEU["hauteur"] + 2 * JEU["marge"]
                Solveur = [(center_right - 90, y_fin - 60), (center_right + 90, y_fin - 10)]

                fltk.cree_fenetre(JEU["largeur"] * JEU["taille_case"] + 2 * JEU["marge"] + 200, \
                                  JEU["hauteur"] * JEU["taille_case"] + 2 * JEU["marge"])
