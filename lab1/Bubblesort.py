#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# n^2 w kazdym przypadku

def bsort(tab):
    for n in range(0, len(tab) - 1):
        change = False
        for i in range(len(tab) - 1):
            if tab[i] > tab[i + 1]:
                tab[i], tab[i + 1] = tab[i + 1], tab[i]
                change = True
        if not change:
            return


A = [1, 2, 5, 7, 3, 2, 11, 9]
bsort(A)
print(A)
