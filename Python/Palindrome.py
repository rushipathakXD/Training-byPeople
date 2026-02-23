num = int(input("Enter a Number: "))
temp = num
reverse = 0

while(num > 0):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if(reverse == temp):
    print(temp, "is Palindrome")
else:
    print(temp, "is not Palindrome")