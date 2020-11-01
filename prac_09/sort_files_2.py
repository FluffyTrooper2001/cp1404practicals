import os
import shutil

def main():
    os.chdir("FilesToSort")
    categories = {}
    for filename in os.listdir('.'):
        extension = filename[filename.find('.')+1:]
        if extension not in categories:
            done = 0
            while not done:
              try:
                category = input(f"What category would you like to sort {extension} files into? ")
                assert category
              except:
                done = 0
              else:
                done = 1
            categories.update({extension: category})
            try:
                os.mkdir(category)
            except:
                pass
        else:
            category = categories[extension]
        shutil.move(filename, category)
        print(filename, "moved to", category)


main()
