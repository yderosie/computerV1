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

def delta(ax,bx,c):
	pass

def enter():
	regex = re.compile("((?:^\s*([+-])?|\s*(?<![+-])([+-]))\s*(?:(\d+(?:\.\d*)?)\s*\*)?\s*(?<![+-])([+-])?(\d+(?:\.\d*)?)?([xX])?(?:\^(\d+))?\s*)+=((?:^\s*([+-])?|\s*(?<![+-])([+-]))|(?:(\d+(?:\.\d*)?)\s*\*)?\s*(?<![+-])([+-])?(\d+(?:\.\d*)?)?([xX])?(?:\^(\d+))?\s*)+")
	equation = str(sys.argv[1]).replace(' ', '')
	if (regex.match(equation)):
		j = 0
		parsing = re.split(r'[+=-]', equation)
		for var in parsing:
			if (int(var.split('^')[1]) > j):
				j = int(var.split('^')[1])
			if (int(var.split('^')[1]) > 2):
				print "The polynomial degree is stricly greater than 2, I can't solve."
				return
	else:
		print "Le paramettre entrer ne correspond pas a une equation."
		return

	print equation
	liste = equation.split('=')
	equ = re.split(r'[+-]', liste[0])
	tab = [0.0, 0.0, 0.0]
	tab2 = [0.0, 0.0, 0.0]
	for var in equ:
		tab[int(var.split('^')[1])] = float(var.split('*')[0])
	egale = re.split(r'[+-]', liste[1])
	for var in egale:
		tab2[int(var.split('^')[1])] = float(var.split('*')[0])
	tab[0] = tab[0] - tab2[0]
	tab[1] = tab[1] - tab2[1]
	tab[2] = tab[2] - tab2[2]
	print ("Reduced form: "+ str(tab[0]) +" + "+ str(tab[1]) +" * X + "+ str(tab[2]) +" * X^2 = 0")
	print ("Polynomial degree:" + str(j))
	delta(tab[2],tab[1],tab[0])
	#parsing(equation)

enter()