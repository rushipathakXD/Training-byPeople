def add(num2,num1):
    return num1 + num2
def sub(num2,num1):
    return num1 - num2
def mul(num2,num1):
    return num1 * num2
def div(num2,num1):
    if(num2 == 0):
        print("Infinity")
    return num1 / num2

choice = True

while(choice == True):
    print("\n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Exit")
    userChoice = int(input("Enter your choice:(1-5) --->"))
    if(userChoice == 5):
            print("Exiting Calculator")
            break
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

    match userChoice:
        case 1:print(add(num1,num2))
        case 2:print(sub(num1,num2))
        case 3:print(mul(num1,num2))
        case 4:print(div(num1,num2))
        
        case _:print("Enter valid Input")