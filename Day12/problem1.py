iVector = map(lambda x: x.strip('\n'), open("input.txt").readlines())
iVector[0] = iVector[0][15:]
iVector.pop(1)

iState = str(iVector.pop(0))
iVector = filter(lambda x: x[1]=='#', map(lambda x: x.split(" => "), iVector))

lead = 2000
end = 5000
generations = 200
iPlants = '.'*lead+iState+'.'*end

def main():
	count = 0
	for i in range(generations):
		newState = '.'*len(iPlants)
		for state in iVector:
			pos = iPlants.find(state[0], 0)
			while pos != -1:
				newState = newState[:pos+2]+state[1]+newState[pos+3:]
				pos = iPlants.find(state[0], pos+1)
		iPlants = newState
		
		oldcount = count
		count = 0
		for x in range(len(iPlants)):
			if iPlants[x]=='#':
				count += x-lead
		print count, count-oldcount
		
	#Set the generations correctly
	print "Result for part 1: ", count 
	print "Result for part 2: ", count+(50000000000-generations)*73
	
	# I found that after a few iterations (~160 for me), the value incremented by 73 every step. This means that it's useless to simulate every step after
	# the first hundred-ish ones
	
if __name__ == "__main__":
	main()
