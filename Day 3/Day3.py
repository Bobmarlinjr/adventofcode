from pathlib import Path
Day3_file = open(Path(__file__).parent / "Day3_input.txt")
Day3_input = Day3_file.read()

################################
###--------- PART 1 ---------###
################################

# Find all parts of the string starting in 'mul(' , then test for remaining criterion.
def find_substring_instances(substring, offset=0):
    instances = []
    start = 0
    while True:
        start = Day3_input.find(substring, start)
        if start == -1:
            break
        instances.append(start + 4) # index on first digit
        start += 1
    return instances

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

def check_mul(instances):
    products_list = []
    for mul_index in [x for x in instances]:
        if not digit_check(mul_index):
            # print("failed first number!")
            continue
        comma_index = digit_check(mul_index)
        first_number = int(Day3_input[mul_index:comma_index])
        if not Day3_input[comma_index] == ",":
            # print("failed comma!")
            continue
        comma_index += 1
        if not digit_check(comma_index):
            # print("failed second number!")
            continue
        cls_prths_index = digit_check(comma_index)
        second_number = int(Day3_input[comma_index:cls_prths_index])
        if not Day3_input[cls_prths_index] == ")":
            # print("failed parentheses!")
            continue
        products_list.append(first_number * second_number)
    return products_list

mul_instances = find_substring_instances("mul(", offset=4)
print(f"Sum of products: {sum(check_mul(mul_instances))}")

################################
###--------- PART 2 ---------###
################################

dont_instances = find_substring_instances("don't()")
do_instances = find_substring_instances("do()")

dont_do_pairs = [[dont_instances[0], do_instances[0]]]
dont_counter = 1
do_counter = 1
while True:
    if dont_instances[dont_counter] > dont_do_pairs[-1][1]:
        if do_instances[do_counter] > dont_instances[dont_counter]:
            dont_do_pairs.append([dont_instances[dont_counter], do_instances[do_counter]])
            dont_counter += 1
        else:
            do_counter += 1
    else:
        dont_counter += 1
    if dont_counter == len(dont_instances) or do_counter == len(do_instances):
        break

counter = 0
for index in [x for x in mul_instances]:
    if index > dont_do_pairs[counter][1]:
        counter += 1
    if counter == len(dont_do_pairs):
        break
    if dont_do_pairs[counter][0] < index < dont_do_pairs[counter][1]:
        mul_instances.remove(index)

print(f"Sum of Products with Conditionals: {sum(check_mul(mul_instances))}")


