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

def parse_day5(inputfile):
    polymer = ""
    with open(inputfile) as f:
        for line in f.readlines():
            polymer = line.strip()
    return polymer

def parse_day6(inputfile):
    coords = []
    with open(inputfile) as f:
        pattern = "([0-9]+), ([0-9]+)"
        for line in f.readlines():
            tokens = re.search(pattern, line)
            if tokens:
                coords.append((int(tokens.groups()[0]), int(tokens.groups()[1])))
    return coords

def parse_day7(inputfile):
    prereqs = [] # list of (required step, dependent step) tuples
    with open(inputfile) as f:
        pattern = "Step ([A-Z]) .+ ([A-Z]) can begin\."
        for line in f.readlines():
            tokens = re.search(pattern, line)
            if tokens:
                tup = tokens.groups()
                prereqs.append(tup)
    return prereqs