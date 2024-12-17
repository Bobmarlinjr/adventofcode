from pathlib import Path
Day12_input = open(Path(__file__).parent / "Day12_input.txt").read()

################################
###--------- PART 1 ---------###
################################

# Find the boundaries of a region via recursion, 
# store all valid region coordinates in dictionary
# Run function on any point not already in region by
# updating dictionary of regions 

def bound_region(p_map, coord, visited=[]):
    region = [coord]
    visited.extend([coord])
    region_char = p_map[coord[1]][coord[0]]
    for dirctn in [(0,1), (1,0), (0,-1), (-1,0)]:
        new_coord = (coord[0] + dirctn[0], coord[1] + dirctn[1])
        if new_coord[1] not in range(len(p_map)) or new_coord[0] not in range(len(p_map[0])):
            continue
        if p_map[new_coord[1]][new_coord[0]] == region_char and new_coord not in visited:
            region.extend(bound_region(p_map, new_coord, visited))
    return region

plot_map = [[x for x in line] for line in Day12_input.split("\n")]

d = {}
region_num = 0
for y, line in enumerate(plot_map):
    for x, plot in enumerate(line):
        if any((x,y) in r for r in d.values()):
            continue
        else:
            d = d | {region_num: bound_region(plot_map, (x,y))}
            region_num += 1

# Make dictionary storing perimiters:
# Perimiter around 1 coordinate = 4 - # of neighbors

def calculate_perimeters(regions):
    d = {}
    for reg_id, coords in regions.items():
        d[reg_id] = 0
        for coord in coords:
            neighbor_count = 0
            for dirctn in [(0,1), (1,0), (0,-1), (-1,0)]:
                newcoord = (coord[0] + dirctn[0], coord[1] + dirctn[1])
                if newcoord in coords:
                    neighbor_count += 1
            d[reg_id] += (4 - neighbor_count)
    return d

price = 0
for key, perimeter in calculate_perimeters(d).items():
    price += perimeter * len(d[key])
print(f"Price of all fenced regions: {price}")

################################
###--------- PART 2 ---------###
################################

# Number of edges = number of corners
# Corners can occur at any diagonal to a cell, if cell occupied, no corner
# of component vectors to the cell are occupied:

#   []O                         []xx                  []xx
#    OXx                         OXx                   xXx
#     xx                          xx                   xxx
#
#   If both components         If one is occupied,    If both are occupied,
#   to the corner are open,    no corner exists.      corner also exists.
#   corner exists.


# EDGE CASE: if diagonal is occupied but neither of the component vectors are,
# then each cell has a corner counted for that diagonal direction. 
#   
#   X[]
#  []X

def calculate_edges(regions):
    d = {}
    for reg_id, coords in regions.items():
        d[reg_id] = 0
        for coord in coords:
            for c in [(1,1), (-1,-1), (1,-1), (-1,1)]:
                newcoord = (coord[0] + c[0], coord[1] + c[1])
                c1_bool = (coord[0], coord[1] + c[1]) in coords
                c2_bool = (coord[0] + c[0], coord[1]) in coords
                if newcoord in coords:
                    if c1_bool is False and c2_bool is False:
                        d[reg_id] += 1
                    continue
                if c1_bool == c2_bool:
                    d[reg_id] += 1
    return d

price = 0
for key, edges in calculate_edges(d).items():
    price += edges * len(d[key])
print(f"Price of Discounted Regions: {price}")