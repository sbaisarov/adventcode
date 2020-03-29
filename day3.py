def part1():
    ctr = 0
    steps = 0
    value = 0
    while value < 361527:
        ctr += 1
        if ctr % 2 != 0:
            value = pow(ctr, 2)
            steps += 1

    diff = 361527 - pow(ctr - 2, 2)
    steps += diff - steps
    print(steps)


def part2():
    squares = [[[1], [1], [1], [1]]]
    area = 8
    total = 0
    while total < 361527:
        prev_square = squares[-1]
        side_size = area // 4
        square = []
        number = 0
        for side_index, prev_side in enumerate(prev_square):
            side = []
            if number:
                side.append(number)  # add the last value from the previous side
            for i in range(side_size):
                point = 0
                point += number
                if area == 8:
                    point += 1
                else:
                    for k in range(-1, 2):
                        if i + k == -1:
                            continue
                        try:
                            point += prev_side[i+k]
                        except IndexError:
                            pass

                if i == 0 and number:
                    point += square[-1][-2]

                if i + 2 >= side_size and side_index == 3:
                    point += square[0][0]

                print(point)
                side.append(point)
                number = point
            square.append(side)

        square[0].insert(0, number)  # add the last number of the square to the first side
        total += number
        squares.append(square)
        area += 8


part2()
