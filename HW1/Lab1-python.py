'''
	Name: Brynhildur Traustadottir
	Date: 08/29/23
	Desc: Python problems set 1
'''

# 1
print()
print("Question 1")

string = input("Please enter a string: ")
k = int(input("Please enter a number: "))

for i in range(k):
	print("Hello", string)

# 2
print()
print("Question 2")

def sumCars(string):
	total = 0
	for char in string:
		total += ord(char)
	return total

inp = input("Please enter a string: ")
result = sumCars(inp)
print(inp, " = ", result)

# 3

print()
print("Question 3")

def isPrime(numb):
	if numb  <= 1:
		return False
	elif numb <= 3:
		return True
	elif numb % 2 == 0 or numb % 3 == 0:
		return False

	i = 7
	while i * i <= numb:
		if numb % i == 0 or numb % (i + 2) == 0:
			return False
		i += 6
	return True

val = input("Please enter a prime number: ")
int_val = int(val)
prime = isPrime(int_val)
print(prime)

# 4

print()
print("Question 4")

def ceasarEncrypt(inString, offset):
	ret = ""
	for i in range(len(inString)):
		c = inString[i]
		if ord(c) >= ord('a') and ord(c) <= ord('z'):
			#lowercase
			ret += chr( (((ord(c) + offset) - ord('a')) % 26) + ord('a'))
		elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
			# uppercase		
			ret += chr( (((ord(c) + offset) - ord('A')) % 26) + ord('A'))
		else:
			ret += c
		print(ret)
		return(ret)

stri = input("Please enter a string: ")
integ = input("Please enter an integer: ")
results = ceasarEncrypt(stri, int(integ))
print(results)

# 5

print()
print("Question 5")

class SwearJar(): 
	def __init__(self):
		self.data = {
			'damn' : 0,
			'crap' : 0,
			'bloody' : 0,
			'bullshit' : 0,
			'pissed' : 0,
			'shit' : 0
		}
		self.total_words = 0
		self.total_swear = 0

	def say(self, string):
		words = string.split()

		for word in words:
			self.total_words += 1
			if word in self.data:
				self.data[word] += 1
				self.total_swear += 1
			else:
				pass

	def reportCard(self):
		print(f"Total Words: {self.total_words}")
		for x in self.data.keys():
			print(f"{x}: {self.data[x]}", end = '')
			print()

		perc = self.total_swear / self.total_words * 100
		print(f"That is {perc}% profanity")

	def Soap(self):
		self.__init__()


sentence = input("Please enter an angry sentence: ")

a = SwearJar()
a.say(sentence)
a.reportCard()
a.Soap()







