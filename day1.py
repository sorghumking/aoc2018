def parse_day1_input(inputfile):
    frequencies = []
    with open(inputfile) as f:
        frequencies = [int(line) for line in f.readlines()]
    return frequencies

def day1_part1(frequencies):
    total = 0
    for f in frequencies:
        total += f
    return total

def day1_part2(frequencies):
    seen = []
    total = 0
    found_duplicate = False
    while not found_duplicate:
        for f in frequencies:
            total += f
            print ("total = {}".format(total))
            if total in seen:
                print("{} == {}".format(total, seen))
                found_duplicate = True
                break
            else:
                seen.append(total)
                # print("seen size = {}".format(len(seen)))
    return total

if __name__ == "__main__":
    fs = parse_day1_input("day1input.txt")
    f = day1_part2(fs)
    print(f)