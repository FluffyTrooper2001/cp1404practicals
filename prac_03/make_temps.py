from random import randint,random

def main():
    file = open("temps_input.txt",'w')
    for i in range(randint(15,30)):
        file.write("{:.15f}\n".format(random()*400-200))
    file.close()
main()
