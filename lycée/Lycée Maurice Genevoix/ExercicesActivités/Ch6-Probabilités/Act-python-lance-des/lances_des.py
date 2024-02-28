import random as rd
import math as ma

def Deux_des_K(n,k):
    succes = 0
    for i in range(n):
        de_1 = rd.randint(1,6)
        de_2 = rd.randint(1,6)
        if de_1 + de_2 == k:
            succes = succes + 1
    return succes/n

def Trois_des_K(n,k):
    succes = 0
    for i in range(n):
        de_1 = rd.randint(1,6)
        de_2 = rd.randint(1,6)
        de_3 = rd.randint(1,6)
        if de_1 + de_2 + de_3 == k:
            succes = succes + 1
    return succes/n

for i in range(1,6):
    print(Deux_des_K(10**i,12))
