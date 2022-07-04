from calendar import formatstring
import math


example = "this is expample string for practice"
#string are array: +, we can access them by number

def strArray():

    print('string has' , len(example), 'length')

    print('em va trinh' in example)
    print('this is' in example)

    print('em va trinh' not in example)
    print('this is' not in example)

def sliceStr():
    print(example[:8])
    print(example[8:])
    print(example[-8:])

def modifyStr():
    print(example.upper())
    print(example.lower())
    print(example.strip())
    print(example.replace('this is', 'that is'))
    print(example.split(' '))

def formatStr():
    name = 'nhat'
    age = 20
    string = 'my name is {1} and my age is {0}'
    print(string.format(age, name))




c='♥'
width = 40

print ((c*2).center(width//2)*2)

for i in range(1,width//10+1):
    print (((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
           (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)

for i in range(width//4,0,-1):
    print ((c*i*4).center(width))
print ((c*2).center(width))


a = 5
c = 'H'

for i in range(a):
    print('H'.rjust(a-i,'-'),sep=',')
