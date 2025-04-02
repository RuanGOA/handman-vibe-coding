import random
import os

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

words_with_hints = {
    "python": "A popular programming language.",
    "hangman": "A classic word-guessing game.",
    "developer": "A person who writes software.",
    "challenge": "A difficult task or test.",
    "programming": "The act of writing computer code.",
    "openai": "An AI research company.",
    "database": "A system to store and retrieve data.",
    "algorithm": "A step-by-step problem-solving method.",
    "network": "A group of connected computers.",
    "encryption": "A method to secure information.",
    "processor": "The brain of a computer.",
    "compiler": "A program that translates source code.",
    "debugging": "The process of fixing errors in code.",
    "repository": "A storage location for code.",
    "software": "Programs used by computers.",
    "hardware": "Physical components of a computer.",
    "framework": "A pre-built structure for software development.",
    "library": "A collection of prewritten code.",
    "cybersecurity": "Protecting systems from digital attacks.",
    "authentication": "Verifying a user's identity.",
    "virtualization": "Creating virtual instances of systems.",
    "scalability": "The ability to handle growth.",
    "bandwidth": "The data transfer capacity of a system.",
    "latency": "Delay in data transmission.",
    "cloud": "Storing and accessing data over the internet.",
    "containerization": "Running software in isolated environments.",
    "machinelearning": "A type of AI that learns from data.",
    "neuralnetwork": "A machine learning model inspired by the human brain.",
    "bigdata": "Extremely large datasets analyzed computationally.",
    "blockchain": "A decentralized digital ledger.",
    "cryptography": "Securing information through encryption.",
    "frontend": "The part of a website users interact with.",
    "backend": "The server-side logic of a web application.",
    "middleware": "Software that connects different applications.",
    "datacenter": "A facility housing computer systems.",
    "microservices": "An architectural style for building software applications.",
    "opensource": "Software whose source code is publicly available.",
    "multithreading": "Executing multiple threads in a program.",
    "parallelcomputing": "Executing multiple computations simultaneously.",
    "cache": "A storage layer that speeds up data retrieval.",
    "serverless": "Running applications without managing servers.",
    "hypervisor": "Software that creates and manages virtual machines.",
    "routing": "Determining the best path for data transmission.",
    "orchestration": "Managing multiple automated tasks.",
    "scripting": "Writing small programs to automate tasks.",
    "firewall": "A network security system.",
    "loadbalancer": "Distributes network traffic across multiple servers.",
    "authentication": "Verifying the identity of a user or process."
}

def choose_word():
    word, hint = random.choice(list(words_with_hints.items()))
    return word, hint

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def draw_hangman(attempts):
    stages = [
        """
         -----
         |   |
         |   O
         |  /|\\
         |  / \\
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |  /
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  /|
         |
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |   |
         |
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |
         |
         |
        ---
        """,
        """
         -----
         |   |
         |
         |
         |
         |
        ---
        """
    ]
    print(stages[attempts])

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hangman(continuous=False):
    guessed_words = 0
    while True:
        word, hint = choose_word()
        guessed_letters = set()
        attempts = 6
        word_guess_attempted = False
        
        while attempts > 0:
            clear_screen()
            draw_hangman(attempts)
            print(f"\nHint: {hint}")
            print(display_word(word, guessed_letters))
            print(f"Tried letters: {' '.join(sorted(guessed_letters))}")
            if continuous:
                print(GREEN + f"Words guessed correctly: {guessed_words}" + RESET)
            guess = input("Guess a letter or the whole word: ").lower()
            
            if not guess.isalpha():
                print("Please enter a valid letter or word.")
                continue
            
            if guess == word:
                guessed_words += 1
                print(GREEN + "Congratulations! You guessed the word: " + word + RESET)
                input("Press Enter to continue...")
                if not continuous:
                    return
                else:
                    break
            
            if len(guess) == 1:
                if guess in guessed_letters:
                    print("You already guessed that letter.")
                    continue
                
                guessed_letters.add(guess)
                
                if guess in word:
                    print("Good job! That letter is in the word.")
                    if all(letter in guessed_letters for letter in word):
                        guessed_words += 1
                        print(GREEN + "Congratulations! You guessed the word: " + word + RESET)
                        input("Press Enter to continue...")
                        if not continuous:
                            return
                        else:
                            break
                else:
                    attempts -= 1
                    print(RED + f"Wrong guess! You have {attempts} attempts left." + RESET)
            else:
                if word_guess_attempted and continuous:
                    print(RED + "You can only guess the word once in infinite mode!" + RESET)
                    continue
                
                word_guess_attempted = True
                clear_screen()
                draw_hangman(attempts)
                print(RED + "Wrong guess! That is not the word. You lose!" + RESET)
                if continuous:
                    print(GREEN + f"Words guessed correctly: {guessed_words}" + RESET)
                input("Press Enter to continue...")
                return
        
        if attempts == 0:
            clear_screen()
            draw_hangman(attempts)
            print(RED + "Game over! The word was: " + word + RESET)
            if continuous:
                print(GREEN + f"Words guessed correctly: {guessed_words}" + RESET)
            input("Press Enter to continue...")
            if not continuous:
                return

def main():
    while True:
        clear_screen()
        print("Welcome to Hangman!")
        print("1. One Shot Mode")
        print("2. Infinite Mode")
        print("3. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            hangman()
        elif choice == "2":
            hangman(continuous=True)
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()

