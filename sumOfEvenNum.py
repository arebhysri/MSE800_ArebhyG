import numpy as py
#take input from user
# mtd1 for loop
num = int(input("Please enter number ? : "))
sum = 0
if num <= 0:
    print("Please enter a number greater than 0")
else:
    even_sum = 0
    print("Even numbers between 1 and", num, ":")

    for i in range(2, num + 1, 2):  # start from 2, step by 2
        print(i, end=" ")
        even_sum += i

    print("\nTotal sum of even numbers:", even_sum)

# mtd 2 while loop
n = int(input("Please enter a number: "))

if n <= 0:
    print("Please enter a number greater than 0")
else:
    even_sum = 0
    i = 2

    print("Even numbers between 1 and", n, ":")

    while i <= n:
        print(i, end=" ")
        even_sum += i
        i += 2

    print("\nTotal sum of even numbers:", even_sum)


