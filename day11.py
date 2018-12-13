import sys

def part1(serial_num):
    levels = {}
    for y in range(1, 301):
        for x in range(1, 301):
            levels[(x,y)] = power_level(serial_num, x, y)

    max_power = -99999
    max_coord = None
    max_width = None
    ### PART TWO ###
    for width in range(1, 301):
        if width % 10 == 0:
            print("Width {}".format(width))
        mp, mc = find_max_square(levels, width)
        if mp > max_power:
            max_power = mp
            max_coord = mc
            max_width = width
    ### PART ONE ###
    # max_width = 3
    # max_power, max_coord = find_max_square(levels, 3)
    ################

    print("Maximum power {} with width {}, upper-left coord {}".format(max_power, max_width, max_coord))

def find_max_square(levels, width):
    max_power = -99999
    max_coord = None
    for y in range(1, 302 - width):
        for x in range(1, 302 - width):
            power = square_power(levels, (x,y), width)
            if power > max_power:
                max_power = power
                max_coord = (x,y)
    return max_power, max_coord

prev_totals = {} # retain previous totals in square_power()

# Client is responsible for keeping params inbounds!
# levels - dict of power levels keyed on (x,y) coord
# coord - upper-left coordinate of square for which to compute total power
# width - width of a side in the square
def square_power(levels, coord, width):
    global prev_totals
    power = 0
    # We've retained total power of previous width square,
    # now we only need to accumulate power along new edges and
    # add to the retained total. Assumes widths increase by 1
    # per call. Still takes about 7 minutes to do part 2, but
    # waaaaay faster than brute forcing which took over 6 hours!
    if coord in prev_totals:
        edge_power = 0
        for y in range(coord[1], coord[1] + width):
            fixed_x = coord[0] + width - 1
            edge_power += levels[(fixed_x, y)]
        for x in range(coord[0], coord[0] + width - 1): # don't double-count lower-right corner
            fixed_y = coord[1] + width - 1
            edge_power += levels[(x, fixed_y)]
        power = edge_power + prev_totals[coord]
    else:
        for y in range(coord[1], coord[1] + width):
            for x in range(coord[0], coord[0] + width):
                power += levels[(x,y)]

    prev_totals[coord] = power
    return power

def power_level(serial_num, x, y):
    rack = x + 10
    pl = rack * y
    pl += serial_num
    pl *= rack
    spl = str(pl)
    if len(spl) >= 3:
        pl = int(spl[len(spl) - 3]) - 5 # grab hundreds' digit
    else:
        pl = -5
    return pl

if __name__ == "__main__":
    part1(9424)
    # part2: uncomment PART TWO code and comment PART ONE