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

    # Horizontal to right
    if (len(crossword[row]) - index) > 3 and crossword[row][index + 1] == "M" and crossword[row][index + 2] == "A" and crossword[row][index + 3] == "S":
        count += 1
    # Horizontal to left
    if index >= 3 and crossword[row][index - 1] == "M" and crossword[row][index - 2] == "A" and crossword[row][index - 3] == "S":
        count += 1
    # Up
    if row >= 3 and crossword[row - 1][index] == "M" and crossword[row - 2][index] == "A" and crossword[row - 3][index] == "S":
        count += 1
    # Down
    if (len(crossword) - row) > 3 and crossword[row + 1][index] == "M" and crossword[row + 2][index] == "A" and crossword[row + 3][index] == "S":
        count += 1
    # Up right
    if row >= 3 and (len(crossword[row]) - index) > 3 and crossword[row - 1][index + 1] == "M" and crossword[row - 2][index + 2] == "A" and crossword[row - 3][index + 3] == "S":
        count += 1
    # Up left
    if row >= 3 and index >= 3 and crossword[row - 1][index - 1] == "M" and crossword[row - 2][index - 2] == "A" and crossword[row - 3][index - 3] == "S":
        count += 1
    # Down right
    if (len(crossword) - row) > 3 and (len(crossword[row]) - index) > 3 and crossword[row + 1][index + 1] == "M" and crossword[row + 2][index + 2] == "A" and crossword[row + 3][index + 3] == "S":
        count += 1
    # Down left
    if (len(crossword) - row) > 3 and index >= 3 and crossword[row + 1][index - 1] == "M" and crossword[row + 2][index - 2] == "A" and crossword[row + 3][index - 3] == "S":
        count += 1

    return count

total = 0

for indexOfRow, row in enumerate(crossword):
    for indexOfChar, char in enumerate(row):
        if char == "X":
            total += check(indexOfRow, indexOfChar)
print(total)
