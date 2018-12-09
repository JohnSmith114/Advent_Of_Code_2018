
def main():
	vect = [line.rstrip('\n') for line in open("input.txt")]
	counter = 0
	for elem in vect:
		counter += int(elem)
	print(counter)

if __name__ == "__main__":
	main()
	
