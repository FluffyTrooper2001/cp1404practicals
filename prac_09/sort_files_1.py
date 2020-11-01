import os
import shutil

def main():
    os.chdir("FilesToSort")
    sort_dict = {}
    extensions = []
    for filename in os.listdir('.'):
        extension = filename[filename.find('.')+1:]
        if extension not in extensions:
            extensions.append(extension)
            sort_dict.update({extension:[filename]})
        else:
            sort_dict[extension].append(filename)
    print(sort_dict)
    for dir_name, filenames in sort_dict.items():
        print(f"Moving {filenames} to {dir_name}")
        try:
            os.mkdir(dir_name)
            print(dir_name, "made")
        except:
            pass
        for filename in filenames:
            shutil.move(filename, dir_name)
            print(filename, "moved to", dir_name)

main()
