from itertools import cycle

nPlayers = 425
lastP = 7084800

def main():
	pPoints = [0 for x in range(nPlayers)]
	marbles = [0]
	currMarble = 0
	currPos = 0
	for player in cycle(range(nPlayers)):
		#print "Current player: ", player
		currMarble += 1
		#print "Current marble: ", currMarble
		#print "Current position: ", currPos
		#print marbles
		if currMarble%23 == 0:
			pPoints[player] += currMarble
			#print pPoints[player]
			currPos = (currPos-7)%len(marbles)
			pPoints[player] += marbles.pop(currPos)
			#print pPoints[player]
			
		else:
			currPos = (currPos + 2)%(len(marbles)) if (currPos + 2)%(len(marbles))!= 0 else len(marbles)
			marbles.insert(currPos, currMarble)
		#print marbles
		if currMarble == lastP:
			break
			
	#print pPoints
	print max(pPoints)
	

if __name__ == "__main__":
	main()
