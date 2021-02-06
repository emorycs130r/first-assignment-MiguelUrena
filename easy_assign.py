
'''

This file contains the functions that you need for completing this assignment. 

1. append_two_strings() --> Function to append a string2 to string1. -- 30%
2. append_character() --> Function to append a character to the end of string. -- 30% 
3. append_num_to_string() --> Function to append a number to the end of a string. -- 40%

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''

def append_two_strings(string_1,string_2):
    string_3= string_1 + string_2
    print("String 1 is: ",string_1)
    print("String 2 is: ",string_2)
    print("When appended the result is: ",string_3)
    return
    


def append_character(string_1,char_1):
    string_4= string_1 + char_1
    print("String 1 is: ",string_1)
    print("Character 1 is: ",char_1)
    print("When appended the result is: ",string_4)
    return 


def append_num_to_string(string_1,num_1):
    string_5= string_1 + num_1
    print("String 1 is: ",string_1)
    print("Number 1 is: ",num_1)
    print("When appended the result is: ",string_5)    
    return

if __name__ == "__main__":
    append_two_strings("Hello"," World")
    append_character("Hello","!")
    append_num_to_string("Hello"," 15")
    