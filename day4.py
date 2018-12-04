from inputs import parse_day4

# events - a list of (datetime, event string) tuples
def day4_part1(events):
    gid = None
    asleep = None
    sleeplog = {} # keyed on Guard ID
    for dt, event in events:
        if event[0] == 'G':
            gid = event.split()[1][1:]
            # print("New Guard #{}".format(gid))
        elif event[0] == 'f':
            asleep = dt.minute
        elif event[0] == 'w':
            if gid not in sleeplog:
                sleeplog[gid] = {m: 0 for m in range(60)}                
            for minute in range(asleep, dt.minute):
                sleeplog[gid][minute] += 1
        else:
            print "SOMETHING IS WRONG"
            return
    find_laziest(sleeplog)
    find_sleepiest_minute(sleeplog)

def find_sleepiest_minute(sleeplog):
    max_freq = -1
    max_minute = None
    max_gid = None
    for gid, sl in sleeplog.items():
        guardmax = max(sl.items(), key=lambda x:x[1])
        if guardmax[1] > max_freq:
            max_minute, max_freq = guardmax
            max_gid = gid
    print("Guard #{} slept during minute {} {} times.".format(max_gid, max_minute, max_freq))

def find_laziest(sleeplog):
    max_sleep = 0
    max_gid = None
    laziest_minute = None
    for gid, sl in sleeplog.items():
        if sum(sl.values()) > max_sleep:
            max_sleep = sum(sl.values())
            max_gid = gid
            laziest_minute = max(sl.items(), key=lambda x:x[1])[0]
    print("Laziest guard: #{}. Laziest minute: {}".format(max_gid, laziest_minute))

if __name__ == "__main__":
    events = parse_day4("day4input.txt")
    day4_part1(events)