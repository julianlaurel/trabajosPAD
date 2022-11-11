Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5-4
1
numero1=5
numero2=10
nombreAlumno="NICOLE"
numeroLetra="1234"
type(numero1)
<class 'int'>
pi=3.1416
type(pi)
<class 'float'>
type(nombreAlumno)
<class 'str'>
numeroLetra+nombreAlumno
'1234NICOLE'
print(numero1+nombreAlumno)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(numero1+nombreAlumno)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
}
prunt(numero+str(numero2))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    prunt(numero+str(numero2))
NameError: name 'prunt' is not defined. Did you mean: 'print'?

>>> 
>>> 
>>> print(nombreAlumno+str(numero2))
NICOLE10
>>> print(nombreAlumno, numero2)
NICOLE 10
>>> print(nombreAlumno,"",numero2)
NICOLE  10
>>> print(nombreAlumno,numero2,",",numero1)
NICOLE 10 , 5
>>> print("La calificacion de"+nombreAlumno+":"+str(numero2))
La calificacion deNICOLE:10
>>> print(f"El dato{numero}")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(f"El dato{numero}")
NameError: name 'numero' is not defined. Did you mean: 'numero1'?
>>> numero='1234'
>>> print(f"El dato{numero}")
El dato1234
>>> print("First line\n Second line")
First line
 Second line
>>> nombreAlumno=input("¿Cómo te llamas?")
¿Cómo te llamas?Vania
>>> print("Hola ", nombreAlumno)
Hola  Vania
>>> edad=input("¿Qué tan viejo estas?")
¿Qué tan viejo estas?14
>>> edad
'14'
>>> totalSemanas=edad*52
>>> print(totalSemanas)
14141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414
>>> edad=int(edad)
>>> totalSemanas=edad*52
>>> print(totalSemanas)
728
>>> edad=int(input("¿Qué tan viejo eres?"))
¿Qué tan viejo eres?14
>>> type(Edad)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    type(Edad)
NameError: name 'Edad' is not defined. Did you mean: 'edad'?
>>> type(edad)
<class 'int'>
