import random

set = [("apple"), ("arrow"), ("beach"), ("bread"), ("bread"), ("cloud"), ("dance"), ("earth"), ("fight"), ("ghost"), ("happy"), ("knife"), ("jumbo"), ("mango"), ("laugh") ]
word = random.choice(set)

def start(attemps = 5):

    userWord = ''

    userAttempt = input(": ")

    if userAttempt == word:
        print("")
        return True
    
    for i in range(len(word)):
        if userAttempt[i] == word[i]:
            userWord += userAttempt[i].upper()
        else:
            userWord += userAttempt[i]

    

    print(userWord + "\n")

print("\nVamos Começar!\n")

start()