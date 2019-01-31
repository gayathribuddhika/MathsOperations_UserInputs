Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=5
>>> y=10
>>> x+y
15
>>> r=input("")
5
>>> r
'5'
>>> g=("enter a number:")
>>> g=input("enter a number:")
enter a number:8
>>> g
'8'
>>> g+x+y
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    g+x+y
TypeError: can only concatenate str (not "int") to str
>>> g+x
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    g+x
TypeError: can only concatenate str (not "int") to str
>>> g=input(int("enter a number:"))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    g=input(int("enter a number:"))
ValueError: invalid literal for int() with base 10: 'enter a number:'
>>> g=int(input("enter a number:"))
enter a number:4
>>> g
4
>>> g+y
14
>>> 2**4
16
>>> pow(2,4)
16
>>> pow(3,5)
243
>>> 3**5
243
>>> abs(-45)
45
>>> abs(23)
23
>>> import math
>>> math.floor(23.6)
23
>>> math.floor(5.2)
5
>>> math.sqrt(144)
12.0
>>> math.sqrt(235)
15.329709716755891
>>> p=math.sqrt
>>> p(100)
10.0
>>> k=math.floor
>>> k(12.9)
12
>>> k(2.3)
2
>>> 
