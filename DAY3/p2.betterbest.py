import re

with open('input.txt', 'r') as file:
    content = file.read()

mul_pattern = r"mul\((\d+),\s*(\d+)\)"
do_pattern = r"\bdo\(\)"
dont_pattern = r"\bdon't\(\)"

mul_matches = [(int(match.group(1)), int(match.group(2))) 
               for match in re.finditer(mul_pattern, content)]

do_positions = [match.start() for match in re.finditer(do_pattern, content)]
dont_positions = [match.start() for match in re.finditer(dont_pattern, content)]

control_positions = [(pos, "do") for pos in do_positions] + \
                    [(pos, "don't") for pos in dont_positions]
control_positions.sort()


enabled = True 
total = 0

for x, y in mul_matches:
  
    for ctrl_pos, ctrl_type in control_positions:
        if ctrl_pos < content.index(f"mul({x},{y})"):
            enabled = (ctrl_type == "do")
        else:
            break  

    if enabled:
        total += x * y

print(total)
