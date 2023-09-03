#This program allows me to run an operation on two nurmerical values


operator = str(input("what operator would you like to use (+:Addition,-:Subtraction,/:division,*:multiplication) "))

print(f"you selected {operator } ")

firstValue = int(input("Input the first Value"))

secondValue = int(input("Input the Second Value"))

print(f"you provided {firstValue }, {secondValue }  ")

  
if operator == '+':
    print("You selected Addition Operation")

    print("The answer is" ,firstValue + secondValue)


if operator == '-':
    print("You selected Subtraction Operation")

    print("The answer is" ,firstValue - secondValue)


if operator == '/':
    print("You selected division Operation")

    print("The answer is" ,firstValue / secondValue)



if operator == '*':
    print("You selected multiplication Operation")

    print("The answer is" ,firstValue * secondValue)



# a = 50
# b = 120
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
