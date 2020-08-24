finished = False
result = 0
while not finished:
    try:
        int(float(input("Please provide integer: ")))
    except:  Exception
        print("Please enter a valid integer.")
print("Valid result is: ", result)
