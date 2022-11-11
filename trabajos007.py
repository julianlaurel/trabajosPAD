Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nombre=input("¿Cómo te llamas?")
¿Cómo te llamas?Julian
>>> edad=int(input("¿Cuántos años tienes?"))
¿Cuántos años tienes?16
>>> cumpleaños=1+edad
>>> print("el cumplira",edad,"años")
el cumplira 16 años
>>> cumpleaños=edad+1
>>> print("el cumplira",edad,"años")
el cumplira 16 años
>>> cumpleaños= edad + 1
>>> print(nomnbre,"el cumplira",edad,"años")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(nomnbre,"el cumplira",edad,"años")
NameError: name 'nomnbre' is not defined. Did you mean: 'nombre'?
>>> NameError: name 'nombre' is not defined. Did you mean: 'nombre'?
SyntaxError: invalid syntax
>>> print(nombre,"el cumplira",edad,"años")
Julian el cumplira 16 años
