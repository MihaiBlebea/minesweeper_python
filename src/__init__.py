import argparse
from src.sweeper_board import SweeperBoard


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Mine Sweeper",
        description="This is just a mine sweeper board.",
        epilog="Pass the board size and enjoy.",
    )

    parser.add_argument("-x", "--columns", default=4, dest="x", type=int)
    parser.add_argument("-y", "--rows", default=4, dest="y", type=int)

    args = parser.parse_args()

    m = SweeperBoard(args.x, args.y)

    print("Generating a simple mine sweeper table:")
    print(m)

    print("Processig the table...\n")
    m.process()

    print("Result:")
    print(m)
