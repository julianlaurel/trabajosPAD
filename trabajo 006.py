Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #variable
>>> 
>>> rebanadas=int(input("¿con cuántas rebanas empezaste?"))
¿con cuántas rebanas empezaste?
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    rebanadas=int(input("¿con cuántas rebanas empezaste?"))
ValueError: invalid literal for int() with base 10: ''
>>> rebanadas=int(input("¿con cuántas rebanadas empezaste?"))
¿con cuántas rebanadas empezaste?2
>>> print("me quedan"(16-rebanadas))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print("me quedan"(16-rebanadas))
TypeError: 'str' object is not callable
>>> print("me quedan"(16-int rebanadas))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("me quedan"+(16-rebanadas)+"rebanadas")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print("me quedan"+(16-rebanadas)+"rebanadas")
TypeError: can only concatenate str (not "int") to str
>>> print("me quedan"+(16-int rebanadas)+"rebanadas")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("me quedan", 16-int(rebanadas),"rebanadas)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("me quedan", 16-int(rebanadas),"rebanadas")
...       
me quedan 14 rebanadas
