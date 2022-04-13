# Author: John Thomas
# netID: jat710
#
# Description: A short program designed to calculate the 

import pytest


from appJar import gui
from cProfile import run
from unittest import result



# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        feet = float(app.getEntry("Feet"))
        inch = float(app.getEntry("Inches"))
        weight = float(app.getEntry("Weight"))
        bmi = bmiCalculator(feet,inch,weight)
        bmiStr = str(bmi)
        result = bmiResult(bmi)
    
        app.setLabel("bmiString", bmiStr)

        app.setLabel("result", result)
        


# create a GUI variable called app
app = gui("BMI Calculator", "800 x 900")
app.setBg("lightBlue")
app.setFont(12)

app.addLabel("height","Please enter your height")
app.addLabelEntry("Feet")

app.addLabelEntry("Inches")

app.addLabel("Please enter your weight in Pounds:")
app.addLabelEntry("Weight")

#app.addEmptyLabel("sep", 1,0,3, 0)

app.addLabel("BMI result:")
app.addLabel("bmiString", "")


app.addLabel("Category:")
app.addLabel("result", "")


# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)



app.setFocus("Weight")






def bmiCalculator(feet,inches,lbs):
    metLbs = lbs*0.45
    metHeight = ((feet*12) + inches) * 0.025
    metHeightSquared = metHeight*metHeight
    return (metLbs / metHeightSquared)
    
def bmiResult(bmi):
    category = ""
    if(bmi < 18.5):
        category = "Underweight"
    elif(bmi >= 18.5 and bmi <= 24.9):
        category = "Normal"
    elif(bmi>=25 and bmi <= 29.9):
        category = "Overweight"
    else:
        category = "Obese"
    return category

#def main(feet,inches,lbs):
    #print("Please imput th1e variables to calculate your BMI. \nHeight")
    #feet = float(input("Feet: "))
    #inches = float(input("Inches: "))
    #lbs = float(input("Weight:\nPounds: "))

    
    #input("PRESS ENTER TO CONTINUE")
   
    
    
    
if __name__ == "__main__":
    app.go()