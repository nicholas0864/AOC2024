
import re


with open('input.txt', 'r') as file:  
    content = file.read()


# pattern = r'mul.*?\)' 
# matches = re.findall(pattern, content)


# result_array = matches


usableCharacters = "mul(,)1234567890do()don't"
i = 0
while i < len(content):
    if content[i] not in usableCharacters:
        content = content.replace(content[i],'')
    else:
        i+=1

s = ""
on = None


usableForMult = '1234567890'

total = 0


#first version

for c in range(len(content)):

    if s == 'mul(' and on: #if the current part has mul( and do is on take the part from mul to next paranthesis, check if its valid, then do the operation
        newPart = content[c:content[c:].find(')')]
        matches = re.findall(re.escape('mul('), newPart)
        if len(matches) >= 2:
            newPart= newPart[newPart.find('mul',(newPart.find('mul')+1))+4:newPart.find(")")]
            newArray = newPart.split(",", 1)
            total += int(newArray[0]) * int(newArray[1])
        is_valid = all(char in usableForMult for char in newPart)
        if is_valid:
            newArray = newPart.split(",", 1)
            total += newArray[0] * newArray[1]

            
    elif s == 'do()':
        on = True
        s = ""
    elif s == 'don\'t()':
        on = False
        s = ""
    if ( not s.startswith("mul("[:len(s)]) or not s.startswith("do()"[:len(s)]) or not s.startswith("don't()"[:len(s)])):
        s = ""
    s += content[c]

print(total)
    







# print(result_array)
# total = 0
# for line in result_array:
#     is_valid = all(char in usableCharacters for char in line)
#     if is_valid:
#         if line != "mul)":
#             newLine = line[(line.find("(")+1):line.find(")")]
#             newArray = newLine.split(",", 1)
#             total += int(newArray[0]) * int(newArray[1])
#     if not is_valid:
#         matches = re.findall(re.escape('mul'), line)
#         if len(matches) >= 2:
#             print(line)
#             newLine= line[

#                 line.find('mul',(line.find('mul')+1))+4:line.find(")")
            
#             ]
#             newArray = newLine.split(",", 1)
#             total += int(newArray[0]) * int(newArray[1])

            

# print(total)



