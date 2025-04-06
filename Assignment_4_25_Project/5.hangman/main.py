import random

# Word list
words = ["python", "developer", "hangman", "programming", "challenge", "keyboard", "function", "variable"]

hangman_stages = [
    """
     --------
     |      |
     |      
     |    
     |      
     |     
    ---
    """,
    """
     --------
     |      |
     |      O
     |    
     |      
     |     
    ---
    """,
    """
     --------
     |      |
     |      O
     |      |
     |      
     |     
    ---
    """,
    """
     --------
     |      |
     |      O
     |     /|
     |      
     |     
    ---
    """,
    """
     --------
     |      |
     |      O
     |     /|\\
     |      
     |     
    ---
    """,
    """
     --------
     |      |
     |      O
     |     /|\\
     |     / 
     |     
    ---
    """,
    """
     --------
     |      |
     |      O
     |     /|\\
     |     / \\
     |     
    ---
    """
]

def get_random_word():
    return random.choice(words)

def display_progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6
    print("\n🔤 Welcome to Hangman!\n")

    while attempts > 0:
        print(hangman_stages[6 - attempts])
        print("Word: ", display_progress(word, guessed_letters))
        guess = input("🔎 Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabetic character.\n")
            continue

        if guess in guessed_letters:
            print("🌀 You already guessed that letter!\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct!\n")
            if all(letter in guessed_letters for letter in word):
                print("🎉 Congrats! You've guessed the word:", word)
                break
        else:
            print("❌ Wrong guess!\n")
            attempts -= 1

    if attempts == 0:
        print(hangman_stages[-1])
        print("💀 Game Over! The word was:", word)

if __name__ == "__main__":
    play_hangman()
