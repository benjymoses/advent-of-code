input = [int(line) for line in open("2021/01/input.txt", "r+").readlines()]

counter = 0

previous_sum = 0

loop_limit = int(len(input) - len(input)%3)

for i in range(loop_limit):
	sum = input[i] + input[i + 1] + input[i + 2]

	if sum > previous_sum:
		counter += 1
	
	previous_sum = sum

print(f"Count is {counter - 1}")