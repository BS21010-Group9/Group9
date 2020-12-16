# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:17:42 2020

@author: alicj
"""
##Marianne's code- Primary Program Functions
# coding: utf-8
#   Primary Functions:
#   - functions: The user should be able to choose which input (T or A) they would like the program to record.
#   - They should also be able to choose the time intervals associated with the values entered (e.g. 5min: 0.07932)

# In[ ]:
import math



values = []    #list of values to be converted

#maxlim, minlim and intervals needed. minlim = 0. maxlim = (length*interv)-interv!

valuecount = int(input("How many values do you have?"))    #This is used to calculate the range of time, assuming the first reading was completed at 0 mins.
#maybe make this float?
interv = int(input("How much time did you leave between each reading? (please enter in minutes):"))

maxlim = ((valuecount*interv)-interv)    #getting 0-highest time stamp

tora = ""    #setting the variable for the while loop that asks the user which (T or A) they would like to calculate.

while tora not in ("t", "a"):
    tora = input("Would you like to calculate Transmittance or Absorbance? Please enter t/a:") 
    if tora == "t":
        for i in range(0,valuecount):    #addition of 0 allows range to be of the right length. (usually excludes end number)
            absr = float(input("Please enter each value in order, starting from the first."))    #user inputs values they want to convert.
            values.append(absr)    #Absorbance readings are added to the list values[]
        
    elif tora == "a":
        for i in range(0,valuecount):    #addition of 0 allows range to be of the right length. (usually excludes end number)
            trans = float(input("Please enter each value in order, starting from the first."))
            values.append(trans)    #Transmittance readings added to list
   
    else:
        print("Please respond with either 't' or 'a'.")    #avoids error, ensures user provides appropriate input.
##these two chunks of code need linked together,
##ive added ala's transmittance & absorbance calculations
##into the same program.

#Alicja's code- Calculations

##This needs to be in a for loop & converted to run a list of values
##Might need a counter based on len of list
#the variables are set to float to make sure they have decimals
absorbance_calc = float()
transmittance_calc = float()

#calculation for absorbance
def intoabs(trans):
    absorbance_calc = 2 - (math.log(trans, 10))
    return(absorbance_calc)

#calculation for transmittance
def intotrans(absr):
    transmittance_calc = (10**-absr)*100
    return(transmittance_calc)

#choosing which function to run based on intended calculation
if tora == "t":
    print(intoabs(absr))
    
else:
    print(intotrans(absr))



#Judith's code
def PrintAllValues ():
  output = 'You have introduced {} values.'.format (valuecount)
  output_2 =' You left {} minutes between each reading.'.format (interv)
  output_3 ='These are your time stamps with each converted value:'

  for r, v in zip(range(0,maxlim+interv,interv), values):

    output_4 = (r, "mins", v)

    print (r, "mins:", v)  

 

  return (output, output_2, output_3, output_4)
