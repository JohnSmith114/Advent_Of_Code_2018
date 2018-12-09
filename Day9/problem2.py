from itertools import cycle
from collections import deque

nPlayers = 425
lastP = 70848

def main():
	pPoints = [0 for x in range(nPlayers)]
	marbles = deque()
	nMarbles = 1
	marbles.append(0)
	currMarble = 0
	currPos = 0
	for player in cycle(range(nPlayers)):
		currMarble += 1
		if currMarble%23 == 0:
			pPoints[player] += currMarble
			marbles.rotate(7)
			pPoints[player] += marbles.pop()
			marbles.rotate(-1)
			nMarbles -= 1
		else:
			marbles.rotate(-1)
			marbles.append(currMarble)
			nMarbles += 1
		if currMarble == lastP:
			break
	print "Result: ",max(pPoints)
	

if __name__ == "__main__":
	main()
