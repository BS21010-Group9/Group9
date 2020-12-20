# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:17:42 2020

@author: alicj
"""

# In[ ]:
import math


def intoabs(trans):    #MAIN FUNCTION - calculation for Absorbance
    absorbance_calc = 2 - (math.log(trans, 10))
    return(absorbance_calc)   


def intotrans(absr):    #MAIN FUNCTION - calc for Transmittance
    transmittance_calc = (10**-absr)*100
    return(transmittance_calc)


def PrintAllValues (valuecount, interv, maxlim, conval):
    print ('You have introduced {} values.'.format (valuecount))
    print ('You left {} minutes between each reading.'.format (interv))
    print ('These are your time stamps with each converted value: ')
    output = 'You have introduced {} values.'.format (valuecount)
    output_2 ='You left {} minutes between each reading.'.format (interv)
    output_3 ='These are your time stamps with each converted value: '
    output_4 =""
    for r, v in zip(range(0,maxlim+interv,interv), conval):#maxlim+interv, as range() excludes the end number provided, but we still want to include max.
        output_4 += "\n" + str(r) + " mins " + str(v)
        print (r, "mins:", v)
    return (output, output_2, output_3, output_4)
#will print time stamp, alongside each converted value.
# the maximum time stamp, and time interval between each reading was used to create a range for the total range of time.
# variables r and v were used to iterate through both this range, and the list of converted values, simultaneously
# this was then used to print the time (in mins), alongside each converted value.    


def SaveResults (x):
    name_file = str(input('Please introduce the name for your file.')) #aks user to choose the name of the file
    f = open ( name_file ,'w')
    for i in range(4):
        f.write (str(x[i])+"\n")
    f.close()
    
def MainLoop():    
    ##PRIMARY FUNCTIONS
    values = [] #list of values to be converted

    conval = [] #list of values after conversion

    check = False

    while check == False:
        try:
            valuecount = int(input("How many values do you have? ")) #This is used to calculate the range of time, assuming the first reading was completed at 0 mins.
        except ValueError:
            print("Sorry you have to put in a whole number. ")
        else:
            if valuecount > 0:
                check = True
            else:
                print("Sorry but you have to put in a positive number. ")
    
    check = False
    
    while check == False:        
        try:
            interv = int(input("How many minutes did you leave between each reading? "))    #used to generate time stamp sequence
        except ValueError:
            print("Sorry you have to input a number. ")
        else:
            if interv > 0:
                check = True
            else:
                print("Sorry but you have to put in a positive number. ")
            
    maxlim = ((valuecount*interv)-interv) #getting 0-highest time stamp
    
    tora = ""    #setting the variable for the input function that asks the user which (T or A) they would like to calculate.
    
    while tora not in ("t", "a","T","A"):    #while loop ensures program continues running if appropriate input is not provided.
        tora = input("Would you like to calculate Transmittance or Absorbance? Please enter t/a: ") 
        if tora == "t" or tora == "T":    #if user chooses to calculate Transmittance
            for i in range(0,valuecount):    #addition of 0 allows range to be of the right length. (usually excludes end number)
                absr = float(input("Please enter each Absorbance value in order, starting from the first. "))    #user inputs values they want to convert.
                values.append(absr)    #Absorbance readings are added to the list values[]
            for i in values:    #for loop applies function to all values in list.
                conval.append(intoabs(i))    #MAIN FUNCTION applied to convert Transmittance to Absorbance.
                                
        elif tora == "a" or tora == "A":    #if user chooses to calculate Absorbance
            for i in range(0,valuecount):    #addition of 0 allows range to be of the right length. (usually excludes end number)
                try:
                    trans = float(input("Please enter each Transmittance value in order, starting from the first. "))
                    values.append(trans)    #Transmittance readings added to list
                except ValueError:
                    print("Sorry you have to put in a number. ")
            for i in values:    #for loop applies function to all values in list.
                conval.append(intotrans(i))    #MAIN FUNCTION applied function
       
        else:
            print("Please respond with either 't' or 'a'. ")    #avoids error, ensures user provides appropriate input.
    
    
    #choosing which function to run based on intended calculation
    x = PrintAllValues(valuecount, interv, maxlim, conval)
    check = False
    while check == False:
        ask_user_save = str(input('Would you like to save the results? Please enter yes/no '))
        if ask_user_save.lower() == "yes":
            SaveResults(x)
            print("Okay, I saved it on your device. ")
            check = True
        elif ask_user_save.lower() == "no":
            print("Okay, no problem! We hope you liked the program. ")
            check = True
        else:
            print ('Please answer yes or no. ')
            
check = False
 
while check == False:
    MainLoop()
    check_again = False
    while check_again == False:
        ask_user_again = input("Would you like to use the program again? ")
        if ask_user_again.lower() == "no":
            print("Okay! See you later!")
            check_again = True
            check = True
        elif ask_user_again.lower() == "yes":
            print("Okay! Here we go again!")
            check_again = True
        else:
            print("Please respond with yes or no.")
     
    
