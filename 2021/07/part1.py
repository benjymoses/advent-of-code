import statistics 

with open("2021/07/input.txt") as f:
	lines = f.read().splitlines()
	input = [int(i) for i in lines[0].split(",")]

target = int(statistics.median(input))

fuel_counter = 0

for crab in input:
	fuel_counter += abs(crab - target)

print(f"Fuel used: {fuel_counter}")