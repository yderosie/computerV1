#!/usr/bin/python

import sys
import re

#def parsing2(equation):
#	i = 0
#	while i < len(equation) and equation[i] != '-' and equation[i] != '+' and equation[i] != '=' :
#		i += 1
#	return i
#
#def parsing(equation):
#	i = j = k = 0
#	while i < len(equation):
#		liste = {}
#		i = parsing2(equation[k:]) + k + 1
#		liste[j] = equation[k:i]
#		k = i
#		print liste[j]
#		j += 1
#		print i, k, j

def delta(tab):
	d = (tab[1] * tab[1]) - 4 * tab[0] * tab[2]
	if d > 0:
		print "Discriminant is strictly positive, the two solutions are:"
		sup()
	elif d == 0:
		egal()
	else:
		pass

def enter():
	solve = True
	regex = re.compile("((?:^\s*([+-])?|\s*(?<![+-])([+-]))\s*(?:(\d+(?:\.\d*)?)\s*\*)?\s*(?<![+-])([+-])?(\d+(?:\.\d*)?)?([xX])?(?:\^(\d+))?\s*)+=((?:^\s*([+-])?|\s*(?<![+-])([+-]))|(?:(\d+(?:\.\d*)?)\s*\*)?\s*(?<![+-])([+-])?(\d+(?:\.\d*)?)?([xX])?(?:\^(\d+))?\s*)+")
	equation = str(sys.argv[1]).replace(' ', '')
	if (regex.match(equation)):
		j = 0
		parsing = re.split(r'[+=-]', equation)
		for var in parsing:
			if (int(var.split('^')[1]) > j):
				j = int(var.split('^')[1])
			if (int(var.split('^')[1]) > 2):
				solve = False	#print "The polynomial degree is stricly greater than 2, I can't solve."
	else:
		print "The paramettre entering is not an equation ."
		return
	print equation
	liste = equation.split('=')
	equ = re.split(r'[+-]', liste[0])
	tab = []
	i = 0
	while j >= i:
		tab.append(0.0)
		i += 1
	for var in equ:
		tab[int(var.split('^')[1])] += float(var.split('*')[0])
	egale = re.split(r'[+-]', liste[1])
	for var in egale:
		tab[int(var.split('^')[1])] -= float(var.split('*')[0])
	print tab
	for t in enumerate(tab):
		if t:
			print str(t[1]) + " * x^" + str(t[0]) + (" + " if int(t[0]) != j else ''),
	print ("= 0")
	print ("Reduced form: "+ str(tab[0]) +" + "+ str(tab[1]) +" * X + "+ str(tab[2]) +" * X^2 = 0")
	print ("Polynomial degree:" + str(j))
	if not solve:
		print "The polynomial degree is stricly greater than 2, I can't solve."
		return
	delta(tab)
	#parsing(equation)

enter()