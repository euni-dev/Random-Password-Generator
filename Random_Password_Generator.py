import random
import string

# Generate random password
def generate_password(length=8):
   characters = string.ascii_letters + string.digits + string.punctuation
   password = ''.join(random.choice(characters) for i in range(length))
   return password

password_length_str = input("Enter password length: ")
if password_length_str:
    password_length = int(password_length_str)
else:
    password_length = 8

password = generate_password(password_length)
print(f"Generated password is: {password}")