with open('data\spreadsheet.txt', 'r') as f:
    input = f.read()


def part1():
    sum = 0
    for line in input.split('\n')[:-1]:
        row = [int(digit) for digit in line.split('\t')]
        sum += max(rows) - min(rows)

    print(sum)


def part2():
    sum = 0
    for line in input.split('\n')[:-1]:
        row = [int(digit) for digit in line.split('\t')]
        for first_digit in row:
            for second_digit in row:
                if first_digit == second_digit:
                    continue
                if first_digit % second_digit == 0:
                    sum += first_digit / second_digit
    print(sum)


part2()
