import sys

lines = [x.strip('\n') for x in open("input.txt", "r")]
positions=[]
velocities=[]
for x in lines:
    positions.append(map(int, x[x.find("<")+1:x.find(">")].split(", ")))
    velocities.append(map(int, x[x.find("<", x.find("<")+1)+1:x.find(">", x.find("<", x.find("<")+1))].split(", ")))

print positions
print velocities

def main():
    counter = 0
    while True:
		maxX = max([positions[x][0] for x in range(len(positions))])+2
		maxY = max([positions[x][1] for x in range(len(positions))])+2
		minX = min([positions[x][0] for x in range(len(positions))])-2
		minY = min([positions[x][1] for x in range(len(positions))])-2
		counter+=1
		if maxX-minX<300 and maxY-minY<300:
			print(minY, maxY, minX, maxX)
			for y in range(minY, maxY):
				for x in range(minX, maxX):
					 if [x,y] in positions:
						sys.stdout.write('#')
						sys.stdout.flush()
					 else:
						sys.stdout.write('.')
						sys.stdout.flush()
				print("|")
			print("-----------------------------------")
			print("COUNTER ", counter)
		for x in range(len(positions)):
			positions[x][0]+=velocities[x][0]
			positions[x][1]+=velocities[x][1]
		

if __name__ == "__main__":
    main()
