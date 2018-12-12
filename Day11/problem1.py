serial = 4455

def calc(x,y):
	rackID = x+10
	powerL = (rackID*y + serial)*rackID
	if powerL > 99:
		return int(str(powerL)[-3])-5
	else:
		return -5

def main():
	matrix = [[0 for x in range(300)] for y in range(300)]
	for x in range(300):
		for y in range(300):
			matrix[x][y] = calc(x,y)
	print matrix
	mtx = []
	maxN = 0
	maxX = 0
	maxY = 0
	sizeM = 0
	for size in range(1, 300): #Remove this and set size=3 for first part
		for y in range(298):
			for x in range(298):
				if x+size>299 or y+size>299:
					continue
				sumTotal = 0
				for b in range(size):
					for a in range(size):
						sumTotal += matrix[x+a][y+b]
				if maxN < sumTotal:
					maxN = sumTotal
					maxX = x
					maxY = y
					sizeM = size
					print maxN, maxX, maxY, size
		print maxN, maxX, maxY, size
	
	#After size 11-ish the points never go up, so you can stop the program early instead of calculating all the possibilities
	
if __name__ == "__main__":
	main()
