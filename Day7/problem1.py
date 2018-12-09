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
	
	for x in lettersPresent:
		if sum(column(mtx, x))==0:
			stepsDone.append(x)
			break
	
	while True:
		print "Steps Done: ", stepsDone
		print "Steps Left: ", stepsLeft
		for x in lettersPresent:
			print "Testing letter ", getC(x)
			valid = 1
			if x in stepsDone:
				continue
			for elem in lettersPresent:
				print "Required: ", getC(elem)
				if column(mtx,x)[elem] == 1 and elem not in stepsDone:
					print "Test failed"
					valid = 0
					break
			if valid == 1 and x not in stepsLeft:
				stepsLeft.append(x)
				print "Appended ", getC(x)
		if len(stepsLeft) == 0:
			break
		else:
			stepsLeft.sort()
			stepsDone.append(stepsLeft[0])
			del stepsLeft[0]
	print map(lambda x: chr(x+65),stepsDone)
		

'''
010100
000010
100001
000010
000000
000010

[[C][[A][[B][D]][F]]]

CABDFE



'''
				
				
						
	
	
	
	
	
	
if __name__ == "__main__":
	main()
