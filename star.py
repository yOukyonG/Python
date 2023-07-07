# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 14:56:16 2023

@author: USER
"""
'''
0____*____    4 1 4 
1___*__*___   3 2 3
2__*____*____ 2 4 2
3_*______*_   1 6 1
4*________*   0 8 0
5* * * * * *  6
'''

print("4번")
for i in range(6):
    if i ==0 or i==5:
        print(" "*(5-i), end ="")
        if i==5:
            print("* "*(i+1), end ="")
        print("* ", end ="")
        print()
    else:
        # for j in range(2, 5-i):
        print(" "*(5-i), end="")
        print("*", end="")
        print(" "*(i*2), end="")
        print("*", end="\n")

        
