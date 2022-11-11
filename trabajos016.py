raining=input("esta lloviendo?")
raining=str.lower(raining)
if raining =="yes":
    windy=input("¿hay viento?")
    windy=str.lower(windy)
    if windy== "yes":
        print("hay mucho viento para una sombrilla")
    else:
        print("toma una sombrilla")
else:
    print("disfruta tu dia")