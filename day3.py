import inputs

def part1(claims):
    area_dict = {}
    for c in claims:
        _, x0, y0, wid, hit = c # _ is dummy for id, unused in part 1
        for x in range(x0, x0 + wid):
            for y in range(y0, y0 + hit):
                if (x,y) in area_dict:
                    area_dict[(x,y)] = True
                else:
                    area_dict[(x,y)] = False
    total_disputed = len([di for di in area_dict.values() if di])
    print("There are {} disputed sqin.".format(total_disputed))
    return area_dict # used in part 2

def part2(claims, area_dict):
    free_claims = []
    for c in claims:
        claim_id, x0, y0, wid, hit = c
        overlaps = 0
        for x in range(x0, x0 + wid):
            for y in range(y0, y0 + hit):
                if (x,y) not in area_dict: # something is wrong
                    print("SOMETHING IS WRONG")
                    return
                elif area_dict[(x,y)]:
                    overlaps += 1
        if overlaps == 0:
            print("ID {} has no overlaps".format(claim_id))
            free_claims.append(claim_id)
    print("Free claims: {}".format(free_claims))


if __name__ == "__main__":
    claims = inputs.parse_day3("day3input.txt")
    area_dict = part1(claims)
    part2(claims, area_dict)
