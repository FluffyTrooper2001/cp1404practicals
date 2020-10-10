from guitar import Guitar
import math
def main():
    done = False
    guitars = []
    print("My guitars!")
    while not done:
        name = input("Name: ")
        if not name:
            break
        else:
            try:
                year = int(input("Year: "))
                if not year:
                    raise Exception
            except:
                year = 0
            try:
                cost = float(input("Cost: $"))
                if not cost:
                    raise Exception
            except:
                cost = 0
            guitars.append(Guitar(name, year, cost))
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i:>{math.ceil(math.log(len(guitars),10))}}: {str(guitar): <{len(max(str(guitar) for guitar in guitars))}s}", '(vintage)' if guitar.is_vintage() else '')

main()
