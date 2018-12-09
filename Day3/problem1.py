#Actually for this one I accidentally overwrote the solution to the first problem, so this is the solution to the second one

def main():
	w = 1000
	h = 1000
	mtx = [[0 for x in range(w)] for y in range(h)]
	vect = [line.strip('\n').split(' ') for line in open("1input.txt", "r")]
	validvector = [1 for x in range(len(vect))]
	
	for line in vect:
		valid = 1
		for y in range(int(line[4])):
			for x in range(int(line[3])):
				mtx[int(line[1])+x][int(line[2])+y] += 1
		
	print validvector
	
	for line in vect:
		for y in range(int(line[4])):
			for x in range(int(line[3])):
				if mtx[int(line[1])+x][int(line[2])+y] > 1 and validvector[int(line[0])-1]==1:
					print(mtx[int(line[1])+x][int(line[2])+y])
					validvector[int(line[0])-1] = 0
						
	
	print validvector
	for x in range(len(validvector)):
		if validvector[x]==1:
			print x
	
if __name__ == "__main__":
	main()
