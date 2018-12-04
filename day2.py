def parse_input(inputfile):
    boxids = []
    with open(inputfile) as f:
        boxids = [line.strip() for line in f.readlines()]
    return boxids

def part1(boxids):
    twos = 0
    threes = 0
    for bid in boxids:
        two, three = exactly_two_or_three(bid)
        twos += two
        threes += three
    return twos * threes

# return tuple 1 if true, 0 if false
def exactly_two_or_three(bid):
    count_dict = {}
    for c in bid:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    two = 1 if 2 in count_dict.values() else 0
    three = 1 if 3 in count_dict.values() else 0
    print("{} contains {} 2s {} 3s".format(bid, two, three))
    return two, three

def part2(boxids):
    for b in boxids:
        if differ_by_exactly_one(b, boxids):
            break

def differ_by_exactly_one(bid, boxids):
    for b in boxids:
        diff_total = 0
        assert(len(bid) == len(b)) # assume all IDs have same length
        for idx in range(len(bid)):
            if bid[idx] != b[idx]:
                diff_total += 1
        if diff_total == 1:
            print("{} and {} differ by exactly 1 letter".format(b, bid))
            return True
    return False

if __name__ == "__main__":
    fs = parse_input("day2input.txt")
    # fs = ["vrtkqyluibsocwvaezjmhgfnll"]
    #print "box ids = {}".format(fs)
    part2(fs)
    #print(f)