import argparse


def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="A simple CLI example")
    parser.add_argument("--name", type=str, default="World", help="Name to greet")
    parser.add_argument("--times", type=int, default=1, help="How many times to greet")
    args = parser.parse_args()

    # Main logic using the parsed arguments
    for _ in range(args.times):
        print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
