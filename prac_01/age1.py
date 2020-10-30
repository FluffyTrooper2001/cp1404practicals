def floor(x):
    if x>=0:
        return int(x)
    else:
        return int(x-1)
is_valid=0
while is_valid==0:
    age_raw = input("Age >")
    try:
        age = floor(float(age_raw))
        if age >= 0 and age < 150:
            is_valid=1
    except:
        pass
if float(age_raw)-age!=0:
    print(age)
if age/2 - int(age/2) == 0:
    print("Even")
else:
    print("Odd")
