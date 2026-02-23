user_input = []
length = int(input("Enter the length of List: "))

for i in range(length):
    num1 = int(input(f"Enter the {i}th Element: "))
    if(num1 not in user_input):
        user_input.append(num1)
    continue

print(user_input)