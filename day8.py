import sys
from inputs import parse_day8

index = 0 # mmmm, global.

def part1(nodes):
    total = node_total(nodes)
    print("total = {}".format(total))

def node_total(nodes):
    global index

    kids, metadata = nodes[index], nodes[index + 1]
    # print("{}: kids = {}, metadata = {}".format(index, kids, metadata))
    index += 2
    if kids == 0:
        total = sum(nodes[index : index + metadata])
        index += metadata
        # print("no kids, returning total {}".format(total))
        return total
    else:
        total = 0

        ### Part 1 ###
        # for _ in range(kids):
        #     # print("Kid {}".format(kid + 1))
        #     total += node_total(nodes)
        # total += sum(nodes[index : index + metadata])
        ##############

        ### Part 2 ###
        kid_totals = []
        for kid in range(kids):
            # print("Kid {}".format(kid + 1))
            kid_totals.append(node_total(nodes))
        # total += sum(nodes[index : index + metadata])
        for md in nodes[index : index + metadata]: # md is one-based
            if (md - 1) < len(kid_totals):
                total += kid_totals[md - 1]
        ###############

        index += metadata
        return total


if __name__ == "__main__":
    # nodes = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    nodes = parse_day8("day8input.txt")
    part1(nodes)