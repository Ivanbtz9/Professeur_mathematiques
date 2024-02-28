import random as rd

def lancer_une_piece_equilibree():
    k = rd.randint(0,1)
    return k

def lancer_une_piece_truquee():
    k = rd.randint(1,5)
    if k <= 4:
        return 0
    else:
        return 1


def frequence(n): #n est le nombre de lancers
    compteur1 = 0
    compteur2 =  0
    for i in range(n):
        a= lancer_une_piece_equilibree()
        b = lancer_une_piece_truquee()
        if a==1:
            compteur1 +=1
        if b==1:
            compteur2 +=1
    frequence1 = compteur1/n
    frequence2 = compteur2/n
    return [frequence1,frequence2]

def repetition_2_lancers_equilibrees():
    p1 = lancer_une_piece_equilibree()
    p2 = lancer_une_piece_equilibree()
    #p3 = lancer_une_piece_equilibree()
    somme = p1+p2
    return somme

def repetition_2_lancers_truques():
    p1 = lancer_une_piece_truquee()
    p2 = lancer_une_piece_truquee()
    #p3 = lancer_une_piece_truquee()
    somme = p1+p2
    return somme

def frequence_2_pieces_equilibrees(n): #n est le nombre de fois que nous répétons cette expérience
    compteur0 = compteur1=compteur2=0
    for i in range(n):
        a= repetition_2_lancers_equilibrees()
        if a==0:
            compteur0 +=1
        elif a==1:
            compteur1 +=1
        else:
            compteur2+=1
    frequence0 = compteur0/n
    frequence1 = compteur1/n
    frequence2 = compteur2/n
    return [frequence0, frequence1,frequence2]


def frequence_2_pieces_truquees(n): #n est le nombre de fois que nous répétons cette expérience
    compteur0 = compteur1=compteur2=0
    for i in range(n):
        a= repetition_2_lancers_truques()
        if a==0:
            compteur0 +=1
        elif a==1:
            compteur1 +=1
        else:
            compteur2+=1
    frequence0 = compteur0/n
    frequence1 = compteur1/n
    frequence2 = compteur2/n
    return [frequence0, frequence1,frequence2]
