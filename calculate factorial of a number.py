no = int(input("Enter a number: "))
fact = 1
if no < 0:
   print(" Factorial does not exist for negative numbers")
elif no == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,no + 1):
       fact = fact*i
   print(fact)
