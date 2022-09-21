#!/usr/bin/env python3

# Created by: Isaiah Fernandez
# Date: September 20, 2022
# This program calculates the area and perimeter of a rectangle.


from re import L
from tkinter import W


def main():
    #This function calculates area and perimeter. 
    L=6
    W=7
    print("if a rectangle has the dimensions:")
    print("{}cm and {}cm". format(L,W))
    print("")
    print("Area is {}cm^2". format(L*W))
    print("Perimeter is {}cm". format(2*(L+W)))

          
if __name__ == "__main__":
    main()