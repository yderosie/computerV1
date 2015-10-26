#!/usr/bin/python

import sys
import re
import math

def rsqrt(x):
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def sup(tab,d):
	print d
	result1 = ((-tab[1]) - rsqrt(int(d)))/(2 * tab[2])
	result2 = ((-tab[1]) + rsqrt(int(d)))/(2 * tab[2])
	print ((-tab[1]) - math.sqrt(int(d)))/(2 * tab[2])
	print ((-tab[1]) + math.sqrt(int(d)))/(2 * tab[2])
	print result1
	print result2

def egal(tab):
	result = (-tab[1]) / (2 * tab[2])
	print result

def delta(tab):
	d = (tab[1] * tab[1]) - (4 * tab[2] * tab[0])
	print d
	if d > 0:
		print "Discriminant is strictly positive, the two solutions are:"
		sup(tab, d)
	elif d == 0:
		print "The solution is:"
		egal(tab)
	else:
		print "Discriminant is strictly negative, they are not solution"

def degre_one(tab):
	result = (-tab[0])/(tab[1])
	print result

def diff(tab):
	pass

def enter():
	solve = True
	equation = str(sys.argv[1]).replace(' ', '')
	regex = re.findall("([+-]?\s*\d*[.,]?\d*\s*\*\s*[Xx]\^\d)", equation)
	print regex
	j = 0
	if regex:
		for var in regex:
			if (int(var.split('^')[1]) > j):
				j = int(var.split('^')[1])
	else:
		print "The paramettre entering is not an equation ."
		return
	print equation
	liste = equation.split('=')
	equ = re.findall("([+-]?\s*\d*[.,]?\d*\s*\*\s*[Xx]\^\d)", liste[0])
	tab = []
	i = 0
	while j >= i:
		tab.append(0.0)
		i += 1
	for var in equ:
		tab[int(var.split('^')[1])] += float(var.split('*')[0])
	egale = re.findall("([+-]?\s*\d*[.,]?\d*\s*\*\s*[Xx]\^\d)", liste[1])
	for var in egale:
		tab[int(var.split('^')[1])] -= float(var.split('*')[0])
	j = 0
	for var in enumerate(tab):
		if var[1] and int(var[0]) > j:
			j = int(var[0])
	print ("Reduced form: "),
	for t in enumerate(tab):
		if t[1]:
			print ("+ " if int(t[1]) > 0 and int(t[0] != 0) else '') + str(t[1]) + (" * X^" + str(t[0]) if int(t[0]) != 0 else ''),
	print ("= 0")
#	print ("Reduced form: "+ str(tab[0]) +" + "+ str(tab[1]) +" * X + "+ str(tab[2]) +" * X^2 = 0")
	print ("Polynomial degree:" + str(j))
	if int(j) > 2:
		print "The polynomial degree is stricly greater than 2, I can't solve."
		return
	if int(j) == 2:
		delta(tab)
	elif int(j) == 1:
		degre_one(tab)
	else:
		diff(tab)

enter()