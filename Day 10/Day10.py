from pathlib import Path
Day10_input = open(Path(__file__).parent / "Day10_input.txt").read()

################################
###--------- PART 1 ---------###
################################

def score_trailhead(tmap, pos, elev=0, found_9s={}):
    if elev == 9 and pos not in found_9s:
        return {pos: 0}
    for direction in [(1,0), (0,1), (-1,0), (0,-1)]:
        newpos = (pos[0] + direction[0], pos[1] + direction[1])
        if newpos[1] not in range(len(tmap)) or newpos[0] not in range(len(tmap[0])):
            continue
        if tmap[newpos[1]][newpos[0]] == elev + 1:
            found_9s = found_9s | score_trailhead(tmap, newpos, elev=elev+1, found_9s=found_9s)
    return found_9s

topo_map = [[int(x) for x in line] for line in Day10_input.split("\n")]

total_score = 0
for y, row in enumerate(topo_map):
    for x, ele in enumerate(row):
        if ele == 0:
            total_score += len(score_trailhead(topo_map, (x,y)))
print(f"Scores of all Trailheads: {total_score}")

################################
###--------- PART 2 ---------###
################################

def rate_trailhead(tmap, pos, elev=0):
    rating = 0
    if elev == 9:
        return 1
    for direction in [(1,0), (0,1), (-1,0), (0,-1)]:
        newpos = (pos[0] + direction[0], pos[1] + direction[1])
        if newpos[1] not in range(len(tmap)) or newpos[0] not in range(len(tmap[0])):
            continue
        if tmap[newpos[1]][newpos[0]] == elev + 1:
            rating += rate_trailhead(tmap, newpos, elev=elev+1)
    return rating

total_rating = 0
for y, row in enumerate(topo_map):
    for x, ele in enumerate(row):
        if ele == 0:
            total_rating += rate_trailhead(topo_map, (x,y))
print(f"Rating of all Trailheads: {total_rating}")