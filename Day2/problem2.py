
from itertools import combinations

vect = [line.strip('\n') for line in open("input.txt")]

def couple():
	for x in combinations(vect,2):
		diff = 0
		string1 = list(x[0])
		string2 = list(x[1])
		for y in range(len(string1)):
			if string1[y] != string2[y]:
				if diff == 0:
					diff = 1
				else:
					diff = 2
					break
		if diff == 1:
			return (x[0], x[1])

def main():
	str1, str2 = couple()
	common = []
	for x in range(len(str1)):
		if str1[x] == str2[x]:
			common.append(str1[x])
	print(str(common))


		
		
	
	
	
if __name__ == "__main__":
	main()
