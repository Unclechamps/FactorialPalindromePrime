
#asking for user input
def userInput():
    wordpal = input("Enter a word to determine if it is a palindrome: ")
    return wordpal

(wordpal) = userInput()

#reversing the word by establishing an empty variable and then asking to add
#all letters from the end to the front.
def palindrome(wordpal):
    reverse_word = ""
    for i in range(1, len(wordpal)+1):
        reverse_word += wordpal[-i]
    return (reverse_word)

reverse_word = palindrome(wordpal)

#check if the value of reverse_word and wordpal is the same. Both with lower-case.
def check(worldpal):
    if wordpal.lower() == reverse_word.lower():
        print(f"The word {wordpal} is a palindrome!")
    else:
        print("This is not a palindrome.")

check(wordpal)
