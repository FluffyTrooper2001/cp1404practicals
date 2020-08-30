"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)

def main():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            result = celsius_to_farenheit(celsius)

        elif choice == "F":
            farenheit = float(input("Farenheit: "))
            result = farenheit_to_celsius(farenheit)

        else:
            result = "Invalid option"
        print("{:s}\n{:s}".format(result,MENU))
        
        choice = input("> ").upper()
    print("Thank you.")

def celsius_to_farenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    result = "Result: {:.2f} F".format(fahrenheit)
    return result
def farenheit_to_celsius(farenheit):
    celsius = 5 / 9 * (farenheit - 32)
    result = "Result: {:.2f} C".format(celsius)
    return result
main()
