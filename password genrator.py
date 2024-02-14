import random
import string

def generate_password(length=12):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password using random.choice to select characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage:
generated_password = generate_password()
print("Generated Password:", generated_password)
