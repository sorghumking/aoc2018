from inputs import parse_day12

def part1(notes):
    # added . on ends of initial state since I was unsure how cases there
    # should be handled...
    state = ".....##.##.##..#..#.#.#.#...#...#####.###...#####.##..#####.#..#.##..#..#.#...#...##.##...#.##......####.................................................................................................................................."
    # state = ".....#..#.#..##......###...###............" # example

    new_state = []
    center_index = 5 # index of pot 0 in modified initial state
    print("Initial state: {}".format(state))
    for gen in range(1, 121):
        for pos in range(len(state)):
            g = get_group(state, pos)
            pos_state = '.' if g not in notes else notes[g]
            new_state.append(pos_state)
        state = "".join(new_state)
        new_state = []
        print("After {} generation: ".format(gen) + state)
        if gen >= 100:
            print("Total planted pots = {}".format(get_total(state, center_index)))

def get_total(state, center_index):
    total = 0
    for p in range(len(state)):
        if state[p] == "#":
            total += (p - center_index)
    return total

def get_group(state, pos):
    if pos == 0:
        return ".." + state[:3]
    elif pos == 1:
        return "." + state[:4]
    elif pos == len(state) - 1:
        start = pos - 2
        return state[start:] + ".."
    elif pos == len(state) - 2:
        start = pos - 3
        return state[start:] + "."
    else:
        return state[pos - 2 : pos + 3]


if __name__ == "__main__":
    notes = parse_day12("day12input.txt")
    # notes = parse_day12("day12example.txt")
    part1(notes)
    # part 2 requires no code, just the observation that the pattern
    # stabilizes at generation 100 (total 5691) with 62 plants that
    # shift forward one per subsequent generation.
    print("Part 2 Total: {}".format(5691 + 62 * (50000000000 - 100)))
