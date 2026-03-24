import numpy as np
from revolver_tournamenter.pairings import generatePairings
from revolver_tournamenter.scoresheet_generator import create_scoresheet

# ------------------------------------------------------------
# MAIN FUNCTION: Create tournament workbook
# ------------------------------------------------------------
def create_tournament(filename="x.txt"):
    lines = []
    with open(filename, "r") as f:
        lines = [line.strip() for line in f]

    pairings = generatePairings(lines, 5)

    create_scoresheet(pairings)

#create_tournament()
x = 2
