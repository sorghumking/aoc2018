from inputs import parse_day13

class Cart:
    def __init__(self, coord, facing):
        self.init_pos = coord # use initial position to identify cart
        self.coord = coord
        self.facing = facing
        self.turns = 0
        self.crashed = False

    def next_turn(self):
        t = [-1, 0, 1]
        result = t[self.turns % 3]
        self.turns += 1
        return result

    def __repr__(self):
        return "{}: facing {} with {} turns".format(self.coord, self.facing, self.turns)

def part1(tracks):
    carts = get_carts(tracks)
    print("Found {} carts".format(len(carts)))
    # print_tracks(tracks)
    while True:
        collision = False
        order = get_order(carts)
        for cart in order:
            move_cart(tracks, cart)
            if cart.coord in [c.coord for c in carts if c.init_pos != cart.init_pos]:
                print("Found crash at {}!".format(cart.coord))
                collision = True
                break
        if collision:
            break
                
def part2(tracks):
    carts = get_carts(tracks)
    print("Found {} carts".format(len(carts)))
    # print_tracks(tracks)
    while True:
        order = get_order(carts)
        for cart in order:
            if not cart.crashed:
                move_cart(tracks, cart)
                if cart.coord in [c.coord for c in carts if c.init_pos != cart.init_pos]:
                    print("Found crash at {}!".format(cart.coord))                
                    cart.crashed = True
                    other_cart = [c for c in carts if c.init_pos != cart.init_pos and c.coord == cart.coord]
                    if len(other_cart) > 1:
                        print("Multi-cart crash???")
                    other_cart[0].crashed = True

        carts = [c for c in carts if not c.crashed]
        if len(carts) == 1:
            print("Last remaining cart at {}".format(carts[0].coord))
            break

# move cart in its current direction and turn if needed
def move_cart(tracks, cart):
    v = next_move(cart.facing)
    new_pos = (cart.coord[0] + v[0], cart.coord[1] + v[1])
    t = get_track_at_pos(tracks, new_pos)
    new_dir = next_dir(cart, t)
    cart.coord = new_pos
    cart.facing = new_dir
    # print("{} next track = {}".format(cart, t))

    # # turn cart according to new location
    # if t == '/' and v[1]
    # pass

# return character representing type of track at coord
def get_track_at_pos(tracks, coord):
    return tracks[coord[1]][coord[0]]

def get_order(carts):
    order = sorted(carts, key=lambda c:c.coord, cmp=compare_coord) # coordinate of cart
    print("order = {}".format(order))
    return order

# sort coordinates with y component taking precedence over x
def compare_coord(c1, c2):
    if c1 == c2:
        return 0
    elif c1[1] > c2[1]:
        return 1
    elif c1[1] < c2[1]:
        return -1
    elif c1[1] == c2[1]:
        return 1 if c1[0] > c2[0] else -1    

def is_cart(c):
    return c in ['v', '^', '<', '>']

# convert initial cart positions and directions to corresponding track
def track_by_dir(d):
    if d in ['v', '^']:
        return '|'
    elif d in ['>', '<']:
        return '-'
    else:
        print("Unexpected dir {}".format(d))

# given cur_dir, turn clockwise rots times,
# counter clockwise if rots < 0
def turn(cur_dir, rots):
    dirs = ['^', '>', 'v', '<']
    cidx = dirs.index(cur_dir)
    result = dirs[(cidx + rots) % 4]
    # print("{} rotated {} times yields {}".format(cur_dir, rots, result))
    return result

# return (delta x, delta y) for current direction
def next_move(d):
    md = {'v':(0,1), '^':(0,-1), '>':(1,0), '<':(-1,0)}
    return md[d]

def next_dir(cart, next_track):
    cur_dir = cart.facing
    if cur_dir in ['^','v']:
        if next_track == '|':
            return cur_dir
        elif next_track == '\\':
            return turn(cur_dir, -1)
        elif next_track == '/':
            return turn(cur_dir, 1)
        elif next_track == '+':
            return turn(cur_dir, cart.next_turn())
        else:
            print("Unexpected track type {}".format(next_track))
    elif cur_dir in ['<', '>']:
        if next_track == '-':
            return cur_dir
        elif next_track == '\\':
            return turn(cur_dir, 1)
        elif next_track == '/':
            return turn(cur_dir, -1)
        elif next_track == '+':
            return turn(cur_dir, cart.next_turn())
        else:
            print("Unexpected track type {}".format(next_track))
    return None

# given tracks input, create Carts and update tracks with
# appropriate track type
def get_carts(tracks):
    carts = []
    for y, row in enumerate(tracks):
        for x, item in enumerate(row):
            if is_cart(item):
                carts.append(Cart((x,y), item))
                row[x] = track_by_dir(item)
                print("Replacing cart {} with track {}".format(item, row[x]))
    return carts

def print_tracks(tracks):
    for row in tracks:
        print("".join(row))

if __name__ == "__main__":
    tracks = parse_day13("day13input.txt")
    # tracks = parse_day13("day13example.txt")
    # part1(tracks)
    part2(tracks)

    # turn('^', 0)
    # turn('^', 1)
    # turn('^', 2)
    # turn('^', 3)
    # turn('>', -1)
    # turn('<', -2)
    # turn('v', -3)
    # order_test = [(1,0), (2,0), (2,1), (0,1), (1,1), (2,2)]
    # print("Test: {}".format(get_order(order_test)))
