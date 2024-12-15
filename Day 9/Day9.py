from pathlib import Path
Day9_input = open(Path(__file__).parent / "Day9_input.txt").read()

################################
###--------- PART 1 ---------###
################################

def expand_diskmap(compressed_map, chunky=False):
    indx = 0
    id_num = 0
    togg = 1
    disk_map = {}
    for ele in compressed_map:
        if togg == -1 and chunky:
            disk_map["g-" + str(indx)] = int(ele)
        elif togg == 1 and chunky:
            disk_map["f-" + str(id_num) + "-" + str(indx)] = int(ele)
        for _ in range(int(ele)):
            if togg == 1 and not chunky:
                disk_map[indx] = id_num
            indx += 1
        id_num += 1 if togg == 1 else 0
        togg *= -1
    return disk_map, indx


def compact_data(data, max_write):
    writer = 0
    reader = max_write
    while True:
        while writer in data:
            writer += 1
        while reader not in data:
            reader -= 1
        if reader <= writer:
            break
        data[writer] = data[reader]
        del data[reader]
    return data


def evaluate_checksum(data):
    checksum = 0
    for index, value in data.items():
        if isinstance(index, int):
            checksum += index * value
    return checksum

def process_all(raw_map):
    return evaluate_checksum(compact_data(*expand_diskmap(raw_map)))

day9_copy = Day9_input
print(f"Checksum for Filesystem: {process_all(day9_copy)}")


################################
###--------- PART 2 ---------###
################################

def defragment_data(data):
    writer = 0
    reader = 0    
    for item in reversed(data.keys()):
        if item[0] == "f":
            reader = int(item.split("-")[-1])
            for x in sorted(data.keys(), key=lambda x: int(x.split("-")[-1])):
                writer = int(x.split("-")[-1])
                if reader <= writer:
                    break
                if x[0] == "g" and data[x] >= data[item]:
                    data["-".join(item.split("-")[:2] + [x.split("-")[1]])] = data[item]
                    data["g-" + str(int(x.split("-")[1]) + data[item])] = data[x] - data[item]
                    del data[item]
                    del data[x]
                    break
    return data     


def evaluate_chunky(data):
    checksum = 0
    for key, value in data.items():
        if key[0] != "f":
            continue
        for i in range(value):
            checksum += int(key.split("-")[1]) * (int(key.split("-")[2]) + i)
    return checksum


def process_chunky(raw_map):
    return evaluate_chunky(defragment_data(expand_diskmap(raw_map, chunky=True)[0]))

day9_copy = Day9_input
print(f"Maintaining File Continuity: {process_chunky(day9_copy)}")