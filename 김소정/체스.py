chess_board=[[1,0,0,1,0],
             [0,0,0,0,0],
             [0,0,2,0,1],
             [0,1,0,0,0]]
q_x=0
q_y=0
for i in range(len(chess_board)):
    for j in range(len(chess_board)):
        if '2' == chess_board[i][j] :
            q_x=chess_board[i]
            q_y=chess_board[j]

for x in range(len(chess_board)):
    for y in range(len(chess_board)):
        if chess_board[x]==q_x :
            print(chess_board[x][y])
        elif chess_board[y]==q_y :
            print(chess_board[x][y])
            # 이거 실행이 안 돼요 엉엉
