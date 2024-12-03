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
        
        
        if diff > 0:
            current_trend = True
        elif diff < 0:
            current_trend = False
        else:
            return False  
        if increasing is None:
            increasing = current_trend
        if increasing != current_trend:
            return False
    return True
count = 0
for report in parsed_data:
    if isGood(report):
        count += 1
print(count)
    


