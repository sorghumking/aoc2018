import sys
from inputs import parse_day6

def part1(coordDict):
    coords = coordDict #.values()

    # find boundaries
    xmin, xmax, ymin, ymax = get_boundaries(coords)

    infinite = find_infinite(coords, xmin, xmax, ymin, ymax)
    print("# of infinites: {}".format(len(infinite)))

    totals = get_totals(coords, xmin+1, xmax, ymin+1, ymax)

    # noninfinite = [c for c in coords if c not in infinite]
    ni_totals = { t[0]:t[1] for t in totals.items() if t[0] not in infinite }
    print("totals = {}, ni_totals = {}".format(len(totals), len(ni_totals)))
    largest = max(ni_totals.items(), key=lambda t:t[1])
    print("Largest area is for point {} with {} closests".format(largest[0], largest[1]))

    # plot = get_plot(coordDict, xmin - 1, xmax + 2, ymin - 1, ymax + 2)
    # print_plot(plot, xmax - xmin + 3)

def part2(coords, threshold):
    # find boundaries
    listo = []
    xmin, xmax, ymin, ymax = get_boundaries(coords)
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            total = get_dist_sum((x,y), coords)
            if total < threshold:
                listo.append(total) # doesn't matter what we append, len of listo will be the answer
    print("There are {} coords with < {} total".format(len(listo), threshold))

# return sum of distance from pt to each c in coords
def get_dist_sum(pt, coords):
    sum = 0
    for c in coords:
        sum += dist(pt, c)
    return sum

def get_boundaries(coords):
    xmin = min(coords, key=lambda p:p[0])[0]
    xmax = max(coords, key=lambda p:p[0])[0]
    ymin = min(coords, key=lambda p:p[1])[1]
    ymax = max(coords, key=lambda p:p[1])[1]
    print("xmin = {}, max = {}, ymin = {}, ymax = {}".format(xmin, xmax, ymin, ymax))
    return xmin, xmax, ymin, ymax

def get_totals(coords, xmin, xmax, ymin, ymax):
    totals = {} # accumulate closest points for each coord in noninfinite
    for y in range(ymin, ymax):    
        for x in range(xmin, xmax):
            closest = find_closest((x,y), coords)
            if closest:
                if closest in totals:
                    totals[closest] += 1
                else:
                    totals[closest] = 1
    return totals

def get_plot(coordDict, x0, x1, y0, y1):
    plot = []
    for y in range(y0, y1):
        for x in range(x0, x1):
            closest = find_closest((x,y), coordDict.values())
            if closest:
                for k,v in coordDict.items():
                    if v == closest:
                        if v == (x,y):
                            plot.append(k)
                        else:
                            plot.append(k.lower())
                        break
            else:
                plot.append('.')
    return plot

def print_plot(plot, width):
    for idx, pt in enumerate(plot):
        if idx != 0 and idx % width == 0:
            sys.stdout.write('\n')
        sys.stdout.write(pt)
    sys.stdout.write('\n')


# return list of points that have infinite area
def find_infinite(coords, xmin, xmax, ymin, ymax):
    # create list of all coordinates on boundaries
    boundaries = [(x, ymin) for x in range(xmin, xmax + 1)]
    boundaries += [(xmax, y) for y in range(ymin, ymax + 1)]
    boundaries += [(x, ymax) for x in range(xmin, xmax + 1)]
    boundaries += [(xmin, y) for y in range(ymin, ymax + 1)]

    infinite = []
    for bp in boundaries:
        closest = find_closest(bp, coords)
        if closest:
            infinite.append(closest)

    return list(set(infinite))
            

# return closest coord in coords to pt, or None
# if multiple coords are closest
def find_closest(pt, coords):
    dists = {}
    for c in coords:
        dists[c] = dist(pt, c)
        if dists[c] == 0:
            return c
    mindist = min(dists.items(), key=lambda x:x[1]) # find min dist
    if len([d for d in dists.values() if d == mindist[1]]) > 1:
        return None # more than one closest
    else:
        return mindist[0]

def dist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])


if __name__ == "__main__":
    # coordDict = {'A':(1,1), 'B':(1,6), 'C':(8,3), 'D':(3,4), 'E':(5,5), 'F':(8,9)}    
    coords = parse_day6("day6input.txt")
    # part1(coords)
    part2(coords, 10000)
    # part1(coordDict.values())