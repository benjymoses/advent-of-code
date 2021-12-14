input = []

with open("2021/09/input.txt") as f:
	lines = f.read().splitlines()
	for line in lines:
		input.append([int(i) for i in line])

low_points = []

for ri, row in enumerate(input):
	for ci, cell_value in enumerate(row):
		neighbours = ["UP", "DOWN", "LEFT", "RIGHT"]
		
		if ri == 0: # Top row
			neighbours.remove("UP")

		if ri == len(input)-1: #Bottom row
			neighbours.remove("DOWN")

		if ci == 0: # Left column
			neighbours.remove("LEFT")

		if ci == len(row)-1: # Right column
			neighbours.remove("RIGHT")

		neighbour_values = []

		for neighbour in neighbours:
			
			if neighbour == "UP":
				neighbour_values.append(input[ri-1][ci])
			elif neighbour == "DOWN":
				neighbour_values.append(input[ri+1][ci])
			elif neighbour == "LEFT":
				neighbour_values.append(input[ri][ci-1])
			elif neighbour == "RIGHT":
				neighbour_values.append(input[ri][ci+1])
			
		if cell_value < min(neighbour_values):
			low_points.append(cell_value)

risk_level = sum(low_points) + len(low_points)

print(f"Sum of risk in heightmap: {risk_level}")
