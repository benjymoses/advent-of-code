with open("2021/07/input.txt") as f:
	lines = f.read().splitlines()
	input = [int(i) for i in lines[0].split(",")]

min_crab = min(input)
max_crab = max(input)

def triangular_number(n):
    return n * (n + 1) // 2

def calculate_fuel(target):
	fuel_counter = 0

	for crab in input:
		distance_to_move = abs(crab - target)
		fuel_counter += triangular_number(distance_to_move)

	return fuel_counter

lowest_cost = calculate_fuel(max_crab)
lowest_cost_target = max_crab

for position in range(min_crab, max_crab + 1):
	cost = calculate_fuel(position)
	if cost < lowest_cost:
		lowest_cost = cost
		lowest_cost_target = position

print(f"Lowest cost is: {lowest_cost} by moving to {lowest_cost_target}")