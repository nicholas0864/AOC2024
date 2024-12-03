# Initialize a 2D list to store the parsed data
parsed_data = []

# Read data from the file
with open("input.txt", "r") as file:
    for line in file:
        # Split each line by whitespace and convert to integers
        row = list(map(int, line.split()))
        parsed_data.append(row)

# Function to check if a report is valid
def is_safe_report(report):
    increasing = None  # True for increasing, False for decreasing, None for uninitialized
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        
        # Check the difference is between 1 and 3
        if not (1 <= abs(diff) <= 3):
            return False
        
        # Determine the direction of the trend
        if diff > 0:
            current_trend = True
        elif diff < 0:
            current_trend = False
        else:
            return False  # Equal values are invalid
        
        # Ensure the trend is consistent
        if increasing is None:
            increasing = current_trend
        elif increasing != current_trend:
            return False  # Trend direction changed
    return True

# Count the number of safe reports
total_safe_reports = sum(1 for report in parsed_data if is_safe_report(report))

print(total_safe_reports)
