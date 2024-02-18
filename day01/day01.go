package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Given a string of digits and characters, returns the first and the last digits in the string
// Parameters:
//   - line: string of digits and characters
//
// Returns:
//   - int: first and last digits in the string
//
// Examples:
//   - "1abc2" => 12
//   - "a1b2c3" => 13
func Solve(line string) int {
	var digit string
	var first_position int
	for i, char := range line {
		if char >= '0' && char <= '9' {
			digit = string(char)
			first_position = i
			break
		}
	}

	runes := []rune(line)
	for i := len(runes) - 1; i >= 0; i-- {
		char := runes[i]
		if i < first_position {
			break
		}
		if char >= '0' && char <= '9' {
			digit = digit + string(char)
			break
		}
	}
	converted_digit, _ := strconv.Atoi(digit)
	return converted_digit
}

// Given a string of digits and characters, returns the first and the last digits in the string
// both numbers and words are considered when looking for digits
// Parameters:
//   - line: string of digits and characters
//
// Returns:
//   - int: first and last digits in the string
//
// Examples:
//   - "1abc2" => 12
//   - "a1b2c3" => 13
//   - "one2asd8" => 18
func SolvePart2(line string) int {

	WORD_TO_DIGIT := map[string]string{
		"1":     "1",
		"2":     "2",
		"3":     "3",
		"4":     "4",
		"5":     "5",
		"6":     "6",
		"7":     "7",
		"8":     "8",
		"9":     "9",
		"0":     "0",
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}
	var first_digit string
	digit_index := len(line) + 1
	for word, digit := range WORD_TO_DIGIT {
		if occurrence_index := strings.Index(line, word); occurrence_index > -1 && occurrence_index < digit_index {
			digit_index = occurrence_index
			first_digit = digit
		}
	}
	var second_digit string
	digit_index = -1
	for word, digit := range WORD_TO_DIGIT {
		if occurrence_index := strings.LastIndex(line, word); occurrence_index > -1 && occurrence_index > digit_index {
			digit_index = occurrence_index
			second_digit = digit
		}
	}
	converted_digit, _ := strconv.Atoi(first_digit + second_digit)
	return converted_digit

}

func main() {
	solutionPart1 := 0
	solutionPart2 := 0
	// Read from input.txt
	file, err := os.OpenFile("input.txt", os.O_RDONLY, 0)
	if err != nil {
		fmt.Println("Failed to read input file")
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		line_sol := Solve(line)
		solutionPart1 = solutionPart1 + line_sol
		line_sol = SolvePart2(line)
		solutionPart2 = solutionPart2 + line_sol
	}
	fmt.Println("Solution Part 1: ", solutionPart1)
	fmt.Println("Solution Part 2: ", solutionPart2)
}
