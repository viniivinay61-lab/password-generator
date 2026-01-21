import random
import string

def generate_password(length):
    # Ensure length is at least 3
    length = max(length, 3)
    
    # 1. Start with one lowercase, one uppercase, and one digit 
    # This guarantees the password meets requirements every time
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]

    # 2. Fill the rest of the length with random letters
    all_characters = string.ascii_letters + string.digits
    for _ in range(length - 3):
        password.append(random.choice(all_characters))

    # 3. Shuffle the list so the required characters aren't always at the start
    random.shuffle(password)

    return "".join(password)

def main():
    try:
        num = int(input("How many passwords? "))
        for i in range(num):
            length = int(input(f"Length of password #{i+1}: "))
            print(f"Password #{i+1}: {generate_password(length)}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()