import random

print(random.randint(5, 20))  # line 1
# inclusive of 5 and 20.
print(random.randrange(3, 10, 2))  # line 2
# 3 to 9; cannot produce 4.
print(random.uniform(2.5, 5.5))  # line 3
# could be inclusive, but the odds are practically negligible.
print(random.randint(1, 100))
