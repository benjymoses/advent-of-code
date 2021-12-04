input = [int(line) for line in open("2021/01/input.txt", "r+").readlines()]

counter = 0
previousValue = 0

for item in input:
	if item > previousValue:
		counter += 1
	
	previousValue = item

print(f"The answer is {counter - 1}")