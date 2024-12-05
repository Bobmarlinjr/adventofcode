from pathlib import Path
Day4_file = open(Path(__file__).parent / "Day4_input.txt")
Day4_input = Day4_file.read()

################################
###--------- PART 1 ---------###
################################

#starting at every "X" in the file, recursively check all 8 directions (keeping track of the previous letter.)

xmas_array = [list(x) for x in Day4_input.split("\n")]

def find_xmas(array):
    xmas_count = 0
    for i in range(len(array)):
        for j, letter in enumerate(array[i]):
            if letter == "X":
                xmas_count += complete_word(i, j, array)
    return xmas_count

def find_next_letter(row, col, i, j, array): #performs edge checking
    if row + i not in range(array) or col + j not in range(array[0]):
        return None
    return array[row + i][col + j]

def complete_word(row, col, array, ltrs_left=["M", "A", "S"], curr_dir=None):
    count = 0
    if curr_dir == None:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                next_letter_M = find_next_letter(row, col, i, j, array)
                if  next_letter_M == ltrs_left[0]:
                    count += complete_word(row + i, col + j, array, ltrs_left[1:], curr_dir=[i,j])
        return count
    else:
        next_letter = find_next_letter(row, col, curr_dir[0], curr_dir[1], array)
        if  next_letter != ltrs_left[0]:
            return 0
        elif len(ltrs_left) == 1:
            return 1
        else:
            return complete_word(row + curr_dir[0], col + curr_dir[1], array, ltrs_left[1:], curr_dir=curr_dir)

print(f"Number of XMAS's: {find_xmas(xmas_array)}")

################################
###--------- PART 2 ---------###
################################

def find_cross_mas(array):
    xmas_count = 0
    for i in range(len(array)):
        for j, letter in enumerate(array[i]):
            if letter == "A":
                xmas_count += complete_cross(i, j, array)
    return xmas_count

def complete_cross(row, col, array):
    mas_count = 0
    for i in [-1, 1]:
        for j in [-1, 1]:
            curr_letter = find_next_letter(row, col, i, j, array)
            if curr_letter in ["M", "S"]:
                remaining_letter = [x for x in ["M", "S"] if x != curr_letter]
                opposite_letter = find_next_letter(row, col, -i, -j, array)
                if opposite_letter in remaining_letter:
                    mas_count += 1
            if mas_count == 4:
                return 1
    return 0

print(f"Number of X-MAS's: {find_cross_mas(xmas_array)}")