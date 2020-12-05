def main():
    count_1gr = 0
    count_2gr = 0
    count_1st = 0
    count_2st = 0
    count_1diag = 0
    count_2diag = 0
    count_1diagdeut = 0
    count_2diagdeut = 0
    order = 0
    round = 0
    step = 0
    board = []
    p1 = input('Player 1 = ')
    p2 = input('Player 2 = ')
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append(0)

    # orismos suntetagmenwn P1,P2

    while (1):
        round = round + 1
        print('---- Round ', round, '----')
        print('')
        for tmp in board:
            print(tmp)
        if order == 0:
            print('')
            print(p1, 'is playing (1)')
            while (1):
                x = int(input('x:'))
                while x < 0 or x > 2:
                    print('--Out of matrix bounds--')
                    print('x must be 0<=x<=2')
                    x = int(input('x:'))
                y = int(input('y:'))
                while y < 0 or y > 2:
                    print('--Out of matrix bounds--')
                    print('y must be 0<=y<=2')
                    y = int(input('y:'))
                if board[x][y] != 0:
                    print('Player 2 has captured this position')
                else:
                    board[x][y] = 1
                    order = 1
                    break
        else:
            print('')
            print(p2, 'is playing (2)')
            while (1):
                x = int(input('x:'))
                while x < 0 or x > 2:
                    print('--Out of matrix bounds--')
                    print('x must be 0<=x<=2')
                    x = int(input('x:'))
                y = int(input('y:'))
                while y < 0 or y > 2:
                    print('--Out of matrix bounds--')
                    print('y must be 0<=y<=2')
                    y = int(input('y:'))
                if board[x][y] != 0:
                    print('Player 1 has captured this position')
                else:
                    board[x][y] = 2
                    order = 0
                    break

        # elegxos nikhs

        for i in range(3):
            for j in range(3):
                if board[i][j] == 1:
                    count_1gr += 1
                elif board[i][j] == 2:
                    count_2gr += 1
        for i in range(3):
            for j in range(3):
                if board[j][i] == 1:
                    count_1st += 1
                elif board[j][i] == 2:
                    count_2st += 1

        # elegxos diagwniwn

        for i in range(3):
            if board[i][i] == 1:
                count_1diag += 1
            elif board[i][i] == 2:
                count_2diag += 1
        for i in range(3, 0):
            if board[i][step] == 1:
                count_1diagdeut += 1
            elif board[i][step] == 2:
                count_2diagdeut += 1
            step += 1
        if count_1gr == 3 or count_1st == 3 or count_1diag == 3 or count_1diagdeut == 3:
            for tmp in board:
                print(tmp)
            print('')
            print(p1, 'wins')
            break
        elif count_2gr == 3 or count_2st == 3 or count_2diag == 3 or count_2diagdeut == 3:
            for tmp in board:
                print(tmp)
            print('')
            print(p2, 'wins')
            break
        else:
            count_1gr = 0
            count_2gr = 0
            count_1st = 0
            count_2st = 0
            count_1diag = 0
            count_2diag = 0
            count_1diagdeut = 0
            count_2diagdeut = 0
            step = 0


if __name__ == "__main__":
    main()
