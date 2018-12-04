import re
import datetime

def parse_day3(inputfile):
    listy = []
    with open(inputfile) as f:
        pattern = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
        for line in f.readlines():
            tokens = re.search(pattern, line)
            if tokens:
                listy.append([int(tok) for tok in tokens.groups()])
    return listy

def parse_day4(inputfile):
    listy = []
    with open(inputfile) as f:
        pattern = "\[([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)\] (.+)"
        for line in f.readlines():
            tokens = re.search(pattern, line)
            if tokens:
                y, m, d, h, mins, event = tokens.groups()
                eventtime = datetime.datetime(int(y), int(m), int(d), int(h), int(mins))
                listy.append((eventtime, event))
    
    listy = sorted(listy, key=lambda x: x[0]) # sort by datetime
    # for l in listy:
    #     print(l)
    return listy