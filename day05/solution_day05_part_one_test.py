import unittest

from solution_day05 import MapRange, Range, parse_map, parse_seeds, parse_map, solve, map_seed

class SolutionDay05PartOne(unittest.TestCase):

    def test_should_map_values(self):
        input = ["seed-to-soil map:", "50 98 2\n", "52 50 48\n"]
        range = parse_map(input)
        expected_mappings = {
            0: 0,
            1: 1,
            48: 48,
            49: 49,
            50: 52,
            51: 53,
            96: 98,
            97: 99,
            98: 50,
            99: 51,
        }
        assert "seed-to-soil" == range.map_name
        for k, v in expected_mappings.items():
            print(f"Evaluating {k},{v}")
            assert v == range.map(k)

    def test_should_parse_the_seeds(self):
        seeds = "seeds: 79 14 55 13"
        expected_seeds = [79, 14, 55, 13]
        actual_seeds = parse_seeds(seeds)
        assert expected_seeds == actual_seeds

    def test_should_map_the_seeds(self):
        seed_to_soil = MapRange("seed-to-soil", [Range(50, 98, 2)])
        soil_to_fertilizer = MapRange("soil_to_fertilized", [Range(1000, 50, 10)])
        seed = 50
        expected_mapping = 1000
        actual_mapping = map_seed([seed_to_soil, soil_to_fertilizer], seed)
        assert expected_mapping == actual_mapping

    def test_should_solve_the_problem(self):
        problem_input = [
            "seeds: 79 14 55 13\n",
            "\n",
            "seed-to-soil map:\n",
            "50 98 2\n",
            "52 50 48\n",
            "\n",
            "soil-to-fertilizer map:\n",
            "0 15 37\n",
            "37 52 2\n",
            "39 0 15\n",
            "\n",
            "fertilizer-to-water map:\n",
            "49 53 8\n",
            "0 11 42\n",
            "42 0 7\n",
            "57 7 4\n",
            "\n",
            "water-to-light map:\n",
            "88 18 7\n",
            "18 25 70\n",
            "\n",
            "light-to-temperature map:\n",
            "45 77 23\n",
            "81 45 19\n",
            "68 64 13\n",
            "\n",
            "temperature-to-humidity map:\n",
            "0 69 1\n",
            "1 0 69\n",
            "\n",
            "humidity-to-location map:\n",
            "60 56 37\n",
            "56 93 4\n",
        ]
        expected = 35
        actual = solve(problem_input)
        assert expected == actual
