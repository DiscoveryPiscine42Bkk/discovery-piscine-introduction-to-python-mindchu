#!/usr/bin/env python3

import sys
from checkmate import checkmate

def main():
    if len(sys.argv) == 1:
        return print("Error: No chessboard input")
    for i in range(1, len(sys.argv)):
        try:
            file = open(sys.argv[i], "r")
            board = file.read()
            checkmate(board)
            file.close()
        except:
            print("Error: Invalid file")

if __name__ == "__main__":
    main()
