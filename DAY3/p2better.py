
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
on = True
mult = None
right = None
usableForMult = '1234567890'

total = 0


#first version

for c in content:
    print(s)
    if s == 'mul(' and on: 
        mult = True
        print("Mul( Check" + s)
        s = ""

    if c == ',' and mult:
        left = s
        print(", Check Check" + s)
        s= ""
        right = True
    if right and c == ")":
        total += int(s) * int(left)
        print(") Check" + s)
        s = ""
        right = False
        mult = False        
    
    elif s == 'do()':
        on = True
        print("Do Check" + s)
        s = ""
    elif s == 'don\'t()':
        on = False
        print("Don't Check" + s)
        s = ""
    # if ( not s.startswith("mul("[:len(s)]) or not s.startswith("do()"[:len(s)]) or not s.startswith("don't()"[:len(s)])):
    #     s = ""
    s += c

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



