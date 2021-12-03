def part1(data):
	goodCounter = 0

	for current in data:
		splitlist = current.split(':')
	
		policy = splitlist[0]
		policysplit = policy.split(' ')
		policybounds = policysplit[0]
		policyletter = policysplit[1]
		policyboundssplit = policybounds.split('-')
		policylower = int(policyboundssplit[0])
		policyupper = int(policyboundssplit[1])

		password = splitlist[1]

		policylettercounter = password.count(policyletter)

		if policylettercounter >= policylower:
			if policylettercounter <= policyupper:
				goodCounter += 1

	print("Part 1: {}".format(goodCounter))
	

def part2(data):
	goodCounter = 0

	for current in data:
		splitlist = current.split(':')
	
		policy = splitlist[0]
		policysplit = policy.split(' ')
		policybounds = policysplit[0]
		policyletter = policysplit[1]
		policyboundssplit = policybounds.split('-')
		policylower = int(policyboundssplit[0])
		policyupper = int(policyboundssplit[1])

		password = splitlist[1].strip()

		occurances = 0

		if password[policylower-1] == policyletter:
			occurances += 1
		
		if password[policyupper-1] == policyletter:	
			occurances += 1

		if occurances == 1:
			goodCounter += 1

		

	print("Part 2: {}".format(goodCounter))


with open("input.txt") as f:
	data = f.readlines()


part1(data)
part2(data)


