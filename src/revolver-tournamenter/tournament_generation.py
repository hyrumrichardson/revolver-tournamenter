import numpy as np
from pairings import generatePairings
from scoresheet_generator import create_scoresheet

# ------------------------------------------------------------
# MAIN FUNCTION: Create tournament workbook
# ------------------------------------------------------------
def create_tournament(filename="input.txt"):
    lines = []
    with open(filename, "r") as f:
        lines = [line.strip() for line in f]

    pairings = generatePairings(lines, 5)

    create_scoresheet(pairings)

create_tournament()
x = 2
