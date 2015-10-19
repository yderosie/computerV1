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
		print 'ok'
		i = j = 0
		while i < len(equation):
			if equation[i] == '^' and int(equation[i + 1]) > 2 and int(equation[i + 1] >= 0):
				print "Equation de degre trop elevee."
				return
			if equation[i] == '^' and int(equation[i + 1]) > j:
				j = int(equation[i + 1])
			i += 1
	else:
		print "Le paramettre entrer ne correspond pas a une equation."
		return
	
	print equation
	liste = equation.split('=')
	equ = re.split(r'[+-]', liste[0])
	#c = ax = bx = 0
	tab = [(0,""), (1,""), (2,"")]
	print tab
	for var in equ:
#		print var
		tab[var.split('^').[1]] = var.split('*').[0]

	#	if var.count('x^0') or var.count('X^0'):
	#		c = var[::-1]
	#		c = c[4:]
	#		c = c[::-1]
	#	elif var.count('x^1') or var.count('X^1'):
	#		bx = var[::-1]
	#		bx = bx[4:]
	#		bx = bx[::-1]
	#	elif var.count('x^2') or var.count('X^2'):
	#		#ax = var[::-1]
	#		#ax = ax[4:]
	#		#ax = ax[::-1]
	#		ax = var[:-4]
	print tab
#	print equ
	if liste[1].find('X^0') or liste[1].find('x^0'):
		egale = liste[1][::-1]
		egale = egale[4:]
		egale = egale[::-1]
#	print liste
#	print egale
#	print ax
#	print bx
#	print c
	c = int(c) - int(egale)
#	print c
	print ("Reduced form: "+ str(c) +" + "+ str(bx) +" * X + "+ str(ax) +" * X^2 = 0")
	print ("Polynomial degree:" + str(j))
	delta(ax,bx,c)
	#parsing(equation)

enter()