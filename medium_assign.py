'''

This file contains the functions that you need for completing this assignment. 

1. expression_1() --> 30%
2. expression_2() --> 40%
3. expression_3() --> 30% 

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''
import math
def expression_1(x):
    print("X is equal to: ",x)
    var_1=math.pow(x,3) - (x*2 + math.pow(x,2)) - 100
    print("The Answer is: ",var_1)
    '''
    
        Write a code that returns value for the following expression: x^3 - (2x + x^2) - 100 
    
    '''
    return

def expression_2(x, y):
    print("X is equal to: ",x)
    print("Y is equal to: ",y)
    var_2=(math.pow(x,4)/(2*y)) - 3*x*y + ((6*y)/(7*x))
    print("The Answer is: ", var_2)
    '''
        Write code that returns only the integer value of the following expression: (x^4 / 2y) - (3xy) + (6y / 7x)
    '''
    return


def expression_3(x, y):
    print("X is equal to: ",x)
    print("Y is equal to: ",y)
    var_3=(math.pow(x,3)+math.pow(y,2))/(math.pow(x,2)-math.pow(y,3))
    print("The Answer is: ", var_3)
    '''
        Write code that returns the value of the following expression: (x^3 + y^2) / (x^2 - y^3)
    '''
    return


if __name__ == "__main__":
    expression_1(3)
    expression_2(2,3)
    expression_3(1,2)