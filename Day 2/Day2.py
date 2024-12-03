from pathlib import Path
Day2_file = open(Path(__file__).parent / "Day2_input.txt")
Day2_input = Day2_file.read()

################################
###--------- PART 1 ---------###
################################

def determine_safety(sequence):
    prev_level = None
    for level in sequence:
        if prev_level is None:
            prev_level = level
            try:
                initial_sign = (sequence[1]-prev_level)/abs(sequence[1]-prev_level)
            except:
                return 0
            continue
        if not 1 <= abs(level-prev_level) <= 3:
            return 0
        if (level-prev_level)/abs(level-prev_level) != initial_sign:
            return 0
        prev_level = level
    return 1   

data = Day2_input.split("\n")
safe_reports = 0
for sequence in data:
    sequence = [int(x) for x in sequence.split(" ")]
    safe_reports += determine_safety(sequence)

print(f"Number of Safe Reports: {safe_reports}")

################################
###--------- PART 2 ---------###
################################

def determine_safety_dampener(sequence):
    prev_level = None
    damper_test = False
    for level in sequence:
        if prev_level is None:
            prev_level = level
            try:
                initial_sign = (sequence[1]-prev_level)/abs(sequence[1]-prev_level)
            except:
                damper_test = True
                break
            continue
        if not 1 <= abs(level-prev_level) <= 3:
            damper_test = True
            break
        if (level-prev_level)/abs(level-prev_level) != initial_sign:
            damper_test = True
            break
        prev_level = level
    if damper_test:
        for i in range(len(sequence)):
            seq_copy = [x for x in sequence]
            seq_copy.pop(i)
            if determine_safety(seq_copy) == 1:
                return 1
        return 0
    else:
        return 1

safe_reports = 0
for sequence in data:
    sequence = [int(x) for x in sequence.split(" ")]
    safe_reports += determine_safety_dampener(sequence)

print(f"Number of Safe Reports With Dampening: {safe_reports}")