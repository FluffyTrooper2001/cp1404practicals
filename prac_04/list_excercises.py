def main():
    print("Basic list operations")
    numbers = []
    for i in range(5):
        done = False
        while not done:
            try:
                number = float(input("Number: "))
                if number == int(number):
                    number = int(number)
                done = True
            except ValueError:
                print("Please input a valid number.")
        numbers.append(number)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))

def security_checker():
    print("\nWoefully inadequate security checker")
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Please enter username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

main()
security_checker()
# input("Ok:")
