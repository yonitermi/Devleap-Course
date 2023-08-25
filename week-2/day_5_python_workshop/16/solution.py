def main(board):
    for i in range(9):
        # Check rows
        if sorted(board[i]) != list(range(1, 10)):
            return 'Try again!'
        # Check columns
        if sorted([board[j][i] for j in range(9)]) != list(range(1, 10)):
            return 'Try again!'
            
    # Check 3x3 squares
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = []
            for x in range(3):
                for y in range(3):
                    square.append(board[i + x][j + y])
            if sorted(square) != list(range(1, 10)):
                return 'Try again!'
    
    return 'Finished!'