'''
Simple Tic Tac Toe Game
2 Players
'''
def printtac(tac):
    """Print the board"""
    print(tac[6]+" "+tac[7]+" "+tac[8])
    print(tac[3]+" "+tac[4]+" "+tac[5])
    print(tac[0]+" "+tac[1]+" "+tac[2])

def checkwin(tac, m):
    """Check if player m won"""

    flag = False
    # Check rows
    if tac[0:3] == [m, m, m] or tac[3:6] == [m, m, m] or tac[6:9] == [m, m, m]:
        flag = True

    # Check columns
    if tac[0] == m and tac[3] == m and tac[6] == m:
        flag = True

    if tac[1] == m and tac[4] == m and tac[7] == m:
        flag = True

    if tac[2] == m and tac[5] == m and tac[8] == m:
        flag = True

    #Check diagonals
    if tac[0] == m and tac[4] == m and tac[8] == m:
        flag = True

    if tac[2] == m and tac[4] == m and tac[6] == m:
        flag = True
    if flag:
        print(m + " won!")
    return flag

def starttac():
    """Driver"""

    # initialize board, variables
    tac = []
    for i in range(10):
        tac.append(".")
    won = False
    p_one = True

    # run program to take turns
    for i in range(9):
        printtac(tac)
        print("Take turn!")

        # take input until valid
        while True:
            key = int(input())
            if key <= 9 and tac[key-1] == ".":
                break
            print("Not a valid choice!")
            printtac(tac)

        # change board piece and swap player
        if p_one:
            tac[key-1] = "x"
        else:
            tac[key-1] = "o"
        p_one = not p_one

        # check win
        won = checkwin(tac, tac[key-1])
        if won:
            printtac(tac)
            break

    # check for draw
    if i == 8 and not won:
        printtac(tac)
        print("it's a draw!")
    input()
