
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
	
	for line in vect:
		hashPos = line.find("#")
		if hashPos == -1:
			time = map(int, line[line.find(" ")+1: line.find("]")].split(":"))
			if line.find("asleep") != -1:
				asleep = 1
				asleepTime = time
			if line.find("asleep") == -1:
				guardTime[currGuard] += time[1] - asleepTime[1]
			continue
		currGuard = int(line[hashPos+1:line.find(' ',hashPos+1)])
		asleep = 0
		
	print guardTime
	
	print "guard: ",guardTime.index(max(guardTime))
	print "time: ",max(guardTime)
	
	maxMinute = [0 for x in range(60)]
	
	isGuard = 0
	asleepTime = []
	
	for line in vect:
		hashPos = line.find("#")
		maxGuard = line.find("#"+str(guardTime.index(max(guardTime))))
		time = map(int, line[line.find(" ")+1: line.find("]")].split(":"))
		
		
		print line
		
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
					print time
					print asleepTime
					for x in range(asleepTime[1], time[1]):
						print x
						maxMinute[x] += 1
		elif maxGuard != -1:
			print "guard found: ", time
			isGuard = 1
			continue
	
	print maxMinute
	
	print "Minute: ",maxMinute.index(max(maxMinute))
	print "times: ",max(maxMinute)
	print guardTime.index(max(guardTime))*maxMinute.index(max(maxMinute))
		
		
		
	
	
if __name__ == "__main__":
	main()
