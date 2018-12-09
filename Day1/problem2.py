

def main():
	vect = [int(line.rstrip('\n')) for line in open("input.txt")]
	output = open("output.txt","w")
	occurr = [0]
	counter = 0
	i = 0
	
	while True:
		counter += vect[i%len(vect)]
		output.write(str(counter)+'\n')
		for elem in occurr:
			if counter == elem:
				print(counter)
				return
		occurr.append(counter)
		print(i)
		i = i+1

if __name__ == "__main__":
	main()
	
