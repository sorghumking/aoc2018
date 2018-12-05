from inputs import parse_day5

def part1(polymer):
    # lame approach - keep making passes until we're done
    cur = polymer
    passnumber = 1
    done = False
    while not done:
        reduced = []        
        i = 0
        while i < len(cur) - 1:
            c1 = cur[i]
            c2 = cur[i+1]
            if c1 != c2 and (c1.upper() == c2 or c1.lower() == c2):
                # print("Reducing {} and {}".format(c1, c2))
                i += 2 # skip ahead
            else:
                reduced.append(c1)
                i += 1
            if i == len(cur) - 1:
                reduced.append(c2)
        
        if len(cur) == len(reduced):
            done = True
            print("Reduced to {} elements".format(len(cur)))
        else:
            # print("Pass {}, reduced to {} elements".format(passnumber, len(reduced)))
            passnumber += 1
            cur = reduced
    return len(cur)

def part2(polymer):
    counts = {}
    for elim_char in [chr(i) for i in range(65, 91)]: # A-Z
        print("Removed {}".format(elim_char))
        elim_polymer = [c for c in polymer if c.upper() != elim_char]
        counts[elim_char] = part1(elim_polymer)
    mrp = min(counts.items(), key=lambda x:x[1])
    print("Most reduced polymer: {}".format(mrp))

if __name__ == "__main__":
    polymer = parse_day5("day5input.txt")
    part2([c for c in polymer])