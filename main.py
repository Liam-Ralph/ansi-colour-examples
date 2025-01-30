# Foreground/Background Selection
color_background = True
position_control = "48"
if not color_background:
    position_control = "38"


# First Sixteen Colors
for i in range(16):
    print(f"\u001b[{position_control};5;{i}m{str(i).rjust(4)} ", end = "")

print("\u001b[0m")

# Remaining Colors
for i in range(16, 256):

    # Print the color
    print(f"\u001b[{position_control};5;{i}m{str(i).rjust(4)} ", end = "")

    # New line every 36 colors, adjust for the first 16
    if (i - 15) % 36 == 0:
        print("\u001b[0m")

print("\u001b[0m")