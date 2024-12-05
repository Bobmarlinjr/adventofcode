from pathlib import Path
Day2_file = open(Path(__file__).parent / "Day2_input.txt")
Day2_input = Day2_file.read()

################################
###--------- PART 1 ---------###
################################

def determine_safety(sequence, damping=False):
    if sequence[0] - sequence[1] == 0:
        if damping:
            return damper_test(sequence)
        return 0
    initial_sign = (sequence[1] - sequence[0]) / abs(sequence[1] - sequence[0])
    prev_level = sequence[0]
    for level in sequence[1:]:
        if not 1 <= abs(level-prev_level) <= 3:
            if damping:
                return damper_test(sequence)
            return 0
        if (level-prev_level)/abs(level-prev_level) != initial_sign:
            if damping:
                return damper_test(sequence)
            return 0
        prev_level = level
    return 1 

def damper_test(sequence):
    for i in range(len(sequence)):
        if determine_safety(sequence[:i] + sequence[i+1:]) == 1:
            return 1
    return 0

data = [[int(x) for x in line.split(" ")] for line in Day2_input.split("\n")]
safe_reports = sum([determine_safety(sequence) for sequence in data])
print(f"Number of Safe Reports: {safe_reports}")

################################
###--------- PART 2 ---------###
################################

safe_reports = sum([determine_safety(sequence, damping=True) for sequence in data])
print(f"Number of Safe Reports With Dampening: {safe_reports}")