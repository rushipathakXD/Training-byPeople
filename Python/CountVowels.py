user_input = input("Enter a String: ")
count = 0
for i in user_input:
    if i in "AEIOUaeiou":
        count += 1

print(f"Number of vowels in {user_input} are: {count}")