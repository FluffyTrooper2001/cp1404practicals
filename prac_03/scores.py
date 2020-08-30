from random import randint

def main():
    num_scores = int(float(input("Number of scores: ")))
    file = open("results.txt",'w+')
    for i in range(num_scores):
        random_integer = randint(0,100)
        file.write("{:d} is {:s}\n".format(random_integer,get_score(random_integer)))
    file.close()
    file = open("results.txt",'r')
    print(file.read())
    file.close()

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
