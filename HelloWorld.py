#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

Hello World.py

Usage:

python3

'''

import  sys
import math
from datetime import datetime

def check_version():
    v= sys.version_info
    if  v.major == 3 and v.minor >=5:
        return
    print('Your current python is %d.%d. Please use Python 3.6.' % (v.major,v.minor))
    exit(1)

def input_name():

    _name = input('Please enter your name: ')
    print('Hello,', _name)


def caculate():
    _result =1024 *768
    print('1024 * 768 =%d' % (_result))

def print_test():
    print(r'''line1
    line2
    line3''')
    n = 123
    f = 456.789
    s1 = 'Hello, world'
    s2 = 'Hello, \'Adam\''
    s3 = r'Hello, "Bart"'
    s4 = r'''Hello,
    Lisa!'''

    print(n)
    print(f)
    print(s1)
    print(s2)
    print(s3)
    print(s4)

    print('%2d-%02d' % (3,122))
    print('%.2f' % 3.1415926)
    s1 = 72
    s2 = 85
    r = 100* (s2-s1)/s1
    print(r)
    print('%.1f%%' % r)

def ListTest():
    classmates =['Allen','Tom','Peter','Jim']
    print(classmates)
    print(classmates[0])
    print(classmates[1])
    print(len(classmates))
    print(classmates[len(classmates)-1])
    print(classmates[-1])
    classmates.append('Adam') #add
    print(classmates)
    classmates.pop() # delete last one
    print(classmates)
    classmates.pop(1) # i is index
    print(classmates)

    L = [
        ['Apple','Google','Microsoft'],
        ['Java','Python','Ruby','PHP'],
        ['Adam','Bart','Lisa']
    ]
    print(L[0][0])
    print(L[1][1])
    print(L[2][2])
    for x in range(len(L)):
        print(L[x][x])

def ifElse():
    w = 80.5
    h = 1.75
    r = w/(h*h)
    print(r)
    if  r<18.5:
        print('guoqing')
    elif r < 25:
        print('Normal')
    elif r <28 :
        print('OverWeight')
    elif r < 32:
        print('Fat')
    else:
        print('Fat-Fat-Fat')

def Loop():
    names =['Michael','Bob','Tracy']
    for name in names:
        print(name)

    sum =0
    for x in [1,2,3,4,5,6,7,8,9,10]:
        sum =sum+x
    print(sum)

    sum =0
    for x in range(11):
        sum=sum+x
    print(sum)

    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n -2
    print(sum)

    sum = 0
    for x in range(101):
        if x % 2 !=0:
            sum = sum + x
    print(sum)

    sum = 0
    for x in range(101):
        if x % 2 == 0:
            continue
        sum = sum + x
    print(sum)

    L = ['Bart','Lisa','Adam']
    for n  in L:
        print('Hello, %s!'%n)

    n = 0
    while n <= 100:
        if n >5:
            break
        print(n)
        n = n + 1
    print('END')

def dictAndSet():
    names =['Michael','Bob','Tracy']
    scores = [95, 76, 84]
    d = {'Micheal': 95, 'Bob':75, 'Tracy': 86}
    print(d['Bob'])

    print('allen' in d)
    print(d.get('allen'))

def areaOfCircle(x):
    PI = 3.1415926
    r = PI * x * x
    print( '%.2f'%r)

    n1 = 255
    n2 = 1000
    n1 = hex(n1)
    n2 = hex(n2)
    print(n1)
    print(n2)
def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x,y, step,angle=0):
    nx = x +step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

def quadratic(a,b,c):
    r = b * b - 4 * a * c
    if r < 0 :
        print('can not have value')
    else:
        v1 = ( -b + math.sqrt(r))/(2 * a)
        v2 = ( -b - math.sqrt(r))/(2 * a)
        print(v1,v2)

def power(x,n=2):
    s = 1
    while n >0:
        n =n-1
        s = s * x
    return s

def calc1(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

def product(*y):
    sum = 1
    for n  in y :
        sum = sum * n
    return sum

def fact(n):
    if n ==1:
        return 1
    else:
        return n + fact(n-1)

def move(n, a, b ,c):
    if n ==1:
        print('move', a, '-->',c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

def getSum():
    L = []
    n = 1
    while n <= 99:
        L.append(n)
        n = n +2
    print(L)

def getInfo():
    L  = ['Allen', 'Tom', 'Bob', 'Jack', 'Hello']
    print([L[0],L[1],L[2]])

    r =[]
    for  i in range(3):
        r.append(L[i])
    print(r)

    print(L[0:3])

    print(L[:3])
    print(L[1:3])
    print(L[-1])
    print(L[-3:])
    L = list(range(100))
    print(L)
    print(L[:10])
    print(L[-10:])
    print(L[10:20])
    print(L[:10:2])
    print(L[::5])

def trim(str):
    #return str.strip()
    n = len(str)
    if n ==0:
        return ''
    while str[0] == '':
         str = str[1:]
    while str[-1] == '':
         str = str[:-1]
    print(str)


def main():
    check_version()
    #input_name()
    #caculate()
    #print_test()
    #ListTest()
    #ifElse()
    #Loop()
    #dictAndSet()
    #areaOfCircle(5)
    #print(my_abs(-98))
    #print(move(100,100,60, math.pi /6)) # return tuple
    #quadratic(2,3,1)
    #print(power(10,3)) # hanshuo
    #print(calc1([1,2,3]))
    #print(calc1((1,2,3)))
    #print(calc2(1,3,5,7))
    #person('Allen',25)
    #person('Allen',25,city='Shanghai')
    #person('Allen',25,city='Shanghai',job='Engineer')
    #print(product(5,6,7))
    #print(fact(100))
    # move(4, 'A', 'B', 'C')
    #getSum()
    #getInfo()
    print(trim('  hello world !  '))
    print(trim('  f  '))



if __name__ =='__main__':
    main()