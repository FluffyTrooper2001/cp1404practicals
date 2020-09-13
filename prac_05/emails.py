def main():
    EMAILS_TO_NAMES = {}
    email = input("Email: ")
    while email != '':
        name = get_name(email)
        EMAILS_TO_NAMES.update({email: name})
        email = input("Email: ")
    print_names_and_emails(EMAILS_TO_NAMES)

def get_name(email):
    if email.find('@') > 0:
        name = email[:email.find('@')].replace('.',' ').title()
        is_name = input("Is your name {}? (Y/n)".format(name)).lower()
        if is_name == 'n':
            is_name = False
        elif is_name == '' or is_name == 'y':
            is_name = True
    else:
        is_name = False
    if not is_name:
        name = input("Name: ")
    return name

def print_names_and_emails(EMAILS_TO_NAMES):
    for email in EMAILS_TO_NAMES:
        print("{} ({})".format(EMAILS_TO_NAMES[email],email))

main()
