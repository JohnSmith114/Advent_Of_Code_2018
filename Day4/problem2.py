
vect = [line.strip('\n') for line in open("input.txt", "r")]

def dateSort(line):
	time = line[line.find("[")+1: line.find("]")].split(" ")
	date = []
	date.append(time[0].split("-"))
	date.append(time[1].split(":"))
	return int(date[0][0]+date[0][1]+date[0][2]+date[1][0]+date[1][1])

def main():
	currGuard = 0
	vect.sort(key = dateSort)
	
	guardTime = [0 for x in range(10000)]
	asleepTime = []	
	
	for x in range(len(vect)):
		print vect[x]
		print x
		
	seenGuards = set()
	candidateGuard = 0
	candidateMinute = 0
	candidateOccurr = 0
	
	counter = 0
	
	while True:
		maxMinute = [0 for x in range(60)]
		isGuard = 0
		guardFound = 0
		for line in vect:
			hashPos = line.find("#")
			maxGuard = line.find("#"+str(currGuard)+" ")
			time = map(int, line[line.find(" ")+1: line.find("]")].split(":"))
			if currGuard == 0:
				if hashPos == -1:
					continue
				if line[hashPos+1:line.find(" ", hashPos+1)] not in seenGuards:
					currGuard = line[hashPos+1:line.find(" ", hashPos+1)]
					guardFound = 1
					isGuard = 1
				continue
			
			if guardFound == 1:
				if isGuard == 1:
					if hashPos != -1 and maxGuard == -1:
						isGuard = 0
						continue
					if hashPos == -1:
						if line.find("asleep") != -1:
							asleep = 1
							asleepTime = time
							continue
						if line.find("asleep") == -1:
							for x in range(asleepTime[1], time[1]):
								maxMinute[x] += 1
				elif maxGuard != -1:
					isGuard = 1
					continue
		if currGuard != "0":
			seenGuards.add(currGuard)
		
		print "For ", currGuard, " the minute table is ", maxMinute
		
		if max(maxMinute)>candidateOccurr:
			candidateGuard = currGuard
			candidateMinute = maxMinute.index(max(maxMinute))
			candidateOccurr = max(maxMinute)
		
		counter += 1
		print "CAND GUARD: ",candidateGuard
		print "CAND MINUTE: ",candidateMinute
		print "CAND OCCURR: ",candidateOccurr
		print "cycle no. ", counter
		print int(candidateGuard) * int(candidateMinute)
		currGuard = 0
		if guardFound == 0:
			break
		
	print seenGuards
	
	
		
		
		
	
	
if __name__ == "__main__":
	main()
