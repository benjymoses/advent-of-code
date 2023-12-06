const sampleInput = "2023/day1/sampleinput.txt"
const puzzleInput = "2023/day1/puzzleinput.txt"


const buildPuzzleInput = async(input) => {
    const fs = require('fs');

    const inputText = fs.readFileSync(input);
    return inputText.toString().split("\n");
}

const puzzleLogic = async(puzzleLines) => {
    let runningTotal = 0;
    for (line of puzzleLines) {
        const firstDigit = parseInt(line.match(/\d/));
        const lastDigit = parseInt(line.match(/(\d+)(?!.*\d)/));
        const finalNumber = parseInt(`${firstDigit}${lastDigit}`)
        runningTotal += finalNumber
    }
    return runningTotal

}

const main = async() => {
    const sampleLines = await buildPuzzleInput(sampleInput);
    const sampleAnswer = await puzzleLogic(sampleLines);
    console.log(`The sum of all of the sample inputs was: ${sampleAnswer}`)

    const puzzleLines = await buildPuzzleInput(puzzleInput);
    const puzzleAnswer = await puzzleLogic(puzzleLines);
    console.log(`The sum of all of the puzzle inputs was: ${puzzleAnswer}`)

}
;

main();