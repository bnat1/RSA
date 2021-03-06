# Nathaniel Baylon
# Spring 2017
# CMSC441

from sys import argv
import random
from datetime import datetime

# 2 ** -PRIME_PROB_EXP === prime error probability
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

#return two primes
def getTwoPrimes(bitSize):
	p = -1
	q = -1
	while p == q:
		p = getLargePrime(bitSize)
		q = getLargePrime(bitSize)
	return p, q

# return gcd(a, b), x, and y, such that gcd(a, b) = ax + by
# best if a > b
def extendedEuclid(a, b):
	if b == 0:
		# a = a * 1 + b * 0
		return a, 1, 0
	d, x, y = extendedEuclid(b, a % b)
	return d, y, x - a // b * y 

# returns d s.t. d === a^-1  (mod m)
def modMulInv(a, m):
	g, x, y = extendedEuclid(a, m)
	# ax + my = 1 (mod m)
	# Note: my = 0 (mod m) 
	# x = a^-1 (mod m)
	return x % m

#apply a key to a message in numerical form
def applyKey(x, exponent, modulus):
	return pow(x, exponent, modulus)

#convert a string message to a number (ascii)
def stringToNum(message):
	x = 0
	for c in message:
		x = x << 8
		x = x ^ ord(c)
	return x

#convert a numerical message back to its ascii form
def numToString(x):
	message = ""
	while x > 0:
		message = chr(x & 255) + message
		x = x >> 8
	return message

def main(argc, argv):
	validateInput(argc, argv)
	modulusSize = int(argv[1])
	random.seed(datetime.now())
	# make sure phi and e have a gcd of 1
	goodPrivateKey = False
	e = 2 ** 16 + 1
	ePhiGCD = -1
	while ePhiGCD != 1:
		p, q = getTwoPrimes(modulusSize)
		n = p * q
		phiOfN = (p - 1) * (q - 1)
		ePhiGCD, x, y = extendedEuclid(e, phiOfN)

	d = modMulInv(e, phiOfN)
 		
	print("Public Key (e, n): (" + str(e) + ", " + str(n) + ')\n')
	print("Private Key (d, n): (" + str(d) + ", " + str(n) + ')\n')

if __name__ == "__main__":
	main(len(argv), argv)