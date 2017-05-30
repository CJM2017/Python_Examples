#!/usr/bin/python3.5
import math


primeNumberResults = []

def is_prime(num):
	prime = True
	remainder = 0
	maxCheck = math.ceil(math.sqrt(num))
	for i in range(2,maxCheck+1):
		remainder = num % i
		if not remainder:
			prime = False
			break
	if (prime):
		primeNumberResults.append(num)

def main():
	for i in range (1,10):#1000000
		is_prime(i)

	primeNumberResults.sort()
	print(primeNumberResults)


if __name__ == "__main__":
	main()