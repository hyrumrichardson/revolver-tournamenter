from itertools import combinations
import random

# Given a list of players and a maximum number of rounds,
# Return a list of pairings such that each player has a random opponent for each round
# No byes allowed
def generatePairings(players, max_rounds):
    #TODO: throw error if max_rounds > players - 1 (round robin if they are equal)

    print(players)
    matches_played = {i: set() for i in players}
    pair_count = {i: 0 for i in players}

    # Ensure that no two players are paired together more than once
    def can_pair(p1, p2):
        return p2 not in matches_played[p1]

    # Total number of pairings made so far
    def pair_count_sum():
        sum = 0
        for p in pair_count:
            sum += pair_count[p]
        return sum

    
    def can_repair(p0, p1, p2):
        return p0 not in matches_played[p1] and p0 not in matches_played[p2]

    # Helper function for fixing 
    def try_repair():
        p0 = [p for p in pair_count if pair_count[p] < max_rounds][0]
        rest = [p for p in players if p != p0]

        for p1 in rest:
            for p2 in rest:
                if p1 == p2:
                    continue
                if can_repair(p0, p1, p2):
                    try:
                        pairs.remove((p1,p2))
                    except ValueError:
                        x = 2

                    try:
                        pairs.remove((p2,p1))
                    except ValueError:
                        x = 2

                    matches_played[p1].remove(p2)
                    matches_played[p2].remove(p1)

                    pairs.append((p0,p1))
                    pairs.append((p0,p2))

                    matches_played[p0].add(p1)
                    matches_played[p0].add(p2)
                    matches_played[p1].add(p0)
                    matches_played[p2].add(p0)

                    pair_count[p0] += 1
                    return      

    pairs = []
    while pair_count_sum() < max_rounds*len(players) - 1:

        candidates = sorted(players, key=lambda x: pair_count[x])

        for p1 in candidates:
            rest = [p for p in players if p != p1]
            random.shuffle(rest) 

            found = False
            for p2 in rest:
                if p1 == p2:
                    continue
                if can_pair(p1, p2) and pair_count[p1] < max_rounds and pair_count[p2] < max_rounds:
                    pairs.append((p1, p2))
                    matches_played[p1].add(p2)
                    matches_played[p2].add(p1)
                    pair_count[p1] += 1
                    pair_count[p2] += 1
                    break    

    if pair_count_sum() < max_rounds*len(players):
        try_repair()

    return pairs

#testplayers = ['bohrealis','W I G H T B O I','EmPython','lilly','SirSoften']

#print(generatePairings(testplayers, 3))
    


