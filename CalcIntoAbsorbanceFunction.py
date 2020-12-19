# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:17:42 2020

@author: alicj
"""

# In[ ]:
import math


def intoabs(trans):    #MAIN FUNCTION - calculation for Absorbance
    absorbance_calc = 2 - (math.log(trans, 10))
    conval.append(absorbance_calc)   ##adds values to new list
    return(absorbance_calc)   


def intotrans(absr):    #MAIN FUNCTION - calc for Transmittance
    transmittance_calc = (10**-absr)*100
    conval.append(transmittance_calc)    #adds values to new list
    return(transmittance_calc)


def PrintAllValues ():
    print ('You have introduced {} values.'.format (valuecount))
    print (' You left {} minutes between each reading.'.format (interv))
    print ('These are your time stamps with each converted value:')
    output = 'You have introduced {} values.'.format (valuecount)
    output_2 =' You left {} minutes between each reading.'.format (interv)
    output_3 ='These are your time stamps with each converted value:'
    for r, v in zip(range(0,maxlim+interv,interv), conval):#maxlim+interv, as range() excludes the end number provided, but we still want to include max.
        output_4 = (r, "mins", v)
        print (r, "mins:", v)
    return (output, output_2, output_3, output_4)
#will print time stamp, alongside each converted value.
# the maximum time stamp, and time interval between each reading was used to create a range for the total range of time.
# variables r and v were used to iterate through both this range, and the list of converted values, simultaneously
# this was then used to print the time (in mins), alongside each converted value.    


def SaveResults ():
    f = open ('example','w')
    f.write (str(PrintAllValues ()))
    f.close()
    
    
 ##PRIMARY FUNCTIONS
values = []    #list of values to be converted

conval = []    #list of values after conversion

#maxlim, minlim and intervals needed. minlim = 0. maxlim = (length*interv)-interv!

valuecount = int(input("How many values do you have?"))    #This is used to calculate the range of time, assuming the first reading was completed at 0 mins.
#maybe make this float?
interv = int(input("How much time did you leave between each reading? (please enter in minutes):"))    #used to generate time stamp sequence

maxlim = ((valuecount*interv)-interv)    #getting 0-highest time stamp

tora = ""    #setting the variable for the input function that asks the user which (T or A) they would like to calculate.

while tora not in ("t", "a"):    #while loop ensures program continues running if appropriate input is not provided.
    tora = input("Would you like to calculate Transmittance or Absorbance? Please enter t/a:") 
    if tora == "t":    #if user chooses to calculate Transmittance
        for i in range(0,valuecount):    #addition of 0 allows range to be of the right length. (usually excludes end number)
            absr = float(input("Please enter each Absorbance value in order, starting from the first."))    #user inputs values they want to convert.
            values.append(absr)    #Absorbance readings are added to the list values[]
        for i in values:    #for loop applies function to all values in list.
            intoabs(i)    #MAIN FUNCTION applied to convert Transmittance to Absorbance.
                            
    elif tora == "a":    #if user chooses to calculate Absorbance
        for i in range(0,valuecount):    #addition of 0 allows range to be of the right length. (usually excludes end number)
            trans = float(input("Please enter each Transmittance value in order, starting from the first."))
            values.append(trans)    #Transmittance readings added to list
        for i in values:    #for loop applies function to all values in list.
            intotrans(i)    #MAIN FUNCTION applied function
   
    else:
        print("Please respond with either 't' or 'a'.")    #avoids error, ensures user provides appropriate input.


#choosing which function to run based on intended calculation

r = int()
v = int()

PrintAllValues ()


ask_user = str(input('Would you like to save the results? Please enter yes/no'))
yes = 'yes'
if ask_user == yes:
    SaveResults()
else:
    print ('Okay. Goodbye!')
    
    
