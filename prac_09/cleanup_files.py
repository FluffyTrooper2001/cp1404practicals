"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))
    print("Files in {}:\n{}\n".format(os.path.join(os.getcwd(),'Lyrics/Christmas'), os.listdir('Lyrics/Christmas')))
    rename('Lyrics/Christmas')

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


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
    for filename in os.listdir(cd):
        if os.path.isdir(filename):
            continue
        
        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)
    os.chdir(go_back)

main()
demo_walk()
