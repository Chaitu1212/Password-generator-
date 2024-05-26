import random
import string

# Function to generate a strong password
def generate_password(length):
    if length < 4:  # Ensure the minimum length is 4 to include all character types
        raise ValueError("Password length should be at least 4")

    # Character sets to include in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensuring the password has at least one character from each character set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the remaining length of the password
    if length > 4:
        all_chars = lower + upper + digits + special
        password += random.choices(all_chars, k=length-4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

# Main function to interact with the user
def main():
    print("Welcome to the Python Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
            password = generate_password(length)
            print(f"Generated password: {password}")
        except ValueError as e:
            print(e)
        
        print("Do you want to generate another password? (yes/no)")
        play_again = input().lower()
        if play_again not in ["yes", "y"]:
            break

# Run the main function
if __name__ == "__main__":
    main()
