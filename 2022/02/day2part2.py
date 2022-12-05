inputFile = open("2022/02/input.txt", "r")
input = inputFile.read().split("\n")

''''
A = Rock: 1
B = Paper: 2
C = Scissors: 3

X = Lose: 0
Y = Draw: 1
Z = Win: 6
'''

results = {
    "A X": 3 + 0, "A Y": 1 + 3, "A Z": 2 + 6,
    "B X": 1 + 0, "B Y": 2 + 3, "B Z": 3 + 6,
    "C X": 2 + 0, "C Y": 3 + 3, "C Z": 1 + 6
}

total_score = sum(results[play] for play in input)

print(f"PART 2: Total score with new definition is {total_score}")