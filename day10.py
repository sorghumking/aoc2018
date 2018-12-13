import sys
from inputs import parse_day10

def part1(pvlist):
    positions = zip(pvlist[0::4], pvlist[1::4])
    velocities = zip(pvlist[2::4], pvlist[3::4])
    # print("pos {}, velocity {}".format(positions[0], velocities[0]))
    # print("pos {}, velocity {}".format(positions[-1], velocities[-1]))

    min_average = 99999
    min_time = 0
    for second in range(50000):
        for idx, v in enumerate(velocities):
            posx, posy = positions[idx]
            positions[idx] = (posx + v[0], posy + v[1])

        # need a way to know when all particles are getting close...
        # try average of distance between p0 and p1, p1 and p2, etc.
        # in list
        total_dist = 0
        for idx, p in enumerate(positions):
            if idx == len(positions) - 1:
                break
            total_dist += dist(positions[idx], positions[idx + 1])
        average = total_dist / (len(positions) - 1)

        # appears second in which particles are collectively closest is 10458.
        # (Actually second 10459 since we start from second 0.)
        if second == 10458:
            xmin = min(positions, key=lambda p:p[0])[0]
            xmax = max(positions, key=lambda p:p[0])[0]
            ymin = min(positions, key=lambda p:p[1])[1]
            ymax = max(positions, key=lambda p:p[1])[1]

            print("Range is {} to {}, {} to {}".format(xmin, xmax, ymin, ymax))

            # print message
            for y in range(ymin, ymax+1):
                for x in range(xmin, xmax+1):
                    if (x,y) in positions:
                        sys.stdout.write('#')
                    else:
                        sys.stdout.write('.')
                sys.stdout.write('\n')

            break

        # if average < min_average:
        #     min_average = average
        #     min_second = second
        #     print("new min_average = {} @ second {}".format(min_average, second))
        # else:
        #     pass
        #     # print('average = {}'.format(average))
        #     # previous second was the closest?
        #     # best_second = second - 1
    
    # print("minimum average {} at second {}".format(min_average, second))

def dist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

if __name__ == "__main__":
    pvlist = parse_day10("day10input.txt")
    part1(pvlist)