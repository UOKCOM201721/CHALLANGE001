#!/usr/bin/env python3

def main():

	for i in range (1,100):
		bool1 = True
		if i % 3 == 0:
			print("Fizz", end='')
			bool1 = False

		bool2 = True
		if i % 5 == 0:
			print("Buzz", end='')
			bool2 = False

		if bool1 and bool2:
			print(i, end='')

		print('', end='\n')

if __name__ == '__main__':
	main()