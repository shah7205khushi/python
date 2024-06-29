# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 21:59:22 2024

@author: khush
"""

#pythone datatypes

#int and float datatype

print("hello")

a=10
b=20

print(a+b)
print(a*a)

print(id(a))

print(id(b))

a=10.5678
b=20

print(a+b)

#complex datatype

c1=3.5+6j
c2=2.5+2.5j

print(c1+c2)

print(int(a))
print(float(b))

#bool datatype

a=12>4
b=3>7

print(b)
print(a)

a='hi friends'
b=20.7890065

print(id(a))

a=2344.765

print(id(a))

#list datatype

L=[12,39.90,2.5+2j,'friends']
print(L)
print(L[0])

#tuple datatype

T=(23,45.60,'cs',789076,0.0987)

print(T)
print(T[2])

#dictionary datatype

d={101:'AAA',102:'BBB',103:'CCC'}
print(d)

#set datatype

s={10,20,30,20,40,50,10,60}
print(s)

#frozenset datatype

fs=frozenset(s)
print(fs)

#range datatype

r=range(0,10,1)
print(r)

print(type(L))
print()

#loop

for i in range(0,10,1):
    print(i)
    
for i in range(11,20,2):
    print(i)
    
for i in range(11,0,-2):
    print(i)  
    
#str datatype


s="rollwala computer"

x='''rollwala computer
     center department 
     of computer science'''
     

print(s) 
print(x) 

a=123.425
s=str(a) 
print(s)

L=[10,20,30.12,'ABC']

for i in L:
    print(i)