"""
calculates the total price of provided items.
"""

number_of_items = int(float(input("Number of items: ")))
still_going = 1
price_total=0
while still_going == 1:
    if number_of_items >= 0:
        for item in range(1,number_of_items+1):
            price_total += float(input("Price of item: "))
        print("Total price for {:d} items is ${:.2f}".format(number_of_items,price_total))
        still_going = 0
    else:
        print("Invalid number of items. Cancelled.")
        number_of_items = int(float(input("Number of items (positive integer): ")))
