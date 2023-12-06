from pydantic import BaseModel

class ValueRange(BaseModel):
    start: int
    width: int
    offset: int

    def __call__(self, check_value: int):
        if check_value >= self.start and check_value <= (self.start + self.width - 1):
            return check_value + self.offset
        return None

class Almanac:
    def __init__(self, almanac_input):
        self.file_contents = almanac_input
        self.seeds = None
        self.seed_to_soil = []
        self.soil_to_fertilizer = []
        self.fertilizer_to_water = []
        self.water_to_light = []
        self.light_to_temperature = []
        self.temperature_to_humidity = []
        self.humidity_to_location = []
        self.map_map = {
            "seed-to-soil map:": self.seed_to_soil,
            "soil-to-fertilizer map:": self.soil_to_fertilizer,
            "fertilizer-to-water map:": self.fertilizer_to_water,
            "water-to-light map:": self.water_to_light,
            "light-to-temperature map:": self.light_to_temperature,
            "temperature-to-humidity map:": self.temperature_to_humidity,
            "humidity-to-location map:": self.humidity_to_location
        }

        self.parse_contents()
        
    def contents_generator(self) -> str:
        for line in self.file_contents.split("\n"):
            yield line

    def parse_contents(self):
        current_section = None
        for line in self.contents_generator():
            if len(line) > 0:
                if line.startswith("seeds:"):
                    self.seeds = [seed for seed in map(int, line[7:].split(" "))]
                elif line in self.map_map:
                    current_section = self.map_map[line]
                else:
                    if current_section is not None:
                        dest, source, width = [m for m in map(int, line.split(" "))]
                        current_section.append(ValueRange(start=source, width=width, offset=(dest - source)))

    def get_destination(self, source_value, map):
        range_map = self.map_map[map]
        for range_value in range_map:
            next_value = range_value(source_value)
            if next_value is not None:
                return next_value
        
        return source_value

    def traverse_seed_to_location(self, seed_value, debug=False):
        current_value = seed_value
        if debug:
            print(f"Starting with seed value of {current_value}")
        for map in self.map_map:
            current_value = self.get_destination(current_value, map)
            if debug:
                print(f"Destination value for {map} is {current_value}")

        return current_value

        return current_value

    