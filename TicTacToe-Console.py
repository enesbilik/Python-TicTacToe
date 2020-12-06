current_player="O"
con=True
secilenler=[]
winner=None
board = ["-" , "-" , "-",
         "-" , "-" , "-",
         "-" , "-" , "-"]

def display_board():
    print(board[0]+"|"+board[1]+"|"+ board[2] + "   " + "1 | 2 | 3" )
    print(board[3]+"|"+board[4]+"|"+ board[5] + "   " + "4 | 5 | 6" )
    print(board[6]+"|"+board[7]+"|"+ board[8] + "   " + "7 | 8 | 9" )
    print("\n")
    try:
        position = int(input("Choose 1-9: "))-1
    except:
        print("Choose betwen 1-9")
        position = int(input())-1

    position=check_pos(position)



    if position not in secilenler:
        draw_shape(position)
        check_game()
        secilenler.append(position)
    else:
        print("{} Zaten Secildi".format(position+1))

def draw_shape(posi):
    flip_player()
    board[posi]=current_player


def flip_player():
  global current_player

  if current_player == "X":
    current_player = "O"

  elif current_player == "O":
    current_player = "X"

def check_game():
    global con
    if board[0]==board[1]==board[2]!= "-" or board[3]==board[4]==board[5]!= "-" or board[6]==board[7]==board[8]!= "-":
        winner=current_player
        print("Winner:",current_player)
        con=False
    elif board[0]==board[3]==board[6]!= "-" or board[1]==board[4]==board[7]!= "-" or board[2]==board[5]==board[8]!= "-":
        winner = current_player
        print("Winner:", current_player)
        con = False
    elif board[2]==board[4]==board[6]!= "-" or board[0]==board[4]==board[8]!= "-" :
        winner = current_player
        print("Winner:", current_player)
        con = False
    else:
        pass

def check_pos(position):
    if position>=9  or position<0:
        print("Choose betwen 1-9")
        try:
            position = int(input())-1
        except:
            print("Choose betwen 1-9")
            position=int(input())-1
        if position in range(-1,10):
            return position
        else:
            return check_pos(position)

    else:
        return position

while con:
    display_board()
