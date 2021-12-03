import math
inputArray = open('input.txt', 'r').readlines()
# inputArray = [100756] # test case


def calculateFuel(mass):
    fuelRequired = int(math.floor(int(mass) // 3 - 2))

    if fuelRequired < 0:
        fuelRequired = 0

    # Useful to debug test cases
    # print("calculateFuel: " + str(fuelRequired))
    return fuelRequired


def part_one(masses):
    totalFuel = 0

    for mass in masses:
        totalFuel += calculateFuel(mass)

    return totalFuel


def part_two(masses):
    totalFuel = 0

    for mass in masses:
        fuelNeeded = mass
        while fuelNeeded > 0:
            fuelNeeded = calculateFuel(fuelNeeded)
            totalFuel += fuelNeeded

    return totalFuel


print("")
print("Part One: " + str(part_one(inputArray)))
print("Part Two: " + str(part_two(inputArray)))
