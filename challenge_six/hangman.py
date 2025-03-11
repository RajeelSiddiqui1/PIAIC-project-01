import random

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
         |
         |
    ======""",
    """
     +---+
     O   |
         |
         |
         |
         |
    ======""",
    """
     +---+
     O   |
     |   |
         |
         |
         |
    ======""",
    """
     +---+
     O   |
    /|   |
         |
         |
         |
    ======""",
    """
     +---+
     O   |
    /|\  |
         |
         |
         |
    ======""",
    """
     +---+
     O   |
    /|\  |
    /    |
         |
         |
    ======""",
    """
     +---+
     O   |
    /|\  |
    / \  |
         |
         |
    ======"""
]


WORDS = [
    # Things (objects, animals, etc.)
    "apple", "bicycle", "cat", "dragon", "elephant", "flower", "guitar", 
    "hammer", "island", "jacket", "kangaroo", "lamp", "mountain", "notebook", 
    "ocean", "pencil", "quartz", "rocket", "snake", "tiger", "umbrella", 
    "volcano", "whale", "xylophone", "yacht", "zebra",
    # People's names
    "alice", "bob", "charlie", "david", "emma", "frank", "grace", "henry", 
    "isabella", "jack", "kate", "liam", "mia", "noah", "olivia", "peter", 
    "quinn", "rose", "sam", "tina", "victor", "wendy", "xavier", "yara", "zach"
]

def get_word():
    """Pick a random word from the list."""
    return random.choice(WORDS).upper()

def display_game(hangman_state, guessed_letters, word_progress):
    """Show the current game state."""
    print(HANGMAN_PICS[hangman_state])
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("Word:", " ".join(word_progress))
    print()

def play_hangman():
    """Main game logic with 6 tries."""
    print("Welcome to Hangman!")
    print("Guess the word (things or names) within 6 wrong tries!")
    
    while True:
        # Initialize game state
        word = get_word()
        word_progress = ["_"] * len(word)
        guessed_letters = set()
        hangman_state = 0
        max_guesses = 6  

       
        while hangman_state < max_guesses and "_" in word_progress:
            display_game(hangman_state, guessed_letters, word_progress)
            
            
            guess = input("Guess a letter: ").upper()
            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single letter!")
                continue
            
            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue
            
            guessed_letters.add(guess)
            
            # Check if guess is in word
            if guess in word:
                print("Good guess!")
                for i, letter in enumerate(word):
                    if letter == guess:
                        word_progress[i] = guess
            else:
                print("Wrong guess!")
                hangman_state += 1

        display_game(hangman_state, guessed_letters, word_progress)
        if "_" not in word_progress:
            print(f"Congratulations! You won! The word was: {word}")
        else:
            print(f"Game Over! You lost after 6 wrong guesses. The word was: {word}")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_hangman()