# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:17:42 2020

@author: alicj
"""
import math

transmittance = float(input("Please type in  your transmittance value here:"))

def intoabs(tran = transmittance):
    A = 2 - (math.log(tran, 10))
    return A
