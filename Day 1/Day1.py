from pathlib import Path
Day1_file = open(Path(__file__).parent / "Day1_input.txt")
Day1_input = Day1_file.read()

################################
###--------- PART 1 ---------###
################################

#Build the lists
left_list = []
right_list = []
for list_pair in Day1_input.split("\n"):
    left_list.append(int(list_pair.split("   ")[0]))
    right_list.append(int(list_pair.split("   ")[1]))

#QuickSort both lists
def quicksort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        pivot = unsorted_list[0]
        small_side = quicksort([x for x in unsorted_list if x < pivot])
        center = [x for x in unsorted_list if x == pivot]
        big_side = quicksort([x for x in unsorted_list if x > pivot])
        sorted_list = small_side + center + big_side
    return sorted_list

left_list_sorted = quicksort(left_list)
right_list_sorted = quicksort(right_list)

#Subtract one list element from the other, and print the sum of the differences.
differences = 0
for i in range(len(left_list_sorted)):
    differences += abs(left_list_sorted[i] - right_list_sorted[i])
print(f"Total Distance: {differences}")

################################
###--------- PART 2 ---------###
################################

#Filter right list to only contain elements in left list
similarity_score = 0
for loc_id in left_list:
    similarity_score += (loc_id * len([x for x in right_list if x == loc_id]))

print(f"Similarity Score: {similarity_score}")