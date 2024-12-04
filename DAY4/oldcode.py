with open('input.txt', 'r') as file:  
    content = file.read()

usableChar = 'XMAS'
crossword = []
for line in content.splitlines():
    row = []
    for char in line:
        if char in usableChar:
            row.append(char)
        else:
            row.append(".")
    crossword.append(row)



def check(row, index):

    count = 0

    #horizontal to right
    if (len(crossword[row]) - index) > 3 and crossword[row][index + 1] == "M" and crossword[row][index + 2] == "A" and crossword[row][index + 3] == "S":
        count += 1
    #horizontal to left
    if index > 3 and crossword[int(row)][index -1] == "M" and crossword[row][index - 2] == "A" and crossword[row][index - 3] == "S":
        count += 1
    #up
    if row > 3 and crossword[row+1][index] == "M" and crossword[row+2][index] == "A" and crossword[row+3][index] == "S":
        count += 1
    #down
    if len(crossword) - row > 3 and crossword[row-1][index] == "M" and crossword[row-2][index] == "A" and crossword[row-3][index] == "S":
        count += 1
    #up right
    if row > 3 and (len(crossword[row]) - index) > 3 and [row+1][index+1] == "M" and crossword[row+1][index+2] == "A" and crossword[row+3][index+3] == "S":
        count += 1
    #up left
    if row > 3 and index > 3 and crossword[row+1][index-1] == "M" and crossword[row+2][index-2] == "A" and crossword[row+3][index-3] == "S":
        count += 1
    #down right
    if len(crossword) - row > 3 and (len(crossword[row]) - index) > 3 and crossword[row-1][index+1] == "M" and crossword[row-2][index+2] == "A" and crossword[row-3][index+3] == "S":
        count += 1
    #down left
    if len(crossword) - row > 3 and index > 3 and crossword[row-1][index-1] == "M" and crossword[row-2][index-2] == "A" and crossword[row-3][index-3] == "S":
        count += 1
    return count

total = 0

for row in crossword:
    for i, char in enumerate(row):
        if char == "X":
            total += check(row, i)
print(total)
        
 # chars = ["M", "S", "M", "S"]
        # # up to right
        # if crossword[row-1][index+1] in chars:
        #     chars.remove(crossword[row-1][index+1])
        #     # up to left
        #     if crossword[row-1][index-1] in chars:
        #         chars.remove(crossword[row-1][index-1])
        #         # down to right
        #         if crossword[row+1][index+1] in chars:
        #             chars.remove(crossword[row+1][index+1])
        #             # down to left
        #             if crossword[row+1][index-1] in chars:
        #                 chars.remove(crossword[row+1][index-1])
        #                 return True