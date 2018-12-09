from collections import Counter
from functools import reduce

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

def main():
	
	x2,y2,x1,y1 = getRectDim()
	counter = 0
	
	for x in range(x1, x2+1):
		for y in range(y1, y2+1):
			distance = reduce(lambda a,b: a+b, map(lambda z: abs(x-z[0])+abs(y-z[1]), posVector))
			if distance < 10000:
				counter += 1
			print counter
	print counter	
	
if __name__ == "__main__":
	main()
