# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:23:15 2017

@author: Andrei
"""

print("Buna!")
print("Calculeaza produsul a doua numere.")
vreiSaCalculezi = True
while vreiSaCalculezi:
    a = int(input("a = "))
    b = int(input("b = "))
    print("Produs a * b = ", a * b, sep='')
    if input() == 'r':
        vreiSaCalculezi = True
    else:
        vreiSaCalculezi = False

print("Program terminat.\nTi-a placut? :)")
input()