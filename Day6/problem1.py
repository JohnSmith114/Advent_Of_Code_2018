from collections import Counter

posVector = [map(int,lines.strip('\n').split(", ")) for lines in open("input.txt")]

def getRectDim():
	maxX = posVector[0][0]
	maxY = posVector[0][1]
	minX = posVector[0][0]
	minY = posVector[0][1]
	for coord in posVector:
		maxX = max(maxX, coord[0])
		maxY = max(maxY, coord[1])
		minX = min(minX, coord[0])
		minY = min(minY, coord[1])
	return maxX, maxY, minX, minY

def getNearestPoint(coord):
	distVector = map(lambda x: abs(x[0]-coord[0])+abs(x[1]-coord[1]), posVector)
	distCounter = Counter(distVector)
	if distCounter[min(distVector)]>1:
		return -1
	else:
		return distVector.index(min(distVector))

def main():
	
	x2,y2,x1,y1 = getRectDim()
	external = set()
	matrix = [[0 for x in range(x2+2)] for y in range(y2+2)]
	
	for x in range(max(x1-1,0), x2+1):
		upperDist = getNearestPoint((x,y2+1))
		lowerDist = getNearestPoint((x,y1-1))
		
		if upperDist != -1:
			external.add(upperDist)
		if lowerDist != -1:
			external.add(lowerDist)
		
	for y in range(max(y1-1,0), y2+1):
		upperDist = getNearestPoint((x2+1,y))
		lowerDist = getNearestPoint((x1-1,y))
		
		if upperDist != -1:
			external.add(upperDist)
		if lowerDist != -1:
			external.add(lowerDist)
	
	currMaxArea = 0
	currMaxIndex = 0
	
	for point in range(len(posVector)):
		counter = 0
		
		if point not in external:
			for x in range(max(x1-1,0), x2+1):
				for y in range(max(y1-1,0), y2+1):
					if getNearestPoint((x,y)) == point:
						counter += 1
			if counter > currMaxArea:
				currMaxArea = counter
				currMaxIndex = point
	
	print currMaxArea, currMaxIndex
	
	print external
	
	
	
	
	
	
if __name__ == "__main__":
	main()
