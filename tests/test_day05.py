from advent_of_code_2023.helpers.almanac import Almanac
from tqdm import tqdm
from multiprocessing import Pool, cpu_count

def test_day05_example():
    test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    almanac = Almanac(test_input)

    print(almanac.seed_to_soil)
    print(almanac.seed_to_soil[0](98))
    print(almanac.seed_to_soil[0](79))
    print(almanac.seed_to_soil[1](79))

    location_array = []

    for seed in almanac.seeds:
        location = almanac.traverse_seed_to_location(seed)
        location_array.append(location)

    print(f"The minimum location is: {min(location_array)}")

    location_array = []

    work_log = [r for r in range(0, len(almanac.seeds), 2)]

    with Pool(cpu_count()) as pool:
        for min_loc in pool.imap_unordered(find_minimum_for_input_range, work_log):
            location_array.append(min_loc)

    print(f"The minimum location for Part 02 is: {min(location_array)}")

def find_minimum_for_input_range(seed_index):
    input_contents = open("inputs/input-05.txt").read()
    almanac = Almanac(input_contents)

    min_value = None

    print(f"Starting the traversal search for seed {almanac.seeds[seed_index]} with range of {almanac.seeds[seed_index+1]}")
    for seed in tqdm(range(almanac.seeds[seed_index], almanac.seeds[seed_index] + almanac.seeds[seed_index+1])):
        location = almanac.traverse_seed_to_location(seed)
        if min_value is None or location < min_value:
            min_value = location

    return min_value


def test_day05():
    input_contents = open("inputs/input-05.txt").read()
    almanac = Almanac(input_contents)

    location_array = []

    for seed in almanac.seeds:
        location = almanac.traverse_seed_to_location(seed)
        location_array.append(location)

    print(f"The minimum location for Part 01 is: {min(location_array)}")

    location_array = []

    work_log = [r for r in range(0, len(almanac.seeds), 2)]

    with Pool(cpu_count()) as pool:
        for min_loc in pool.imap_unordered(find_minimum_for_input_range, work_log):
            location_array.append(min_loc)

    print(f"The minimum location for Part 02 is: {min(location_array)}")