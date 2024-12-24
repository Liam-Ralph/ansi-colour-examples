# Foreground/Background Selection
color_background = True
position_control = "48"
if not color_background:
    position_control = "38"


# First Sixteen Colors
for i in range(16):
    print("\u001b[" + position_control + ";5;" + str(i) + "m " + str(i) + " ", end = "")
    if i < 10:
        print(" ", end = "")

print("\u001b[0m")

# Remaining Colors
for i in range(16, 256):

    # Print the color, extra space if needed
    print("\u001b[" + position_control + ";5;" + str(i) + "m " + str(i) + " ", end = "")
    if i < 100:
        print(" ", end = "")

    # New line every 36 colors, adjust for the first 16
    if (i - 15) % 36 == 0:
        print("\u001b[0m")

print("\u001b[0m")