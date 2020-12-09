# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:50:32 2020

@author: alicj
"""

absorbance = float(input("Please type in your absorbance value here:"))

def intotrans(absr = absorbance):
    T = (10**-absr)*100
    return(T)