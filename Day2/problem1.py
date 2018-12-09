from collections import Counter


vect = [line.strip('\n') for line in open("input.txt", "r")]

def countOccurr(ID):
	twiceOccurr = 0
	triceOccurr = 0
	splitID = list(ID)
	count = Counter(splitID)
	for x in count.values():
		if x == 2:
			twiceOccurr = 1
		if x == 3:
			triceOccurr = 1
	return (twiceOccurr, triceOccurr)

def main():
	results = []
	for x in vect:
		results.append(countOccurr(x))
	
	print(reduce((lambda x,y: [x[0]+y[0], x[1]+y[1]]), results)[0]*reduce((lambda x,y: [x[0]+y[0], x[1]+y[1]]), results)[1])
	



	
	



if __name__ == "__main__":
	main()
