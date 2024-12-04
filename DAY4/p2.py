with open('input.txt', 'r') as file:  
    content = file.read()

usableChar = 'MAS'
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
    if (row > 0 and row < len(crossword)-1) and (index > 0 and index < len(crossword[row])-1):
        neighbors1 = [crossword[row-1][index-1], crossword[row+1][index+1]]
        if neighbors1.count("M") == 1 and neighbors1.count("S") == 1:
            neighbors2 = [crossword[row-1][index+1], crossword[row+1][index-1]]
            if neighbors2.count("M") == 1 and neighbors2.count("S") == 1:
                return True
    return False
    

count = 0
for indexOfRow, row in enumerate(crossword):
    for indexOfChar, char in enumerate(row):
        if char == "A" and check(indexOfRow, indexOfChar):
            count += 1
print(count)

