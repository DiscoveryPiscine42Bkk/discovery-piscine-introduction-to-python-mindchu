#!/usr/bin/env python3

import sys
from checkmate import checkmate

def main():
    if len(sys.argv) == 1:
        return print("Error: No chessboard input")
    for argv in sys.argv[1:]:
        try:
            file = open(argv, "r")
            board = file.read()
            checkmate(board)
            file.close()
        except:
            print("Error: Invalid file")

if __name__ == "__main__":
    main()
