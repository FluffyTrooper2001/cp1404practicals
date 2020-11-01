import os
import shutil

def main():
    os.chdir("FilesToSort")
    sort_dict = {}
    for filename in os.listdir('.'):
        extension = filename[filename.find('.')+1:]
        if extension not in os.listdir('.'):
            sort_dict.update({extension:[filename]})
        else:
            sort_dict[extension].append(filename)
    for dir_name, filenames in sort_dict.items():
        try:
            os.mkdir(dir_name)
        except:
            pass
        for filename in filenames:
            shutil.move(filename, dir_name)
