import argparse
from revolver_tournamenter.tournament_generation import create_tournament

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="A simple CLI example")
    parser.add_argument("--filename", type=str, default="input.txt", help="File name with list of participants and decklists")
    parser.add_argument("--rounds", type=int, default=5, help="Number of rounds in the tournament")
    args = parser.parse_args()

    # Main logic using the parsed arguments
    create_tournament(args.filename)

if __name__ == "__main__":
    main()
