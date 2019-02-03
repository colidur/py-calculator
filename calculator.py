#Pythnon3
#Calculator

import re

print("--------- Calculator --------")
print("---- Type 'quit' to exit ----\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""


    if previous == 0:
        equation = input("Enter equation: ")
        
    else:
        print("\n---- Type 'quit' to exit -------")
        print("---- Type 'restart' to clear ---\n")
        equation = input("Enter equation: "+ str(previous) + " ")
        
        
    try:
        
        if equation == 'quit':
            print("You've decided to stop the program.")
            run = False
            
        elif equation == 'restart':
            print("You've decided to restart the program.")
            previous = 0
    
        else:
            equation = re.sub('[a-zA-Z:" ","\'"]', '', equation)
            
            if previous == 0:
                previous = eval(equation)
                
            else:
                previous = eval(str(previous) + equation)
            print(previous)
    
    
    except ZeroDivisionError:
        print("/!\ Please do not divide by zero")
    
    except SyntaxError:
        print("/!\ Please use numbers or mathematics symbols only")

    except NameError:
        print("/!\ Please use numbers")

while run:
    performMath()