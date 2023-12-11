# Ingest a game file and determine if feasible
import re


class CubeGame:
    def __init__(self, filename, red_limit, blue_limit, green_limit):
        self.file_contents = open(filename).read()
        self.GAME_ID_REGEX = re.compile(r"^Game (\d+):")
        self.BLUE_COUNT_REGEX = re.compile(r"(\d+) blue")
        self.GREEN_COUNT_REGEX = re.compile(r"(\d+) green")
        self.RED_COUNT_REGEX = re.compile(r"(\d+) red")
        self.red_limit = red_limit
        self.blue_limit = blue_limit
        self.green_limit = green_limit

    def contents_generator(self):
        for line in self.file_contents.split("\n"):
            yield line

    def cube_counts(self, game_string):
        red_matches = self.RED_COUNT_REGEX.findall(game_string)
        green_matches = self.GREEN_COUNT_REGEX.findall(game_string)
        blue_matches = self.BLUE_COUNT_REGEX.findall(game_string)
        return {"red": red_matches, "blue": blue_matches, "green": green_matches}

    def validate_game(self, game_string):
        matches = self.cube_counts(game_string)
        invalid_red = [red for red in matches.get("red") if int(red) > self.red_limit]
        if len(invalid_red) > 0:
            return False

        invalid_green = [
            green for green in matches.get("green") if int(green) > self.green_limit
        ]
        if len(invalid_green) > 0:
            return False

        invalid_blue = [
            blue for blue in matches.get("blue") if int(blue) > self.blue_limit
        ]
        if len(invalid_blue) > 0:
            return False

        return True

    def valid_game_generator(self):
        for game in self.contents_generator():
            if len(game) > 0 and self.validate_game(game):
                yield int(self.GAME_ID_REGEX.findall(game)[0])

    def minimum_cubes_needed(self, game_string):
        matches = self.cube_counts(game_string)
        min_red_needed = max(map(int, matches.get("red")))
        min_green_needed = max(map(int, matches.get("green")))
        min_blue_needed = max(map(int, matches.get("blue")))

        return min_red_needed, min_green_needed, min_blue_needed

    @staticmethod
    def cube_game_power(red, green, blue):
        return red * green * blue

    def game_power_sum(self):
        power_sum = 0
        for game in self.contents_generator():
            if len(game) > 0:
                power_sum += self.cube_game_power(*self.minimum_cubes_needed(game))

        return power_sum
