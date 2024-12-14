from pathlib import Path
Day7_input = open(Path(__file__).parent / "Day7_input.txt").read()

################################
###--------- PART 1 ---------###
################################

# Recursion?

def solve_equation(target, sequence, current_total, concat_flag=False):
    if len(sequence) == 0:
        if current_total == target:
            return target
        else:
            return 0
    if solve_equation(target, sequence[1:], current_total * sequence[0], concat_flag) == target:
        return target
    elif solve_equation(target, sequence[1:], current_total + sequence[0], concat_flag) == target:
        return target
    elif concat_flag and solve_equation(target, sequence[1:], int(str(current_total) + str(sequence[0])), concat_flag) == target:
        return target
    else:
        return 0

calibration_data = {int(data.split(":")[0]):[int(x) for x in data.split(": ")[1].split(" ")] for data in Day7_input.split("\n")}

calibration_sum = 0
for key, value in calibration_data.items():
    calibration_sum += solve_equation(key, value[1:], value[0])

print(f"Sum of Correct Test Values: {calibration_sum}")

################################
###--------- PART 2 ---------###
################################

concat_sum = 0
calibration_data = {int(data.split(":")[0]):[int(x) for x in data.split(": ")[1].split(" ")] for data in Day7_input.split("\n")}
for key, value in calibration_data.items():
    concat_sum += solve_equation(key, value[1:], value[0], concat_flag=True)

#print(solve_equation(192, [8, 14], 17, concat_flag=True))
print(f"Sum of Correct Test Values with Concatenation: {concat_sum}")