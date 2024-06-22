# Assuming the conversion_table and rgb_to_hex() functions are defined correctly
conversion_table = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF"
}

keys = ["red", "green", "blue"]
r, g, b = 255, 0, 0

# Printing the formatted string
print("{} {}".format(conversion_table[keys[i].text], rgb_to_hex((r,g,b))))
