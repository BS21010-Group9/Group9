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


def intoabs(trans):    ##MAIN FUNCTION - calculation for Absorbance
    absorbance_calc = 2 - (math.log(trans, 10))
    conval.append(absorbance_calc)   ##adds values to new list
    return(absorbance_calc)   

def intotrans(absr):    ##MAIN FUNCTION - calc for Transmittance
    transmittance_calc = (10**-absr)*100
    conval.append(transmittance_calc)    #adds values to new list
    return(transmittance_calc)


values = []    #list of values to be converted

conval = []    #list of values after conversion

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
        for i in values:    #for loop applies function to all values in list.
            intoabs(i)    #applies the function to convert Transmittance to Absorbance.
                            
    elif tora == "a":
        for i in range(0,valuecount):    #addition of 0 allows range to be of the right length. (usually excludes end number)
            trans = float(input("Please enter each value in order, starting from the first."))
            values.append(trans)    #Transmittance readings added to list
        for i in values:    #for loop applies function to all values in list.
            intotrans(i)    #applies function
   
    else:
        print("Please respond with either 't' or 'a'.")    #avoids error, ensures user provides appropriate input.   #avoids error, ensures user provides appropriate input.
#these two chunks of code need linked together,
#ive added ala's transmittance & absorbance calculations
#into the same program.
#need a for loop & counter in this calculation area to go through the whole list 
#Alicja's code- Calculations


#choosing which function to run based on intended calculation
print(conval)


###
r = int()
v = int()
#Judith's code
def PrintAllValues ():
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
PrintAllValues ()
def SaveResults ():
    f = open ('example','w')
    f.write (str(PrintAllValues ()))
    f.close()
    
    #save function
ask_user = str(input('Would you like to save the results?'))
yes = 'yes'
if ask_user == yes:
    SaveResults()
else:
    print ('Okay. Goodbye!')
    
    
#=======
#absorbance = float(input("Please type in your absorbance value here:"))
#>>>>>>> refs/remotes/origin/main

#def intotrans(absr = absorbance):
#    transmittence_calc = (10**-absr)*100
#    return(transmittence_calc)

#print(absorbance_calc, transmittence_calc)

#<<<<<<< HEAD
#  return (output, output_2, output_3, output_4)


#=======
#>>>>>>> refs/remotes/origin/main
