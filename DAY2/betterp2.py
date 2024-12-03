from itertools import pairwise

# Initialize a 2D list to store the parsed data
parsed_data = []

# Read data from the file
with open("input.txt", "r") as file:
    for line in file:
        # Split each line by whitespace and convert to integers
        row = list(map(int, line.split()))
        parsed_data.append(row)


def isGood(report):
    increasing = None
    for a, b in pairwise(report):
        diff = a - b
        if not (1 <= abs(diff) <= 3):
            return False
        current_trend = diff < 0
    
        if increasing is None:
            increasing = current_trend
        if increasing != current_trend:
            return False
    return True


def isGoodWithDamp(report):
    if isGood(report):
        return True
    for i in range(len(report)):
        newList = report[:i] + report[i+1:]
        if isGood(newList):
            return True
    return False

count = sum(1 for report in parsed_data if isGoodWithDamp(report))
print(count)

