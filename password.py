import random
import string
from IPython.display import display, HTML

def colorful_message(message, color="black"):
    """Helper to display colorful messages in Jupyter/Colab."""
    display(HTML(f"<p style='color:{color}; font-size:16px;'>{message}</p>"))

def generate_password(length):
    if length < 4:
        colorful_message("Password length should be at least 4 characters!", "red")
        return None
    
    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    # Ensure password has at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
        random.choice(letters.upper())
    ]
    
    # Fill the rest with random choices from all sets
    all_chars = letters + digits + symbols
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Shuffle to avoid predictable placement
    random.shuffle(password)
    
    # Join into final string
    final_password = "".join(password)
    colorful_message(f"🔐 Your secure password: <b>{final_password}</b>", "green")
    return final_password

def password_generator_loop():
    colorful_message("Welcome to the Secure Password Generator!", "blue")
    while True:
        try:
            length = int(input("Enter desired password length: "))
            generate_password(length)
        except ValueError:
            colorful_message("Please enter a valid number!", "red")
            continue
        
        choice = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if choice not in ["yes", "y"]:
            colorful_message("Goodbye! Stay secure! 🔒", "purple")
            break

# Run the interactive loop
password_generator_loop()
