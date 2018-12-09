line = map(int, open("input.txt", "r").readline().strip('\n').split(" "))

def recSum(string):
	nChild = string[0]
	metaLen = string[1]
	cLength = 0
	cSum = 0
	tSum = 0
	startPos = 2
	while nChild > 0:
		cLength, cSum = recSum(string[startPos:])
		tSum += cSum
		startPos += cLength
		nChild -= 1
	return startPos+metaLen, tSum+sum(string[startPos: startPos+metaLen])
		
def main():
	print recSum(line)
	
if __name__ == "__main__":
	main()
