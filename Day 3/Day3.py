from pathlib import Path
Day3_file = open(Path(__file__).parent / "Day3_input.txt")
Day3_input = Day3_file.read()

################################
###--------- PART 1 ---------###
################################

# Find all parts of the string starting in 'mul(' , then test for remaining criterion.
substring = "mul("
mul_instances = []
start = 0
while True:
    start = Day3_input.find(substring, start)
    if start == -1:
        break
    mul_instances.append(start + 4) # index on first digit
    start += 1

print(len(mul_instances))

def digit_check(index): #checks to see if at specific index, if there is a block of 1-3 digits. If true, returns new index of first non-digit.
    digit_counter = 0
    for i in range(4):
        if Day3_input[index + i].isdigit():
            digit_counter += 1
        else:
            break
    if digit_counter == 0 or digit_counter == 4:
        return False
    else:
        return index + i #index will be on first non-digit

products_list = []
for mul_index in [x for x in mul_instances]:
    if not digit_check(mul_index):
        print("failed first number!")
        continue
    comma_index = digit_check(mul_index)
    first_number = int(Day3_input[mul_index:comma_index])
    if not Day3_input[comma_index] == ",":
        print("failed comma!")
        continue
    comma_index += 1
    if not digit_check(comma_index):
        print("failed second number!")
        continue
    cls_prths_index = digit_check(comma_index)
    second_number = int(Day3_input[comma_index:cls_prths_index])
    if not Day3_input[cls_prths_index] == ")":
        print("failed parentheses!")
        continue
    products_list.append(first_number * second_number)

print(sum(products_list))