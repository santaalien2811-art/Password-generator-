is_running = True
import random
import string
while is_running:
    try:
        Lenght = int(input("Please enter the password lenght: "))

        chars = string.ascii_letters
        chars += string.digits
        chars += string.punctuation

        password = ''.join([random.choice(chars) for i in range(Lenght)])
        print(f"Your password is {password} ")
        is_running = False
    except ValueError:
        print("Lenght must be a number")    