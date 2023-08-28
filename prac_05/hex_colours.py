COLOR_CODES = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUA": "#00ffff",
    "AQUAMARINE": "#7fffd4",
    "AZURE": "#f0ffff",
    "BEIGE": "#f5f5dc",
    "BISQUE": "#ffe4c4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#ffebcd",
    "BLUE": "#0000ff"
}

print("Color Names and Codes:")
for color_name, color_code in COLOR_CODES.items():
    print(f"{color_name} is {color_code}")

color_name_input = input("Enter a color name (or blank to exit): ").upper()

while color_name_input != "":
    color_code = COLOR_CODES.get(color_name_input)

    if color_code:
        print(f"The code for {color_name_input.lower()} is {color_code}")
    else:
        print("Invalid color name")

    color_name_input = input("Enter a color name (or blank to exit): ").upper()
