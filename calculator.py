
#calculatrice

import re

print("--------- Calculator --------")
print("---- Type 'quit' to exit ----\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation=""

    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input("Enter equation: "+str(previous))
    
    if equation == 'quit':
        print("You've decided to stop the program.")
        run = False
    else:
        equation = re.sub('[a-zA-Z:" ","\'"]','',equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        print(previous)

while run:
    performMath()