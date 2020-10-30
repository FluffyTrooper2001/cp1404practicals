"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Demo os module functions."""
    starting_directory = os.getcwd()
    if starting_directory != os.path.join(os.path.dirname(starting_directory),'prac_09'):
        os.chdir('prac_09')
    print("Starting directory is: {}".format(starting_directory))
    print("Files in {}:\n{}\n".format(os.path.join(starting_directory,'Lyrics','Christmas'), os.listdir(os.path.join('Lyrics','Christmas'))))
    rename(os.path.join('Lyrics','Christmas'))
    os.chdir(starting_directory)

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    name1 = filename[:-3]
    name2=''
    for i in range(len(filename[:-4])):
        if name1[i+1].isupper() and name1[i].islower():
            name2 = name2 + name1[i] + '_'
        else:
            name2 = name2 + name1[i]
    return '_'.join([word.title() for word in name2.split(' ')]) + filename[-4:].lower()


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        rename(os.path.join(os.getcwd(),directory_name))

def rename(cd):
    go_back = os.getcwd()
    os.chdir(cd)
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        
        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)
    os.chdir(go_back)

#main()
demo_walk()
