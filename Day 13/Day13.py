from pathlib import Path
Day13_input = open(Path(__file__).parent / "Day13_input.txt").read()

################################
###--------- PART 1 ---------###
################################

# Intersection of X and Y lines, if answers are whole numbers

# X = Axna + Bxnb
# Y = Ayna + Bynb

# [Ax Bx]  [na]    [X]
# [Ay By]* [nb]  = [Y]

# [By -Bx]     1/(AxBy - BxAy)
# [-Ay Ax] * 


def multiply_matrix(matx_A, matx_B):
    product = []
    curr_row = None
    for i in range(len(matx_A)):
        for j in range(len(list(matx_B[0]))):
            x = sum(a * b for a,b in zip(matx_A[i],[z[j] for z in matx_B]))
            if curr_row != i:
                product.append([x])
                curr_row = i
            else:
                product[i].append(x)
    return product


def solve_system(but_A, but_B, target):
    digits = len(str(target[0][0] // 1))
    sf = but_A[0]*but_B[1] - but_A[1]*but_B[0]
    A_inv = [[but_B[1]/sf, -but_B[0]/sf],[-but_A[1]/sf, but_A[0]/sf]]
    answers = multiply_matrix(A_inv, target)
    a_tok = abs(round(answers[0][0], 1)) if abs(answers[0][0] - round(answers[0][0], 1)) < 0.001 else 0
    b_tok = abs(round(answers[1][0], 1)) if abs(answers[1][0] - round(answers[1][0], 1)) < 0.001 else 0
    if but_A[0] * a_tok + but_B[0] * b_tok == target[0][0] and but_A[1] * a_tok + but_B[1] * b_tok == target[1][0]:
        return a_tok * 3 + b_tok
    else:
        return 0


def package_data(lines, offset=0):
    data = []
    for line in lines:
        data.append([int(z) for z in filter(None, ["".join(filter(str.isdigit, x)) for x in line.split(" ")])])
    button_A = data[0]
    button_B = data[1]
    target = [[x+offset] for x in data[2]]
    return button_A, button_B, target

buffer = []
total_tokens = 0
for x in Day13_input.split("\n"):
    if x == "":
        continue
    buffer.append(x)
    if len(buffer) == 3:
        total_tokens += int(solve_system(*package_data(buffer)))
        buffer = []

print(f"fewest tokens to win all prizes: {total_tokens}")

################################
###--------- PART 2 ---------###
################################

buffer = []
total_tokens = 0
for x in Day13_input.split("\n"):
    if x == "":
        continue
    buffer.append(x)
    if len(buffer) == 3:
        total_tokens += int(solve_system(*package_data(buffer, offset=1e13)))
        buffer = []

print(f"fewest tokens with conversion: {total_tokens}")