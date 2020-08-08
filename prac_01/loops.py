for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0,100,10):
    print(i, end=' ')
print()

# b.
for i in range(20,1,-1):
    print(i, end=' ')
print()

# c.
n = int(float(input("Stars: ")))
for i in range(1,n+1): #+1 to fix bug.
    print('*', end='')
print()

for i in range(1,n+2): #+2 to fix bug. idk y it wrks.
    for j in range(1,i):
        print('*', end='')
    print()
