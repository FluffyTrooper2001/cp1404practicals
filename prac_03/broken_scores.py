"""
CP1404/CP5632 - Practical
Not broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    print(get_score(score))

def get_score(score):
    if score < 0  or score > 100:
        result = "Invalid score."
    elif score < 50:
        result = "Bad."
    elif score >= 90:
        result = "Excellent."
    else:
        result = "Passable."
    return result
main()
