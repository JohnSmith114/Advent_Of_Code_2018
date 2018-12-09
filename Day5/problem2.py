def main():
	inputFile = open("input.txt","r")
	iString = list(inputFile.readline().strip('\n'))
	alphabet=list("abcdefghijklmnopqrstuvwxyz")
	least = 10000000000000000000000
	
	for letter in alphabet:
		print "CURRENT LETTER: ",letter
		inputString = list(iString)
		c1 = 0
		for x in range(len(inputString)):
			if inputString[x].lower()==letter:
				print("k")
				inputString[x] = '0'
		for x in list(inputString):
				if x == '0':
					c1 += 1
		for x in range(c1):
			inputString.remove('0')
		print "mod: ", inputString
		
		while True:
			changed = 0
			counter = 0
			
			for x in list(inputString):
				if x == '0':
					counter += 1
			for x in range(counter):
				inputString.remove('0')
			for x in range(len(inputString)-1):
				if inputString[x].lower()==inputString[x+1].lower() and ((inputString[x].istitle() and not inputString[x+1].istitle())or(not inputString[x].istitle() and inputString[x+1].istitle())):
					inputString[x]='0'
					inputString[x+1]='0'
					changed = 1
			print inputString
			
			if changed == 0:
				break
		if len(inputString)<least:
			least = len(inputString)
	
	print least
		

if __name__ == "__main__":
	main()
