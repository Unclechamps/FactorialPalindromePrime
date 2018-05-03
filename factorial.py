# ask for user input. While the value is a number, return number. If an ValueError
#is returned, then ask for a number.

def userInput():
    while True:
        try:
            number=float(input("Enter a number to calculate factorial: "))
        except ValueError:
            print("Please enter a number!")
            continue
        else:
            return number

(number) = userInput()

def factorial(number):
    total = 1
    while number >= 1:
        total = total * number
        number = number - 1
    return total

print(factorial(number))
