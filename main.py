import random

set = [("apple"), ("arrow"), ("beach"), ("bread"), ("steam"), ("cloud"), ("dance"), ("earth"), ("fight"), ("ghost"), ("happy"), ("knife"), ("jumbo"), ("mango"), ("laugh") ]
word = random.choice(set)

def start():

    attempts = 5

    while attempts > 0:

        userWord = ['', '', '', '', '']
        userAttempt = input(": ")

        if userAttempt == word:
            print(userAttempt.upper() + "\nCongratulations!\n")
            return True
        
        for i in range(len(word)):
            
            if userAttempt[i] == word[i]:
                userWord[i] = userAttempt[i].upper()
            elif userAttempt[i] in word:
                userWord[i] = userAttempt[i].lower()
            else:
                userWord[i] = '_'

        attempts -= 1

        print("".join(userWord))

    print("\nGAME OVER!\n")

    return False

print("\nVamos Começar!\n")

start()
