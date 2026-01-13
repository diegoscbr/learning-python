'''
Docstring for membershipOperators

A siple guessing game program to show how membership operators work
'''
'''

'''
guess = "-----"
word = "APPLE"
word = word.lstrip()
print("""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗  ║
║   ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝  ║
║   ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗    ║
║   ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝    ║
║   ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗  ║
║    ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝  ║
║                                                                   ║
║            ╔════════════════════════════════════════╗             ║
║            ║   LETTER GUESSING GAME                 ║             ║
║            ║   Guess the 5-letter word!             ║             ║
║            ║   Type 'exit' or 'quit' to end         ║             ║
║            ╚════════════════════════════════════════╝             ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
""")
while True:
    print(guess)
    letter = input("Guess a letter that is in the 5 letter word: ")
    letter = letter.upper()
    if letter == "EXIT" or letter == "QUIT":
        print("END OF GAME")
        break
    if letter in word:
        positions = [i for i, char in enumerate(word) if char == letter]
        print(f"There is a {letter} in the word at position{positions}")
        for i in positions:
            #word = word[:index] + new_char + word[index + 1:]
            guess = guess[:i] + letter + guess[i+1:]
        #get the index of where it is
    
    if letter not in word:
        print(f"There is not a {letter} in the word")

    if guess == word:
        print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗   ║
║   ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║   ║
║    ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║   ║
║     ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║   ║
║      ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║   ║
║      ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝   ║
║                                                                  ║
║                    🎉 CONGRATULATIONS! 🎉                        ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
""")
        break
    



