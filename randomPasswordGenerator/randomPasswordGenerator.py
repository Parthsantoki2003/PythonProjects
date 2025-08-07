
import random
import string

def generate_password():
    # Random 8-digit number
    number = random.randint(10000000, 99999999)
    
    # Generate 4 random uppercase letters
    letters = ''.join(random.choices(string.ascii_uppercase, k=4))
    
    # Combine in a unique pattern
    password = f"{letters[3]}{letters[0]}{number}{letters[1]}{letters[2]}"
    
    # Save to file
    with open("GeneratedPasswords.txt", "a") as file:
        file.write(password + "\n")
    
    return password

pwd = generate_password()
print(f"🔐 Your Generated Password: {pwd}")
