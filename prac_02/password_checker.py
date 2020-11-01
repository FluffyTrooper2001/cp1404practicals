"""
CP1404 - Practical 2
"""

MIN_LENGTH = 4
MAX_LENGTH = 14
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
  


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""

    bad_password = False # initial value
    if len(password)>MAX_LENGTH or len(password)<MIN_LENGTH:
        bad_password = True
    elif password.isdigit() or password.isupper() or password.islower():
        bad_password = True # opportunity to skip loop for speed
    else:     
        count_digit = 0
        count_lower = 0
        count_upper = 0
        if SPECIAL_CHARS_REQUIRED: # determine if lack of special characters can return a False
            count_special = 0
        else:
            count_special = 1 # add a virtual char to meet the requirements
               
        for char in password:
            if char.isdigit():
                count_digit += 1
            if char in SPECIAL_CHARACTERS:
                count_special += 1
            if char.isupper():
                count_upper += 1
            if char.islower():
                count_lower += 1
            
        bad_password = not count_digit or not count_special or not count_lower or not count_upper
    return not bad_password # returns true if not a bad password

main()
