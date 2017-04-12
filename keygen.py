#!/usr/bin/env python3
# Nathaniel Baylon
# CMSC441 Marron
# Spring 2017
from sys import argv
import random
from datetime import datetime

# 2 ** -PRIME_PROB_EXP === prime error
PRIME_PROB_EXP = 100

# Valid input is positive integer
def validateInput(argc, argv):
	if argc != 2 or not argv[1].isdigit():
		print("usage: python keygen.py <modulus size>")
		exit()

# find r, d such that 2 ** r * d === num
def factorPow2(num):
	r = 0
	d = num
	while d % 2 != 0:
		d /= 2
		r += 1 
	return r, d
# Primalilty test, return True for prime, False for composite
# expects testNum > 2
def millerRabin(n):
	# all even numbers are composite
	if n % 2 == 0:
		return False
	s = PRIME_PROB_EXP // 2
	r, d = factorPow2(n - 1)
	# s itertions for error of 2 ** -PRIME_PROB_EXP	
	for i in range(s):
		continueOuter = False
		a = random.randint(2, n - 2)
		x = pow(a, d, n)
		if x == 1 or x == n - 1:
			continue
		for j in range(r - 1):
			x = pow(x, 2, n)
			if x == 1:
				return False
			if x == n - 1:
				continueOuter = True
				break
		if continueOuter:
			continue
		return False
	return True

# try random numbers until prime probably found
def getLargePrime(bitSize):
	primeSize = bitSize // 2
	upperBound = 2 ** primeSize
	lowerBound = 2 ** (primeSize - 1)
	while True:
		testPrime = random.randint(lowerBound, upperBound)
		if millerRabin(testPrime):
			return testPrime
# def getLargeProduct():

def main(argc, argv):
	validateInput(argc, argv)
	modulusSize = int(argv[1])
	random.seed(datetime.now())
	p = getLargePrime(modulusSize)
	q = getLargePrime(modulusSize)
	n = p * q
	print("P: " + str(p))
	print("Q: " + str(q))
	print("N: " + str(n))

	#generate P and Q, such that their product, N is 

if __name__ == "__main__":
	main(len(argv), argv)