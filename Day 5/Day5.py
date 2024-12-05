from pathlib import Path
Day5_input = open(Path(__file__).parent / "Day5_input.txt").read()

################################
###--------- PART 1 ---------###
################################

# For each line, pull any rule containing any two numbers in the sequence
rules = Day5_input.split("\n\n")[0]
updates = Day5_input.split("\n\n")[1]

rules = [[int(x) for x in line.split("|")] for line in rules.split("\n")]
updates = [[int(x) for x in line.split(",")] for line in updates.split("\n")]

associated_rules = {}
for sequence in updates:
    for rule in rules:
        if all(ele in sequence for ele in rule):
            if associated_rules.get(tuple(sequence)) == None:
                associated_rules[tuple(sequence)] = []
            associated_rules[tuple(sequence)].append(rule)

# Topological Sort using Kahn's Algorithm: 

# Count how many times a number must be after another (How many times does it appear as the second number in the rule):
# if no. of times is 0, add it to the sorted list. 
# Remove all rules that have that number as the first number
# Check if more numbers now qualify
# If number remains, list is unsortable.

def kahn_sort(sequence, rules):
    in_degrees = {}
    if len(sequence) == 1:
        return sequence
    for number in sequence:
        in_degrees[number] = 0
        for rule in rules:
            if rule[1] == number:
                in_degrees[number] += 1
        if in_degrees[number] == 0:
            new_seq = [x for x in sequence]
            new_seq.remove(number)
            new_rules = [x for x in rules]
            for rule in rules:
                if rule[0] == number:
                    new_rules.remove(rule)
            sorted_list = kahn_sort(new_seq, new_rules)
            if sorted_list is not False:
                return [number] + sorted_list
    return False

correct_sum = 0
fixed_sum = 0
for sequence in updates:
    result = kahn_sort(sequence, associated_rules[tuple(sequence)])
    if result != sequence:
        fixed_sum += result[len(result) // 2]
    else:
        correct_sum += result[len(result) // 2]

print(f"Sum of correct sequences:{correct_sum}")

################################
###--------- PART 2 ---------###
################################

print(f"Sum of fixed sequences: {fixed_sum}")


