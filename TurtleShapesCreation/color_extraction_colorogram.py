import colorgram

colors=colorgram.extract("image1.jpg",1000)

colors_list=[]

for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_tup=(r,g,b)

    colors_list.append(new_tup)
print(colors_list)