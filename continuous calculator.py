import re
print("My first calculator")
previous = 0
run = True

def perform_math():
        global previous
        global run
        equation = ""
        if previous == 0:
            equation = input("enter the equation")
        else:
             equation = input(str(previous))
        if equation == "quit":
            run = False
        else:
            equation = re.sub("[a-zA-Z.,()" "], ","", equation)
            if previous == 0:
                previous = eval(equation)
            else:
                previous = eval(str(previous) + equation)

while run:
    perform_math()