def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("select the operation")
print("1.Addition")
print("2.subtraction")
print("3.multiply")
print("4.Division")

choice = input("enter the choice(1,2,3,4)")

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if choice == "1":
    print(num1, "+" , num2 , "=" , add(num1,num2))

elif choice == "2":
    print(num1 , "-" , num2 ,"=" , sub(num1,num2))

elif choice == "3":
    print(num1, "*", num2 , multiply(num1,num2))

elif choice == "4":
    print(num1, "/", num2 , divide(num1,num2))
else:
    print("Invalid input")










