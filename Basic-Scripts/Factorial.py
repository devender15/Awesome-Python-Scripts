# Python program to find the factorial of a number provided by the user.


# we are finding the factorial of a number by recursion
def factorial(n):
   if(n < 0):
      print("Sorry, factorial does not exist for negative numbers")
   elif(n <= 1):
      return 1

   return n * factorial(n-1)

if __name__ == '__main__':
   num = int(input("Enter a number: "))
   print(f"The factorial of {num} is {factorial(num)} !")