# To take input from the user
num = int(input("Please enter a number: "))

#Init
factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Factorial shouldn't be negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
