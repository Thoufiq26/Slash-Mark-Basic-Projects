import random

def generate_passwords(lengths):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for length in lengths:
        password = ''.join(random.choice(alphabet) for _ in range(length))
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)
        passwords.append(password)
    
    return passwords

def replace_with_number(password):
    num_replacements = random.randint(1, 2)  # replace 1 or 2 characters with numbers
    for _ in range(num_replacements):
        replace_index = random.randrange(len(password) // 2)
        password = password[:replace_index] + str(random.randint(0, 9)) + password[replace_index + 1:]
    return password

def replace_with_uppercase_letter(password):
    num_replacements = random.randint(1, 2)  # replace 1 or 2 characters with uppercase letters
    for _ in range(num_replacements):
        replace_index = random.randrange(len(password) // 2, len(password))
        password = password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]
    return password

def main():
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        if num_passwords <= 0:
            print("Number of passwords should be greater than 0.")
            return

        print("Generating " + str(num_passwords) + " passwords")

        password_lengths = []
        print("Minimum length of password should be 3")

        for i in range(num_passwords):
            while True:
                length = int(input(f"Enter the length of Password #{i + 1} (minimum 3): "))
                if length < 3:
                    print("The length is too short, setting to the minimum length of 3.")
                    length = 3
                password_lengths.append(length)
                break  # valid length entered, exit the loop

        passwords = generate_passwords(password_lengths)

        for i, password in enumerate(passwords):
            print(f"Password #{i + 1} = {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
