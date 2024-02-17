package main

import "testing"

func TestShouldReturnFirstAndLastDigit(t *testing.T) {
    text := "1abc2"
    expected := 12
    actual := Solve(text)
    if actual != expected {
        t.Errorf("Expected %d, got %d", expected, actual)
    }
}


func Test_should_return_the_digits_in_the_middle(t *testing.T){
    line := "pqr3stu8vwx"
    actual := Solve(line)
    expected := 38
    if actual != expected {
        t.Errorf("Expected %d, got %d", expected, actual)
    }
}

func Test_should_take_only_the_first_digits_found(t *testing.T){
    line := "1b2c3d4e5f"
    actual := Solve(line)
    expected := 15
    if actual != expected {
        t.Errorf("Expected %d, got %d", expected, actual)
    }
}

func Test_should_take_the_only_digit_as_first_and_last(t *testing.T){
    line := "treb7uchet"
    actual := Solve(line)
    expected :=77
    if actual != expected {
        t.Errorf("Expected %d, got %d", expected, actual)
    }


}
