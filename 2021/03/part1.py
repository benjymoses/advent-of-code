with open("2021/03/input.txt") as f:
    input = [line.rstrip() for line in f]

length_of_binaries = len(input[0])

sum_of_one = []
sum_of_zero = []

for i in range(length_of_binaries):
	
	sum_of_one.append(0)
	sum_of_zero.append(0)

	for bin in input:
		if bin[i] == "0":
			sum_of_zero[i] += 1
		else:
			sum_of_one[i] += 1

gamma = ""
epsilon = ""

for i in range(len(sum_of_zero)):
	if sum_of_zero[i] > sum_of_one[i]:
		gamma += "0"
		epsilon += "1"
	else:
		gamma += "1"
		epsilon += "0"

gamma = (int(gamma, 2))
epsilon = (int(epsilon, 2))

power_usage = gamma * epsilon

print(f"Power usage is {power_usage}")
