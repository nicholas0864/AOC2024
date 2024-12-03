# Initialize a 2D list to store the parsed data
# This list will hold each report, where each report is a list of integers.
parsed_data = []

# Open the input file and process each line
# Reading the file containing reports, each report being a line of numbers
with open("input.txt", "r") as file:
    for line in file:
        # Split each line by whitespace and convert the values to integers
        # `map(int, line.split())` splits the line into individual strings and converts them to integers.
        row = list(map(int, line.split()))
        # Append the list of integers to `parsed_data`
        parsed_data.append(row)

# Function to check if a report is safe without modifications
def is_safe(report):
    """
    This function checks if a report is safe based on the following conditions:
    1. All differences between adjacent levels must be between 1 and 3.
    2. The levels must either be consistently increasing or consistently decreasing.
    
    Parameters:
    - report (list): A list of integers representing a single report.
    
    Returns:
    - bool: True if the report is safe, False otherwise.
    """
    increasing = None  # Track whether the report is increasing or decreasing (None if undetermined)
    
    # Iterate through the levels of the report to check adjacent differences
    for i in range(len(report) - 1):
        # Calculate the difference between adjacent levels
        diff = report[i + 1] - report[i]
        
        # Check if the difference is within the valid range (1 to 3 inclusive)
        if not (1 <= abs(diff) <= 3):
            return False  # If any difference is out of range, return False
        
        # Determine whether the current trend is increasing or decreasing
        current_trend = diff > 0  # True if increasing, False if decreasing
        
        # If no trend has been established yet, set it to the current trend
        if increasing is None:
            increasing = current_trend
        # If the trend changes (from increasing to decreasing or vice versa), return False
        elif increasing != current_trend:
            return False
    
    # If the loop completes without returning False, the report is safe
    return True

# Function to check if a report is safe or can be made safe by removing one level
def is_safe_with_dampener(report):
    """
    This function checks if a report is safe or can be made safe by removing a single level.
    A report is considered safe if it is already safe or if removing one level makes it safe.
    
    Parameters:
    - report (list): A list of integers representing a single report.
    
    Returns:
    - bool: True if the report is safe or can be made safe by removing one level, False otherwise.
    """
    # First, check if the report is already safe without any modifications
    if is_safe(report):
        return True
    
    # Try removing each level in turn and check if the modified report becomes safe
    for i in range(len(report)):
        # Create a modified report by removing the level at index `i`
        modified_report = report[:i] + report[i+1:]
        
        # If the modified report is safe, return True
        if is_safe(modified_report):
            return True
    
    # If no modification made the report safe, return False
    return False

# Count the number of safe reports using the `is_safe_with_dampener` function
# This will count all reports that are either already safe or can be made safe by removing one level
total_safe_reports = sum(1 for report in parsed_data if is_safe_with_dampener(report))

# Print the total number of safe reports
print(total_safe_reports)
