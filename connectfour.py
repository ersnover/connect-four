players = {1: "#",
2: "@"}

def BoardInit():
    board = []
    for i in range(6):
        board.append(["O"] * 7)
    return board

def PrintBoard(board):
    for row in board:
        print(" ".join(row))
    print("-------------")
    print("1 2 3 4 5 6 7\n")

def GameInit():
    print("\nWelcome to Connect 4!\n")
    TurnNum = 1
    board = BoardInit()
    PrintBoard(board)
    return TurnNum, board

def WhoTurn(TurnNum):
    if TurnNum % 2 == 0:
        player = 2
    else:
        player = 1
    return player

def GetCol():
    col = input("Which column? \n>> ")
    try:
        col=int(col)
        while col < 1 or col > 7:
            print("Please choose column 1 - 7")
            col = int(input("Which column? \n>> "))
        return col
    except:
        print("Please enter a number")
        GetCol()

def UpdateBoard(col, player, board):
    for i in range(5,0,-1):
        if board[i][col] == "O":
            board[i][col] = players[player]
            break
    return board

def Turn(TurnNum, board):
    player  = WhoTurn(TurnNum)
    print(f"Player {player}! Your turn!")
    col = GetCol() - 1
    UpdateBoard(col, player, board)
    PrintBoard(board)
    TurnNum += 1
    return TurnNum,board, player

def Play():
    GameOver = False
    TurnNum, board = GameInit()
    while GameOver == False:
        TurnNum, board, player= Turn(TurnNum, board)
        GameOver = WinCheck(board, player)
    print(f"Congratulations Player {player}!! You win!!!")

#Following Functions check winning conditions

def ColumnFlip(board):
    ColArray = [[],[],[],[],[],[],[]]
    for col in range(7):
        for row in range(6):
            ColArray[col].append(board[row][col])
    return ColArray

def RowCheck(board, player):
    token = players[player]
    for row in board:
        for i in range(4):
            if row[i] == token and row[i+1] == token and row[i+2] == token and row[i+3] == token:
                return True
    return False

def ColCheck(board, player):
    token = players[player]
    board = ColumnFlip(board)
    for row in board:
        for i in range(3):
            if row[i] == token and row[i+1] == token and row[i+2] == token and row[i+3] == token:
                return True
    return False

#All of this is for DiagCheck()
def fours(board):
    four = [[],[],[],[]]
    for a in range(0,4):
        four[0].append(board[3-a][a])
    for a in range(0,4):
        four[1].append(board[5-a][3+a])
    for a in range(0,4):
        four[2].append(board[2+a][0+a])
    for a in range(0,4):
        four[3].append(board[0+a][3+a])
    return four

def fives(board):
    five = [[],[],[],[]]
    for a in range(0,5):
        five[0].append(board[4-a][a])
    for a in range(0,5):
        five[1].append(board[5-a][2+a])
    for a in range(0,5):
        five[2].append(board[1+a][0+a])
    for a in range(0,5):
        five[3].append(board[a][2+a])
    return five

def sixes(board):
    six = [[],[],[],[]]
    for a in range(0,6):
        six[0].append(board[a][a])
    for a in range(0,6):
        six[1].append(board[a][1+a])
    for a in range(0,6):
        six[2].append(board[a][5-a])
    for a in range(0,6):
        six[3].append(board[5-a][1+a])
    return six

def DiagFlip(board):
    four = fours(board)
    five = fives(board)
    six = sixes(board)
    return four, five, six

def DiagCheck(board, player):
    token = players[player]
    four, five, six = DiagFlip(board)
    for row in four:
        if row[0] == token and row[1] == token and row[2] == token and row[3] == token:
            return True
    for row in five:
        for i in range(2):
            if row[i] == token and row[i+1] == token and row[i+2] == token and row[i+3] == token:
                return True
    for row in six:
        for i in range(3):
            if row[i] == token and row[i+1] == token and row[i+2] == token and row[i+3] == token:
                return True
                
    return False

#Combine all three Check functions

def WinCheck(board,player):
    WinRow = RowCheck(board, player)
    WinCol = ColCheck(board, player)
    WinDiag = DiagCheck(board, player)
    if WinRow or WinCol or WinDiag:
        return True
    else:
        return False

Play()