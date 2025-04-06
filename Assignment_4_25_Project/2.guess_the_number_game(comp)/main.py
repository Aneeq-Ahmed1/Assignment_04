import random

print("\n ✨ Welcome to the Number Guessing Game ✨ \n")
print("💻 Computer Guess the Number.\n")

low = 1
high = 10

print("🤔 Think of a number between 1 and 10, and 💻 will try to guess it!")

input("🎯 Press Enter when you're ready...")

while low <= high:
    guess = random.randint(low, high)
    print(f"\n🤖 Computer's guess is {guess}")

    feedback = input("👉 Enter 'h' for too high, 'l' for too low, or 'c' for correct: ").lower()

    if feedback == 'c':
        print(f"\n🎉 Yay! 💻 The computer guessed your number {guess}! 🎉")
        break
    elif feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    else:
        print("⚠️ Invalid input. Please enter only 'h', 'l', or 'c'. 🚫")

if low > high:
    print("\n😅 Hmm... It seems there was a misunderstanding. Let's try again! 🔄")










