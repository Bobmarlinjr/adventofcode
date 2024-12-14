from pathlib import Path
Day8_input = open(Path(__file__).parent / "Day8_input.txt").read()

################################
###--------- PART 1 ---------###
################################

# Store the locations of all nodes of the same kind in dictionary.
# Iterate over all combinations of nodes of the same kind
# Find distance between nodes, use this to calculate locations of antinodes.
# Check if antinode coordinate already exists

def collect_nodes(node_map):
    node_dic = {}
    for y, row in enumerate(node_map):
        for x, ele in enumerate(row):
            if ele != ".":
                if node_dic.get(ele) == None:
                    node_dic[ele] = [(x, y)]
                else:
                    node_dic[ele].append((x,y))
    return node_dic

def compute_combinations(l):
    combos = []
    if len(l) < 2:
        raise Exception("too few values to get combos!")
    if len(l) == 2:
        return [[l[0], l[1]]]
    for x in l[1:]:
        combos.extend([[l[0], x]])
    combos.extend(compute_combinations(l[1:]))
    return(combos)

def check_edges(node_map, node):
    if node[1] in range(len(node_map)) and node[0] in range(len(node_map[0])):
        return True
    return False

def check_for_antinodes(node_map, nodes):
    found_antinodes = []
    for node_type, coords in nodes.items():
        for coord_combo in compute_combinations(coords):
            delta_x = coord_combo[0][0] - coord_combo[1][0]
            delta_y = coord_combo[0][1] - coord_combo[1][1]
            antinode1 = (coord_combo[0][0] + delta_x, coord_combo[0][1] + delta_y)
            antinode2 = (coord_combo[1][0] - delta_x, coord_combo[1][1] - delta_y)
            if antinode1 not in found_antinodes and check_edges(node_map, antinode1):
                found_antinodes.append(antinode1)
            if antinode2 not in found_antinodes and check_edges(node_map, antinode2):
                found_antinodes.append(antinode2)
    return found_antinodes


node_map = [[x for x in line] for line in Day8_input.split("\n")]
node_collection = collect_nodes(node_map)

print(f"Number of Valid Antinode Positions: {len(check_for_antinodes(node_map, node_collection))}")

################################
###--------- PART 2 ---------###
################################

def check_for_resonance(node_map, nodes):
    found_antinodes = []
    for node_type, coords in nodes.items():
        for coord_combo in compute_combinations(coords):
            delta_x = coord_combo[0][0] - coord_combo[1][0]
            delta_y = coord_combo[0][1] - coord_combo[1][1]
            m = 1
            d = {"an1_inrange": True, "an2_inrange": True}
            while d["an1_inrange"] or d["an2_inrange"]:
                antinode1 = (coord_combo[1][0] + (delta_x * m), coord_combo[1][1] + (delta_y * m))
                antinode2 = (coord_combo[0][0] - (delta_x * m), coord_combo[0][1] - (delta_y * m))
                for i, an in enumerate([antinode1, antinode2]):
                    if not check_edges(node_map, an):
                        d[f"an{i + 1}_inrange"] = False
                        continue
                    if an not in found_antinodes:
                        found_antinodes.append(an)
                m += 1
    return found_antinodes

print(f"Antinodes Accounting for Resonance: {len(check_for_resonance(node_map, node_collection))}")
