# initialise filespace if working on pc, just for convenience
import os
if os.login() is 'Michael':
    os.chdir("C:\\Users\\Michael\\OneDrive\\Desktop\\misc\\prac_02")

#start of actual code

    #1
name = input("Name: ")
file = open("name.txt",'w+')
file.write(name)
file.close()
del name

    #2
file = open("name.txt",'r')
name = file.read()
print("Your name is {:s}".format(name))
file.close()
del name

    #3
numbers=open("numbers.txt",'r')
for line in range(2):
    num_out = float(numbers.readline())
    num_out += float(numbers.readline())
    print(numout)
del num_out
numbers.close()

    #4
numbers=open(input("File name: "),'r')
num_out = 0
for line in numbers:
    num_out += float(numbers.readline())
print(num_out)
