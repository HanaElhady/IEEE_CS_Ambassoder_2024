'''
Problem7
Create a module containing functions for
mathematical operations (addition, subtraction, multiplication, division)
'''

def addition(num1 , num2 ) :
    return num1 + num2
def subtraction(num1 , num2 ) :
    return num1 - num2
    
def multiplication(num1 , num2 ) :
    return num1 * num2   
    
def division(num1 , num2 ) :
  if num2 == 0  :
      return "UNDEFINED"
  else :
      return num2 / num1       
        