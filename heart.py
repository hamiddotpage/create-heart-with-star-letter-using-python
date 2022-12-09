for row in range(6):
    for colm in range(7):
        if (row == 0 and colm % 3 != 0) or (row == 1 and colm % 3 == 0) or (row - colm == 2) or (row + colm == 8):
            print("*", end="")
        else:
            print(" ", end="")
    print()
