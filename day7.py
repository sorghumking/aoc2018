import sys
from inputs import parse_day7

def part1(prereqs):
    done = []
    reqs = get_req_dict(prereqs)
    steps = reqs.keys()
    while len(done) < len(steps):
        ns = find_next_step(done, steps, reqs)
        done.append(ns)
    print("order: {}".format(''.join(done)))

def part2(prereqs, workers, basetime):
    done = []
    in_progress = {} # keyed on step, value is cur # of seconds on step
    reqs = get_req_dict(prereqs)
    steps = reqs.keys()
    sec = 0
    while True:
        # resolve completed steps
        completed = []
        for step in in_progress:
            if in_progress[step] == get_step_time(step, basetime):
                completed.append(step)
                print("Step {} done.".format(step))
        for c in completed:
            done.append(c)
            del in_progress[c]

        if len(done) == len(steps):
            break # we're done!

        # look for new available steps and assign workers if available
        while True:
            next_steps = [s for s in steps if s not in done and s not in in_progress]
            ns = find_next_step(done, next_steps, reqs)
            if ns and len(in_progress) < workers:
                # assign to worker if one is available
                in_progress[ns] = 0
            else:
                break

        # do work
        for step in in_progress:
            in_progress[step] += 1

        sec += 1

    print("Took {} seconds to complete all tasks.".format(sec))

def get_step_time(step, basetime):
    return (ord(step) - ord('A')) + 1 + basetime

def get_req_dict(prereqs):
    steps = []
    reqs = {}
    for pr in prereqs:
        steps.append(pr[0])
        steps.append(pr[1]) # ensure we catch all steps
        if pr[1] in reqs:
            reqs[pr[1]].append(pr[0])
        else:
            reqs[pr[1]] = [pr[0]]
    steps = list(set(steps)) # eliminate duplicate steps
    print("steps = {}".format(steps))

    # add entries for steps with no prerequisites
    for s in [s for s in steps if s not in reqs]:
        # print("Adding missing step {}".format(s))
        reqs[s] = []

    print("total steps: {}".format(len(steps)))
    return reqs

# done: list of completed steps
# steps: list of potential next steps
# reqs: dict with items dependent step: [prerequisite steps]
def find_next_step(done, steps, reqs):
    candidates = [] # list of possible next steps
    for s in steps:
        can_do_step = True
        for pr in reqs[s]:
            if pr not in done:
                can_do_step = False
                break
        if can_do_step and s not in done:
            candidates.append(s)
    if len(candidates) > 0:
        return min(candidates)
    else:
        return None

if __name__ == "__main__":
    # prereqs = [('C','A'),('C','F'),('A','B'),('A','D'),('B','E'),('D','E'),('F','E')]
    prereqs = parse_day7("day7input.txt")
    # print(prereqs)
    # part1(prereqs)
    part2(prereqs, workers=5, basetime=60)