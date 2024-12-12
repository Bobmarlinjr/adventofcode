from pathlib import Path
Day6_input = open(Path(__file__).parent / "Day6_input.txt").read()

################################
###--------- PART 1 ---------###
################################

maze_master = [list(x) for x in Day6_input.split("\n")]
#[0,-1] -> [1,0] -> [0,1] -> [-1,0]
# multiply X by -1, then swap.

for y, row in enumerate(maze_master):
    for x, ele in enumerate(row):
        if ele == "^":
            START_POS = [x,y]

def simulate_guard(maze, obs_flag=False):
    obs_seen = {}
    current_pos = START_POS
    direction = [0,-1]
    tiles_visited = 0
    while current_pos[1] + direction[1] in range(len(maze)) and current_pos[0] + direction[0] in range(len(maze[0])):
        future_pos = [current_pos[0] + direction[0], current_pos[1] + direction[1]]
        if maze[future_pos[1]][future_pos[0]] == "#":
            if obs_flag:
                try:
                    curr_list = obs_seen[tuple(future_pos)]
                    # print(curr_list)
                    if tuple(direction) in curr_list:
                        return 1
                    else:
                        obs_seen[tuple(future_pos)].append(tuple(direction))
                except:
                    obs_seen[tuple(future_pos)] = [tuple(direction)]
            direction = [direction[1] * -1, direction[0]]
            continue
        if maze[future_pos[1]][future_pos[0]] != "#":
            if maze[future_pos[1]][future_pos[0]] == ".":
                tiles_visited += 1
            maze[current_pos[1]][current_pos[0]] = "X"
            current_pos = future_pos
    maze[current_pos[1]][current_pos[0]] = "X"
    if obs_flag:
        return 0
    return tiles_visited + 1

print(f"Total spaces visited: {simulate_guard([x[:] for x in maze_master])}")

################################
###--------- PART 2 ---------###
################################

# Keep a list of all obstacles encountered and directions in a dictionary: 
# if a matching pair exists, then there's a loop.

loops_created = 0
maze_copy = [_[:] for _ in maze_master]
for y, row in enumerate(maze_copy):
    for x, ele in enumerate(row):
        if ele == ".":
            alt_maze = [z[:] for z in maze_master]
            alt_maze[y][x] = "#"
            if simulate_guard([z[:] for z in alt_maze], obs_flag=True) == 1:
                loops_created += 1

print(f"Total valid loop-creating positions: {loops_created}")


