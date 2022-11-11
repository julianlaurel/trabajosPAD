Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
minutos=60
segundos=60
totalminutos=minutos*24
totalsegundos=segundos*totaliminutos
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    totalsegundos=segundos*totaliminutos
NameError: name 'totaliminutos' is not defined. Did you mean: 'totalminutos'?
totalsegundos=segundos*totalminutos
dias=int(input())
dias=int(input("¿Cuántos dias quieres?"))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dias=int(input())
ValueError: invalid literal for int() with base 10: 'dias=int(input("¿Cuántos dias quieres?"))'
>>> dias=input("¿Cuántos dias quieres?")
¿Cuántos dias quieres?12
>>> dias=int(dias)
>>> print()

>>> 

>>> 

... 
>>> 
>>> 
>>> horas=24
>>> print("en",dias,"hay",horas,totalminutos,totalsegundos)
en 12 hay 24 1440 86400
>>> print("en",dias,"hay",horas*12"horas",totalminutos*12"minutos",totalsegundos*12"segundos")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("en",dias,"hay"horas*12"horas",totalminutos*12"minutos",totalsegundos*12"segundos")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("en",dias,"hay",horas*12"horas",totalminutos*12"minutos",totalsegundos*12"segundos")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("en 12 dias hay")
en 12 dias hay
>>> print(horas,"horas")
24 horas
>>> print(horas*12,"horas")
288 horas
>>> print(totalminutos*12,"minutos")
17280 minutos
>>> print(totalsegundos*12,"segundos")
1036800 segundos
