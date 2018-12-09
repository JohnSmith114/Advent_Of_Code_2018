inputLines = [lines.strip('\n') for lines in open("input.txt", "r")]

mtx = [[0 for x in range(26)] for y in range(26)]

def getNumber(char):
	return ord(char)-65
	
def getC(num):
	return chr(num+65)
	
def column(matrix, i):
    return [row[i] for row in matrix]

def main():
	stepsDone = []
	stepsLeft = []
	instructions = [0,0]
	lettersPresent = set()
	for elem in inputLines:
		instructions[0]=elem[5:6]
		instructions[1]=elem[-12:-11]
		lettersPresent.add(getNumber(instructions[0]))
		lettersPresent.add(getNumber(instructions[1]))
		mtx[getNumber(instructions[0])][getNumber(instructions[1])] = 1
				
	for lines in mtx:
		print lines
	workers = [[-1,1] for x in range(2)]
	elab = set()
	timer = -1
	stepTime = 60
	while True:
		timer += 1
		if len(stepsDone) == len(lettersPresent):
			break
		
		for work in workers:
			work[1] -= 1

		for work in workers:
			if work[1] == 0 and work[0]!=-1:
				stepsDone.append(work[0])
	
		for x in lettersPresent:
			print "Testing letter ", getC(x)
			valid = 1
			if x in stepsDone:
				continue
			for elem in lettersPresent:
				if column(mtx,x)[elem] == 1 and elem not in stepsDone:
					valid = 0
					break
			if valid == 1 and x not in stepsLeft and x not in elab:
				stepsLeft.append(x)
				print "Appended ", getC(x)
		print "Steps Done: ", stepsDone
		print "Steps Left: ", stepsLeft
		
		for work in workers:
			stepsLeft.sort()
			if work[1]==0:
				if len(stepsLeft)>0:
					work[0] = stepsLeft.pop(0)
					work[1] = work[0]+1+stepTime
					elab.add(work[0])
				else:
					work[0] = -1
					work[1] = 1
		print workers
		print timer
	
if __name__ == "__main__":
	main()
