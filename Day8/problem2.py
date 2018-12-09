line = map(int, open("input.txt", "r").readline().strip('\n').split(" "))

def recSum(string):
	nChild = string[0]
	metaLen = string[1]
	cLength = 0
	cSum = 0
	tSum = 0
	cValues = []
	startPos = 2
	i = nChild
	
	while i > 0:
		cLength, cSum = recSum(string[startPos:])
		cValues.append(cSum)
		startPos += cLength
		i -= 1
		
	if nChild == 0:
		tSum = sum(string[startPos: startPos+metaLen])
	else:
		for x in range(metaLen):
			req = string[startPos+x]
			print req, nChild
			if not(req == 0 or req>nChild):
				tSum += cValues[req-1]
	
	return startPos+metaLen, tSum
		
def main():
	print recSum(line)
	
if __name__ == "__main__":
	main()
