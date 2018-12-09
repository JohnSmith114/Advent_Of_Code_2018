def main():
	inputFile = open("inputgiuz.txt","r")
	inputString = list(inputFile.readline().strip('\n'))
	
	
	while True:
		changed = 0
		for x in range(len(inputString)-1):
			if inputString[x].lower()==inputString[x+1].lower() and ((inputString[x].istitle() and not inputString[x+1].istitle())or(not inputString[x].istitle() and inputString[x+1].istitle())):
				inputString[x]='0'
				inputString[x+1]='0'
				changed = 1
				
		counter = 0
		for x in list(inputString):
			if x == '0':
				counter += 1
		for x in range(counter):
			inputString.remove('0')
				
		print inputString
		if changed == 0:
			break
	print "length: ", len(inputString)
		

if __name__ == "__main__":
	main()
