inputFile = open("2022/03/input.txt", "r")
input = inputFile.read().split("\n")

def char_value(letter):
    # Magic numbers derived from trial and error with sample input from puzzle
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

# Part 1
def part1():
    sum_of_item_values = 0
    
    for backpack in input:

        compartment_1, compartment_2 = backpack[:len(backpack)//2], backpack[len(backpack)//2:]
        common_character = "".join(set(compartment_1).intersection(compartment_2))

        sum_of_item_values += char_value(common_character)

    return sum_of_item_values


# Part 2
def part2():
    sum_of_item_values = 0

    for index in range(0, len(input), 3):
        
        backpack_1 = input[index]
        backpack_2 = input[index + 1]
        backpack_3 = input[index + 2]

        badge_letter = "".join(set(backpack_1) & set(backpack_2) & set(backpack_3))

        sum_of_item_values += char_value(badge_letter)

    return sum_of_item_values

print(f"PART 1: Sum of item values is {part1()}")
print(f"PART 2: Sum of item values is {part2()}")