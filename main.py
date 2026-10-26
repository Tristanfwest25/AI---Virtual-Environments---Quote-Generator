import random


# Function to get a random quote from the list of quotes
quotes = [
    
    ("The best way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("Don't let yesterday take up too much of today.", "Will Rogers"),
    ("It's not whether you get knocked down, it's whether you get up.", "Vince Lombardi"),
    ("If you are working on something exciting, it will keep you motivated.", "Unknown"),
    ("Success is not in what you have, but who you are.", "Bo Bennett"),
    ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("The only limit to our realization of tomorrow is our doubts of today.", "Franklin D. Roosevelt"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Do what you can with all you have, wherever you are.", "Theodore Roosevelt"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt")
]

def get_random_quote():
    """Returns a random quote from the list of quotes."""
    quote, author = random.choice(quotes)
    return f'"{quote}" - {author}'

if __name__ == "__main__":
    """Prints a random quote when the script is run directly."""
    print(get_random_quote())