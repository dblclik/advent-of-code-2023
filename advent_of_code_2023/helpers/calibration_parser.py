class CalibrationParser:
    def __init__(self, filename):
        self.file_contents = open(filename).read()
        self.conversion_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }

    def contents_generator(self):
        for line in self.file_contents.split("\n"):
            yield line

    def string_to_numeral(self, input_text: str):
        final_text = ""
        conversion_map_items = self.conversion_map.items()
        i = 0
        while i < len(input_text):
            found = False
            for k, v in conversion_map_items:
                if input_text[i : (i + len(k))] == k:
                    final_text += v
                    found = True
                    i += 1
                    continue

            if not found:
                final_text += input_text[i]
                i += 1

        return final_text

    def correct_calibration_values(self, string_mapping: bool = False):
        for line in self.contents_generator():
            if string_mapping:
                line = self.string_to_numeral(line)
            numerical_values = [c for c in line if c.isnumeric()]
            if len(numerical_values) > 0:
                yield int(f"{numerical_values[0]}{numerical_values[-1]}")
