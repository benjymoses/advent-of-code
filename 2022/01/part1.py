elf_dict = {}
current_elf = 0

with open("2022/01/input.txt") as file:
    for line in file:

        calories = line.rstrip("\n")

        if (calories == ""):
            current_elf += 1
        else:
            if current_elf in elf_dict:
                elf_dict[current_elf].append(int(calories))
            else:
                elf_dict[current_elf] = [int(calories)]

elf_totals = []

for key, value in elf_dict.items():
    elf_totals.append(sum(value))


print(f"PART 1: Highest calories held by an elf is {max(elf_totals)}")

elf_totals.sort(reverse=True)

print (f"PART 2: Total calories held by 3 highest calory carrying elvesis: {elf_totals[0] + elf_totals[1] + elf_totals[2]}")