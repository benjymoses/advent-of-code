choice_definitions = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

score_total = 0

with open("2022/02/input.txt") as file:
    for line in file:

        line = line.rstrip("\n")
        their_choice = {
            "letter": line[0],
            "choice": choice_definitions[line[0]]
        }

        my_choice = {
            "letter": line[2],
            "choice": choice_definitions[line[2]]
        }

        if my_choice["choice"] == "Rock":
            if their_choice["choice"] == "Scissors":
                # I win
                my_score = 1 + 6
            elif their_choice["choice"] == "Paper":
                # I lose
                my_score = 1 + 0
            elif their_choice["choice"] == "Rock":
                # Draw
                my_score = 1 + 3
        elif my_choice["choice"] == "Paper":
            if their_choice["choice"] == "Rock":
                # I win
                my_score = 2 + 6
            elif their_choice["choice"] == "Scissors":
                # I lose
                my_score = 2 + 0
            elif their_choice["choice"] == "Paper":
                # Draw
                my_score = 2 + 3
        elif my_choice["choice"] == "Scissors":
            if their_choice["choice"] == "Paper":
                # I win
                my_score = 3 + 6
            elif their_choice["choice"] == "Rock":
                # I lose
                my_score = 3 + 0
            elif their_choice["choice"] == "Scissors":
                # Draw
                my_score = 3 + 3

        score_total += my_score

print(f"PART 1: Following strategy gives a score of {score_total}")