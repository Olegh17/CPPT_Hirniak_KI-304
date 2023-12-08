import numpy as np


def main():
    print("Enter the side length of a square: ", end="")
    sideLength = int(input())

    print("Enter the filler symbol: ", end="")
    symbol = input()



    matrix = np.full((sideLength, sideLength), " ", dtype=str)

    for i in range(sideLength):
        for j in range(sideLength):
            if i >= j and (
                    (i < sideLength / 2 and j < sideLength / 2) or (i >= sideLength / 2 and j >= sideLength / 2)):
                matrix[i][j] = symbol
           # else:
            #    matrix[i][j] = ' '

    print(matrix)
    np.savetxt("Result.txt", matrix, fmt="%s", delimiter="")




if __name__ == "__main__":
    main()

