COLOUR_NAME_TO_HEX = ["aliceblue": "#f0f8ff",
                      "antiquewhite": "#faebd7",
                      "aquamarine1": "#7fffd4",
                      "azure1": "#f0ffff",
                      "beige": "#f5f5dc",
                      "bisque1": "#ffe4c4",
                      "black": "#000000",
                      "blanchedalmond": "#ffbcd",
                      "blue1": "#0000ff",
                      "blueviolet": "#8a2be2"]
name = input("Enter name: ").lower()
if name in COLOUR_NAME_TO_HEX:
    print("Hex code: {}".format(COLOUR_NAME_TO_HEX[name]))
else:
    print("{} not found in dictionary.".format(name))
while name != '':
    name = input("Enter name: ").lower()
    if name in COLOUR_NAME_TO_HEX:
        print("Hex code: {}".format(COLOUR_NAME_TO_HEX[name]))
    else:
        print("{} not found in dictionary.".format(name))
