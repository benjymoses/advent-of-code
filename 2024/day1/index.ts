import * as fs from "fs";

const getInput = (fileName: string) => {
  const input = fs.readFileSync(fileName, "utf-8").split("\n");

  let leftList: number[] = [];
  let rightList: number[] = [];

  input.forEach((line) => {
    const numbers = line.split("   ");
    leftList.push(parseInt(numbers[0]));
    rightList.push(parseInt(numbers[1]));
  });

  leftList = leftList.sort();
  rightList = rightList.sort();

  return { leftList, rightList };
};

const part1 = (fileName: string) => {
  const { leftList, rightList } = getInput(fileName);

  let result = 0;

  for (let i = 0; i < leftList.length; i++) {
    result += Math.abs(leftList[i] - rightList[i]);
  }

  console.log(`Part 1 answer: ${result}`);
};

const part2 = (fileName: string) => {
  const { leftList, rightList } = getInput(fileName);

  let result = 0;

  leftList.forEach((element) => {
    const elementCounter = rightList.filter(
      (rightElement) => rightElement == element
    ).length;
    result += element * elementCounter;
  });

  console.log(`Part 2 answer: ${result}`);
};

part1("day1/input.txt");
part2("day1/input.txt");
