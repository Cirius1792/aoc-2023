package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
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

func main() {
	fmt.Println("Part 1:")
    solution := 0
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
        solution = solution + line_sol 
    }
    fmt.Println("Solution: ", solution)
}
