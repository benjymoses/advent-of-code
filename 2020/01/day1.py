
def read_integers(filename):
	with open(filename) as f:
		return [int(x) for x in f]


def day1part1(inputList):
	total = 2020

	for current in inputList:
		seek = total - current

		if seek in inputList:
			return current*seek

def day1part2(inputList):
	total = 2020

	for i in inputList:
		for j in inputList:
			for k in inputList:
				if i + j + k == total:
					return i*j*k 

def main():
	print ("Advent of Code Day 1")

	intlist = read_integers('./input.txt')

	print("Answer to part 1 is: {}".format(day1part1(intlist)))
	print("Answer to part 2 is: {}".format(day1part2(intlist)))


if __name__ == "__main__":
    main()