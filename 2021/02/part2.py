with open("2021/02/input.txt") as f:
    input = [line.rstrip() for line in f]

horizontal = 0
depth = 0
aim = 0

for line in input:
	value = [int(i) for i in line.split() if i.isdigit()]
	
	if "forward" in line:
		horizontal += value[0]
		depth += (aim * value[0])
	
	if "down" in line:
		aim += value[0]
	
	if "up" in line:
		aim -= value[0]

print(f"Answer is: {horizontal * depth}")