
board=[[ 1 ,-1 ,-1 ],
       [ 0 ,-1 , 0 ],
       [-1 ,-1 ,-1 ]]

tboard = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(3):
       for j in range(3):
              tboard[i][j]=board[j][i]


def check_line(line):
    if line[0] == line[1] == line[2]:
        return line[0]
    else:
        return 0

def check_row(tline):
    if tline[0] == tline[1] == tline[2]:
        return tline[0]
    else:
        return 0
def check_diagnol(line):
    if line[0][0] == line[1][1] == line[1][1]:
        return line[0][0]
    else: return 0

def check_tdiagnol(line):
    if line[0][2] == line[1][1] == line[2][0]:
        return line[0][2]
    else: return 0


def winlist():
    cha_list=[]
    cha_list.extend(list(map(check_line,board)))
    cha_list.extend(list(map(check_row,tboard)))
    cha_list.append(check_diagnol(board))
    cha_list.append(check_tdiagnol(board))
    return cha_list

def choose_one(list):
    for i in list:
        if i != 0 :
            return i
        else:
            continue


print(winlist())
print(choose_one(winlist()))



