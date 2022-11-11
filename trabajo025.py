name=input("pon tu primer nombre:")
if len(name)<5:
    surname=input("pon tu apellido:")
    name=name+surname
    print(name.upper())
else:
    print(name.lower())
    