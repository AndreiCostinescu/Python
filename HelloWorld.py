# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 08:09:18 2017

@author: Andrei
"""

print("Bună dimineața!", end='\n')
print("Cum te cheamă?")
nume = input("Nume: ")
print("Bună dimineața, ", nume, "!", sep='')
if nume == "David":
    print("Ești cel mai tare!")
elif nume == "Andrei":
    print("Și tu ești cel mai tare!")
elif nume == "Teodora":
    print("Tu nu ești cea mai tare, dar ești cea mai frumoasă! :D")
else:
    print("Este o zi frumoasă azi, nu?")
    
input()
