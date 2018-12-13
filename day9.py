
def part1(players, last_marble):
    # removed = []
    next_marble = 1
    cur_marble = 0 # index of current
    cur_player = 0
    scores = [0 for p in range(players)]
    circle = [0]

    while next_marble <= last_marble:
        marble_to_add = next_marble
        next_marble += 1

        if marble_to_add % 10000 == 0:
            print("Next Marble to add: #{}".format(marble_to_add))

        # determine where it should be placed
        if (marble_to_add % 23) == 0:
            scores[cur_player] += marble_to_add
            rm_idx = (cur_marble - 7) % len(circle)
            scores[cur_player] += circle[rm_idx]
            # print("Removed {}@{} from len {}".format(circle[rm_idx], rm_idx, len(circle)))
            # removed.append(circle[rm_idx])
            del circle[rm_idx]
            cur_marble = rm_idx % len(circle)
            # print("New current: {}".format(cur_marble))
            # print(circle)
        else:
            if len(circle) == 1:
                circle.append(marble_to_add)
                cur_marble = 1
            else:
                idx1 = (cur_marble + 1) % len(circle)
                idx2 = (cur_marble + 2) % len(circle)
                if idx1 > idx2: # insert at end
                    circle.append(marble_to_add)
                    cur_marble = len(circle) - 1
                    # print("Added {} at {}".format(marble_to_add, len(circle) - 1))
                else:
                    circle.insert(idx2, marble_to_add)
                    cur_marble = idx2
                    # print("Added {} at {}".format(marble_to_add, idx2))

        # print("Current Marble #{}, index {}".format(circle[cur_marble], cur_marble))

        # next player
        cur_player = (cur_player + 1) % players

    print("{} players, last marble {}: scores: {}".format(players, last_marble, scores))
    best = max(scores)
    best_player = scores.index(best) + 1
    print("Best player #{} with {} points".format(best_player, best))



if __name__ == "__main__":
    # part1(404, 71852)
    part1(404, 7185200) # part 2 - brute forced it
    # examples
    # part1(9, 25)
    # part1(10, 1618)
    # part1(13, 7999)
    # part1(17, 1104)
    # part1(21, 6111)
    # part1(30, 5807)