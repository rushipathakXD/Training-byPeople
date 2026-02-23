num = int(input("Enter a number: "))
digitSum = 0
temp = num
while(temp>0):
    reverse = temp % 10
    digitSum += reverse
    temp = temp // 10

print(f"The sum of {num} is {digitSum}")