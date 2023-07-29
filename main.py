import random

set = [("apple"), ("arrow"), ("beach"), ("bread"), ("steam"), ("cloud"), ("dance"), ("earth"), ("fight"), ("ghost"), ("happy"), ("knife"), ("jumbo"), ("mango"), ("laugh") ]
word = random.choice(set)

def start():

    userWord = ''
    attempts = 5

    while attempts > 0:
        userAttempt = input(": ")

        if userAttempt == word:
            print(userAttempt.upper() + "\nCongratulations!\n")
            return True
        
        for i in range(len(word)):
            if userAttempt[i] == word[i]:
                userWord += userAttempt[i].upper()
            elif userAttempt[i] in word:
                userWord += userAttempt[i].lower()
            else:
                userWord += '_'

        attempts -= 1

        print("\n" + userWord + "\n")

    return False

print("\nVamos Começar!\n")

start()
