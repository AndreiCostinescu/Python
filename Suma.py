# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 08:57:50 2017

@author: Andrei
"""

print("Buna!")
print("Calculeaza suma a doua numere.")
vreiSaCalculezi = True
while vreiSaCalculezi:
    a = int(input("a = "))
    b = int(input("b = "))
    print("Suma a + b = ", a + b, sep='')
    if input() == 'r':
        vreiSaCalculezi = True
    else:
        vreiSaCalculezi = False

print("Program terminat.\nTi-a placut? :)")
input()