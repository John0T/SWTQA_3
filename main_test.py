import main
import pytest

#bmi result test cases:


#bmi test, underweight, N x 1
def test_bmiResultUW_OFF():
    assert main.bmiResult(18.6) != "Underweight"
    
def test_bmiResultUW_ON():
    assert main.bmiResult(18.5) != "Underweight"
    
def test_bmiResultUW_ON2():
    assert main.bmiResult(18.4) == "Underweight"
    
#bmi test, Normal (lower bound), N x 1
def test_bmiResultNormal_Lower_OFF():
    assert main.bmiResult(18.4) != "Normal"

def test_bmiResultNormal_Lower_ON():
    assert main.bmiResult(18.5) == "Normal"
    
def test_bmiResultNormal_Lower_ON2():
    assert main.bmiResult(18.6) == "Normal"

#bmi test, Normal (lower bound), N x 1
#BOUNDARY SHIFT OF 0.1
#def test_bmiResultNormal_Lower_OFF():
#    assert main.bmiResult(18.5) != "Normal"

#def test_bmiResultNormal_Lower_ON():
 #   assert main.bmiResult(18.6) == "Normal"
    
#def test_bmiResultNormal_Lower_ON2():
#    assert main.bmiResult(18.7) == "Normal"
    
#bmi test, Normal (upper bound), N x 1
def test_bmiResultNormal_Upper_OFF():
    assert main.bmiResult(25) != "Normal"

def test_bmiResultNormal_Upper_ON():
    assert main.bmiResult(24.9) == "Normal"
    
def test_bmiResultNormal_Upper_ON2():
    assert main.bmiResult(24.8) == "Normal"
    
    
#bmi test, Overweight(Lower bound), N x 1
def test_bmiResultOW_Lower_OFF():
    assert main.bmiResult(24.9) != "Overweight"

def test_bmiResultOW_Lower_ON():
    assert main.bmiResult(25) == "Overweight"
    
def test_bmiResultOW_Lower_ON2():
    assert main.bmiResult(25.1) == "Overweight"
    

#bmi test, Overweight(Upper bound), N x 1
def test_bmiResultOW_Upper_OFF():
    assert main.bmiResult(30) != "Overweight"

def test_bmiResultOW_Upper_ON():
    assert main.bmiResult(29.9) == "Overweight"
    
def test_bmiResultOW_Upper_ON2():
    assert main.bmiResult(29.8) == "Overweight"


#bmi test, Obese, N x 1
def test_bmiResultObese_OFF():
    assert main.bmiResult(29.9) != "Obese"
    
def test_bmiResultObese_ON():
    assert main.bmiResult(30) == "Obese"
    
def test_bmiResultObese_ON2():
    assert main.bmiResult(30.1) == "Obese"
    
#test cases for the BMI calculator
    
def test_bmiCalculatorON():
    assert main.bmiCalculator(6,2,150) == 19.722425127830533

def test_bmiCalculatorOFF():
    assert main.bmiCalculator(6,2,150) != 20