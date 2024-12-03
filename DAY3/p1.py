# # Initialize a 2D list to store the parsed data
# parsed_data = ""


# with open("input.txt", "r") as file:
#     for line in file:
#         parsed_data += line


# left = 0
# right = 1
# total = 0
# while right < len(parsed_data):
#     currentLine = parsed_data[left:right+1]
#     if parsed_data[left] == "m":
#         if parsed_data[right] == ")":
#             if "(" in currentLine and ")" in currentLine and "mul" in currentLine and "," in currentLine:
#                 newLine = currentLine[(currentLine.find("(")+1):currentLine.find(")")]
#                 newArray = newLine.split(",", 1)
#                 if newArray[0] != "" and newArray[1] != "":
#                     total += (int(newArray[0]) * int(newArray[1]))
#                 left = right
#                 right = left + 1
#     elif parsed_data[left] != "m":
#         left += 1
#     right+=1

# print(total)


import re


with open('input.txt', 'r') as file:  
    content = file.read()


pattern = r'mul.*?\)' 
matches = re.findall(pattern, content)


result_array = matches


usableCharacters = "mul(,)1234567890"

total = 0

for line in result_array:
    is_valid = all(char in usableCharacters for char in line)
    if is_valid:
        if line != "mul)":
            newLine = line[(line.find("(")+1):line.find(")")]
            newArray = newLine.split(",", 1)
            total += int(newArray[0]) * int(newArray[1])
    if not is_valid:
        matches = re.findall(re.escape('mul'), line)
        if len(matches) >= 2:
            print(line)
            newLine= line[

                line.find('mul',(line.find('mul')+1))+4:line.find(")")
            
            ]
            newArray = newLine.split(",", 1)
            total += int(newArray[0]) * int(newArray[1])

            

print(total)



