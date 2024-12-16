from pathlib import Path
Day11_input = open(Path(__file__).parent / "Day11_input.txt").read()

################################
###--------- PART 1 ---------###
################################

#use dictionaries to keep track of indicies

def process_blinks(data, blinks):
    for _ in range(blinks):
        data_c = data.copy()
        for ele in data.keys():
            if len(str(ele)) % 2 == 0:
                middle_index = int(len(str(ele)) / 2)
                ele_left = int(str(ele)[:middle_index])
                ele_right = int(str(ele)[middle_index:])
                data_c[ele_right] = data_c.get(ele_right, 0) + data[ele]
                data_c[ele_left] = data_c.get(ele_left, 0) + data[ele]
                data_c[ele] -= data[ele]
            elif ele == 0:
                data_c[1] = data_c.get(1, 0) + data[ele]
                data_c[0] -= data[ele]
            else:
                data_c[ele * 2024]  = data_c.get(ele * 2024, 0) + data[ele]
                data_c[ele] -= data[ele]
            if data_c[ele] == 0:
                del data_c[ele]
        data = data_c
    return sum(data.values())

d = {}
for ele in [int(x) for x in Day11_input.split(" ")]:
    if d.get(ele):
        d[ele] += 1
    else:
        d[ele] = 1

print(f"Number of Stones after 25 Blinks: {process_blinks(d, 25)}")

################################
###--------- PART 2 ---------###
################################

print(f"Number of Stones after 75 Blinks: {process_blinks(d, 75)}")