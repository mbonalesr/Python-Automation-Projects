import colorgram

# extracting colors rgb from image
colors = colorgram.extract('hirst.jpg', 30)
print(colors)


all_colors = []


for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]


    clean_color = (r,g,b)
    all_colors.append(clean_color)


print(all_colors)

