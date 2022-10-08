import platform
import os
import random

# Console colors
RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
WHITE = '\033[0m'
BOLD = '\033[1m'

# Constant values
MIN_PASS_LENGTH = 1
MAX_PASS_LENGTH = 50
OPTIONS = {1: 'Easy to say', 2: 'Easy to read', 3: 'All characters'}
CHEER_WORDS = ['Great!', 'Awesome!', 'Amazing!', 'Good!', 'Lovely!']
AMBIGUOUS = ['l', '1', 'I', 'O', '0']

# Password Generate
LOWER_CASE = 'abcdefghijklmnopqrstuvwxyz'
UPPER_CASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SYMBOLS = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def welcome():
    os_name = platform.system()

    # Clear the terminal based on the OS name.
    if os_name == 'Windows':
        os.system('cls')
    elif os_name == 'Linux':
        os.system('clear')

    print(f'''{GREEN}{BOLD}- Welcome to PassGenTool.{WHITE}
Passwords provide the first line of defense against unauthorized access to your computer and personal information.
Computers can try thousands of passwords per second, but for this technique to be worthwhile, the malicious cyber
threat actor needs the password to be easy to identify, which is why a {BOLD}strong password matters{WHITE}.
The stronger your password, the more protected your computer will be from hackers and malicious software.
You should maintain strong and different passwords for all accounts on your computer.''')

def customize_password():
    print(f'''{YELLOW}{BOLD}- Customize your password:{WHITE}''')

    while True:
        try:
            length = input(f'{BOLD}1) {WHITE}How long would you like your password to be? (Recommended = 12 characters): ')

            if length.isdigit() == False:
                raise Exception('Password length must be an integer.')
            
            length = int(length)

            if length < MIN_PASS_LENGTH or length > MAX_PASS_LENGTH:
                raise Exception('Password length must be a number between %d and %d.' % (MIN_PASS_LENGTH, MAX_PASS_LENGTH))

            break

        except Exception as err:
            print(f'{RED}{BOLD}- Error: {WHITE}{err}')

    print(f'{GREEN}{cheer()} Let\'s continue.{WHITE}')
    
    while True:
        try:
            option = input(f'''{BOLD}2) {WHITE}Here are three types of passwords.
- Easy to say: Avoid numbers and special characters.
- Easy to read: Avoid ambiguous characters like l, 1, I, O, and 0.
- All characters: Any character combinations like !, 7, h, K, and l1.
Please choose what suits you best out of the three: ''')

            if option.isdigit() == False:
                raise Exception('Password type must be an integer.')

            option = int(option)

            if option not in OPTIONS:
                raise Exception('Password type must be 1, 2, or 3.')

            break
        except Exception as err:
            print(f'{RED}{BOLD}- Error: {WHITE}{err}')
    
    print(f'{GREEN}{cheer()} One last step.{WHITE}')

    option_based_functionality(option, length)

def cheer():
    return random.choice(CHEER_WORDS)

def option_based_functionality(option: int, length: int) -> None:
    if option == 1:
        while True:
            try:
                uppercase = str(input(f'Would you like to use {BOLD}capital {WHITE}letters? ({GREEN}Yes{WHITE} / {RED}No{WHITE}): ')).lower()

                if uppercase == 'yes':
                    lowercase = str(input(f'Would you like to use {BOLD}lower {WHITE}case letters too? ({GREEN}Yes{WHITE} / {RED}No{WHITE}): ')).lower()

                    if lowercase != 'yes' and lowercase != 'no':
                        raise Exception('Input must be either yes or no (case insensitive).')
                    break
                elif uppercase == 'no':
                    lowercase = 'yes'
                    break
                else:
                    raise Exception('Input must be either Yes or No (case insensitive).')
            except Exception as err:
                print(f'{RED}{BOLD}- Error: {WHITE}{err}')
        
        password = generate_password(length, uppercase, lowercase)

        print(f'''{check_password(length)}{password}''')
    if option == 2 or option == 3:
        while True:
            try:
                uppercase = str(input(f'Would you like to use {BOLD}capital {WHITE}letters? ({GREEN}Yes{WHITE} / {RED}No{WHITE}): ')).lower()

                if uppercase != 'yes' and uppercase != 'no':
                    raise Exception('Input must be either yes or no (case insensitive).')

                lowercase = str(input(f'Would you like to use {BOLD}lower {WHITE}case letters? ({GREEN}Yes{WHITE} / {RED}No{WHITE}): ')).lower()

                if lowercase != 'yes' and lowercase != 'no':
                    raise Exception('Input must be either yes or no (case insensitive).')
                else:
                    break
            except Exception as err:
                print(f'{RED}{BOLD}- Error: {WHITE}{err}')

        while True:
            try:
                numbers = str(input(f'Would you like to use numbers? ({GREEN}Yes{WHITE} / {RED}No{WHITE}): ')).lower()

                if numbers != 'yes' and numbers != 'no':
                    raise Exception('Input must be either yes or no (case insensitive).')
                
                break

            except Exception as err:
                print(f'{RED}{BOLD}- Error: {WHITE}{err}')

        while True:
            try:
                symbols = str(input(f'Would you like to use symbols? ({GREEN}Yes{WHITE} / {RED}No{WHITE}): ')).lower()

                if symbols != 'yes' and symbols != 'no':
                    raise Exception('Input must be either yes or no (case insensitive).')
                
                break

            except Exception as err:
                print(f'{RED}{BOLD}- Error: {WHITE}{err}')
        
        password = generate_password(length, uppercase, lowercase, numbers, symbols)

        print(f'''{check_password(length)}{password}''')

def generate_password(length, uppercase, lowercase, numbers = 'no', symbols = 'no') -> str:
    ans = ''
    
    if uppercase == 'yes':
        ans += UPPER_CASE
    
    if lowercase == 'yes':
        ans += LOWER_CASE

    if numbers == 'yes':
        ans += NUMBERS

    if symbols == 'yes':
        ans += SYMBOLS

    password = "".join(random.sample(ans, length))

    return password

def check_password(length: int) -> str:
    if length <= 3:
        return f"{RED}Dangerous Password: {WHITE}"
    elif length <= 6:
        return f"{RED}Unsafe Password: {WHITE}"
    elif length <= 8:
        return f"{YELLOW}Moderate Password: {WHITE}"
    elif length <= 11:
        return f"{GREEN}Secure Password: {WHITE}"
    else:
        return f"{GREEN}Strong Password: {WHITE}"
            

def main():
    welcome()

    customize_password()

if __name__ == '__main__':
    main()
