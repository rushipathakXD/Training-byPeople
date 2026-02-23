length1 = int(input("Enter the length of List 1: "))
length2 = int(input("Enter the length of List 2: "))

lst1 = []
lst2 = []

print("Enter the elements of list 1 --> ")
for i in range(length1):
    num = int(input(f"Enter the {i+1}th element: "))
    lst1.append(num)

print("Enter the elements of list 2 --> ")
for i in range(length2):
    num = int(input(f"Enter the {i+1}th element: "))
    lst2.append(num)

commonElements = []
for i in lst2:
    if(i in lst1 and i not in commonElements):
        commonElements.append(i)

print(f"The common elements are: {commonElements}")