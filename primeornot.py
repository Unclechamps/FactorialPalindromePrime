#asking for user input
def userInput():
    number = int(input("Enter an integer: "))
    return number

(number) = userInput()

#calculating whether number % num in range == 0
def isPrime(number):
    for i in range(2, number):
        if number > 2 and number % i == 0:
            prime = False
            break
        else:
            prime = True
    return prime

#assigning value of isPrime(number) to a variable.
prime = isPrime(number)

#printing function with prime as argument
def printprime(prime):
    if prime == False:
        print(f"{number} is NOT a prime number")
    else:
        print(f"{number} is definitely a prime number!")

printprime(prime)
