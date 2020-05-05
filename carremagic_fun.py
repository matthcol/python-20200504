# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:37:03 2020

Ref :
https://fr.wikipedia.org/wiki/Carr%C3%A9_magique_(math%C3%A9matiques)


@author: Matthias
"""

def isMagique(carre):
    n = len(carre)
    sm = n*(n**2+1)//2
    # verifier que toutes les lignes ont une somme égale à sm
    #for i in range(n):
    res = all(sum(ligne)==sm for ligne in carre)
    # verifier que toutes les colonnes ont une somme égale à sm
    res = res and all(sum(carre[i][j] for i in range(n))==sm for j in range(n))
    # vérifier que les 2 diagonales ont une somme à sm
    res = res and sum(carre[i][i] for i in range(n))==sm \
            and sum(carre[i][-i-1] for i in range(n))==sm
    # vérifier nbs tous utilisés une fois
    return res


def zeroSquare(n):
	return [[0 for j in range(n)] for i in range(n)]

def makeMagic(n):
	if n%2 == 0:
		raise ValueError("even size is not possible")
	nn = n**2
	square = zeroSquare(n)
	l,c = 0, n//2
	square[l][c] = 1
	for e in range(2,nn+1):
		l2, c2 = (l+2)%n, (c+1)%n
		if square[l2][c2] == 0:
			l,c = l2,c2
		else:
			l = (l+1)%n
		square[l][c] = e
	return square
