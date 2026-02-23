user_input = []
max = 0
length = int(input("Enter the length of List: "))

for i in range(length):
    num1 = int(input(f"Enter the {i}th Element: "))
    user_input.append(num1) 

for num in user_input:
    if(num > max):
        max = num

print(f"Max: {max}")