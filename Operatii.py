# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:36:19 2017

@author: Andrei
"""

print("Buna!")
print("Calculeaza operatii cu doua numere.")
vreiSaCalculezi = True
while vreiSaCalculezi:
    a = int(input("a = "))
    b = int(input("b = "))
    operatie = input("operatie = ")
    if operatie == "+":
        print("Suma a + b = ", a + b, sep='')
    elif operatie == "-":
        print("Diferenta a - b = ", a - b, sep='')
    elif operatie == "*":
        print("Produs a * b = ", a * b, sep='')
    else:
        print("Operatie necunoscuta... :(")
    if input() == 'r':
        vreiSaCalculezi = True
    else:
        vreiSaCalculezi = False

print("Program terminat.\nTi-a placut? :)")
input()