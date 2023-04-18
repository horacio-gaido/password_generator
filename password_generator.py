import os
import string
import secrets
import getpass

os.system("cls")

# Function to ask a question and receive either just `yes` or `no`
def ask_question(question: str):
    while True:
        answer = input(f"{question} -> ").lower()
        if answer in ("yes", "no"):
            return answer
        else:
            print("Please type 'yes' or 'no'")

# Recognizing user decisions about the password
boolean_upper_lowercase = ask_question("Before we create a secure password for you, we kindly request that you answer the following questions. \nWould you like the password to include both upper and lower case letters? Please respond with either 'yes' or 'no'. ")
boolean_digits = ask_question("Would you like the password to include numbers? Please respond with either 'yes' or 'no'. ")
boolean_symbols = ask_question("Would you like the password to include symbols? Please respond with either 'yes' or 'no'. " )
while True:
    try:
        size = int(input("Please specify the desired number of characters for the password -> "))
        break
    except ValueError:
        print("Please input an integer number only...")

# Declaring possible characters of password
characters = string.printable[:-6]  # Excludes whitespace and quotes

# Generating the password
## Setting all characters available for password and including one of every type into the password
password = [secrets.choice(string.ascii_lowercase)]

if boolean_upper_lowercase == "yes":
    password.append(secrets.choice(string.ascii_uppercase))

if boolean_digits == "yes":
    password.append(secrets.choice(string.digits))

if boolean_symbols == "yes":
    password.append(secrets.choice(string.punctuation))

## Including characters left needed
password += [secrets.choice(characters) for _ in range(size - len(password))]

secrets.SystemRandom().shuffle(password)

print("Your password is:")
print("".join(password))
