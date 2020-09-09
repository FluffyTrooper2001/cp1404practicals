def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = input("How many months? ")
    while not number_of_months.isdigit():
        number_of_months = input("Please enter a valid integer.\nHow many months?")
    number_of_months = int(number_of_months)
    for i in range(number_of_months):
        done = False
        while not done:
            try:
                income = float(input("Enter income for month {}: ".format(i+1)))
                done = True
            except ValueError:
                print("Please enter a valid float.")
        incomes.append(income)
    print_report(incomes)

def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(len(incomes)):
        income = incomes[month]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()
