def showboard():
     for i in range(3):
        print("---------------------------------------------------\n"*2)
        print("--              --               --              --\n"*2)
        print("--       ",x[3*i],"    --       ",x[3*i+1],"     --       ", x[3*i+2] ,"    --")
        print("--              --               --              --\n"*2)
        print("---------------------------------------------------\n"*2)

def tictactoe(winner):
    global turn
    showboard()
    if x[0] == "O" and x[1] == "O" and x[2] =="O" or x[3] == "O" and x[4] == "O" and x[5] =="O" or x[6] == "O" and x[7] == "O" and x[8] =="O" or x[0] == "O" and x[3] == "O" and x[6] =="O" or x[1] == "O" and x[4] == "O" and x[7] =="O" or x[2] == "O" and x[5] == "O" and x[8] =="O" or x[0] == "O" and x[4] == "O" and x[8] =="O" or x[2] == "O" and x[4] == "O" and x[6] =="O":
            return "1"
    if x[0] == "X" and x[1] == "X" and x[2] =="X" or x[3] == "X" and x[4] == "X" and x[5] =="X" or x[6] == "X" and x[7] == "X" and x[8] =="X" or x[0] == "X" and x[3] == "X" and x[6] =="X" or x[1] == "X" and x[4] == "X" and x[7] =="X" or x[2] == "X" and x[5] == "X" and x[8] =="X" or x[0] == "X" and x[4] == "X" and x[8] =="X" or x[2] == "X" and x[4] == "X" and x[6] =="X":
            return "2"
    else:
            if turn %2 ==1:
                
                y = 0
                try:
                    y = int(input(f"Player 1 turn {int ((turn+1)/2)}: "))-1
                    if x[y] == "O" or x[y] == "X":
                        print("Oops, this square is already taken!")
                    else:
                        x[y] = "O"
                        turn += 1
                except ValueError:
                    print("Please type an integer")
            else:
                    y = 0
                    try:
                        y = int(input(f"Player 2 turn {int ((turn)/2)-1}: "))-1
                        if x[y] == "O" or x[y] == "X":
                            print("Oops, this square is already taken!")
                        else:
                            x[y] = "X"
                            turn += 1
                    except ValueError:
                        print("Please type an integer")
            return "0"



x = [1,2,3,4,5,6,7,8,9]
print("Welcome to Tic-Tac-Toe\nType the number of the corresponding square on your turn")
global winner
winner = "0"
turn = 1

while turn <= 9:
    if winner == "0":
        winner = tictactoe(winner)
    if tictactoe(winner) == "1" or tictactoe(winner) == "2":
        winner = tictactoe(winner)
        print(f'Player {winner} wins!')
        break
if turn == 10:
    print("No one wins! Try again!")
        

   



