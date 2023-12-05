import unittest


NUMBERS = set([
    '0', 
    '1',     
    '2',    
    '3',
    '4',     
    '5', 
    '6',     
    '7',
    '8', 
    '9', 
    ])

def get_val_from_line(line:str) -> int:
    i = 0
    first_digit = ""
    second_digit = ""
    while i < len(line) and (not first_digit or not second_digit):
        if not first_digit and line[i] in NUMBERS:
            first_digit = line[i]
        j = -(i+1)
        if not second_digit and line[j] in NUMBERS:
            second_digit = line[j]
        i += 1
    return int(first_digit + second_digit)



class SolutionTest(unittest.TestCase):

    def test_should_return_the_first_and_last_digit(self):
        line = "1abc2"
        val = get_val_from_line(line)
        assert 12 == val

    def test_should_return_the_digits_in_the_middle(self):
        line = "pqr3stu8vwx"
        val = get_val_from_line(line)
        assert 38 == val
 
    def test_should_take_only_the_first_digits_found(self):
        line = "1b2c3d4e5f"
        val = get_val_from_line(line)
        assert 15 == val

    def test_should_take_the_only_digit_as_first_and_last(self):
        line = "treb7uchet"
        val = get_val_from_line(line)
        assert 77 == val
 
if __name__ == '__main__':
    with open('./01/input_part_one.txt', 'r') as reader:
        acc = 0
        for line in reader:
            acc += get_val_from_line(line)
        print(f"result: {acc}")

