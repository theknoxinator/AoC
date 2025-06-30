import pytest
from common import *
import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day10
import day11
import day12
import day13
import day14
import day15
import day16
import day17
import day18
import day19
import day20
import day21
import day22
import day23
import day24
import day25


class TestDay1:
    problem = "Day1/input.txt"
    sample1 = "Day1/sample1.txt"
    sample2 = "Day1/sample2.txt"
    sample3 = "Day1/sample3.txt"
    sample4 = "Day1/sample4.txt"
    sample5 = "Day1/sample5.txt"
    sample6 = "Day1/sample6.txt"
    sample7 = "Day1/sample7.txt"
    sample8 = "Day1/sample8.txt"
    sample9 = "Day1/sample9.txt"
    sample10 = "Day1/sample10.txt"
    sample11 = "Day1/sample11.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 0), (sample2, 0), (sample3, 3),
        (sample4, 3), (sample5, 3), (sample6, -1),
        (sample7, -1), (sample8, -3), (sample9, -3)
    ])
    def test_sample(self, sample, expected):
        check(sample, day1.part1, expected)

    def test_part1(self):
        run(self.problem, day1.part1)

    @pytest.mark.parametrize("sample,expected", [
        (sample10, 1), (sample11, 5)
    ])
    def test_sample2(self, sample, expected):
        check(sample, day1.part2, expected)

    def test_part2(self):
        run(self.problem, day1.part2)


class TestDay2:
    problem = "Day2/input.txt"
    sample1 = "Day2/sample1.txt"
    sample2 = "Day2/sample2.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 58), (sample2, 43)
    ])
    def test_sample(self, sample, expected):
        check(sample, day2.part1, expected)

    def test_part1(self):
        run(self.problem, day2.part1)

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 34), (sample2, 14)
    ])
    def test_sample2(self, sample, expected):
        check(sample, day2.part2, expected)

    def test_part2(self):
        run(self.problem, day2.part2)


class TestDay3:
    problem = "Day3/input.txt"
    sample1 = "Day3/sample1.txt"
    sample2 = "Day3/sample2.txt"
    sample3 = "Day3/sample3.txt"
    sample4 = "Day3/sample4.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 2), (sample2, 4), (sample3, 2)
    ])
    def test_sample(self, sample, expected):
        check(sample, day3.part1, expected)

    def test_part1(self):
        run(self.problem, day3.part1)

    @pytest.mark.parametrize("sample,expected", [
        (sample4, 3), (sample2, 3), (sample3, 11)
    ])
    def test_sample2(self, sample, expected):
        check(sample, day3.part2, expected)

    def test_part2(self):
        run(self.problem, day3.part2)


class TestDay4:
    problem = "Day4/input.txt"
    sample1 = "Day4/sample1.txt"
    sample2 = "Day4/sample2.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 609043), (sample2, 1048970)
    ])
    def test_sample(self, sample, expected):
        check(sample, day4.part1, expected)

    def test_part1(self):
        run(self.problem, day4.part1)

    def test_part2(self):
        run(self.problem, day4.part2)


class TestDay5:
    problem = "Day5/input.txt"
    sample1 = "Day5/sample1.txt"
    sample2 = "Day5/sample2.txt"

    def test_sample(self):
        check(self.sample1, day5.part1, 2)

    def test_part1(self):
        run(self.problem, day5.part1)

    def test_sample2(self):
        check(self.sample2, day5.part2, 2)

    def test_part2(self):
        run(self.problem, day5.part2)


class TestDay6:
    problem = "Day6/input.txt"
    sample1 = "Day6/sample1.txt"
    sample2 = "Day6/sample2.txt"
    sample3 = "Day6/sample3.txt"
    sample4 = "Day6/sample4.txt"
    sample5 = "Day6/sample5.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 1000000), (sample2, 999000), (sample3, 998996),
        (sample4, 1), (sample5, 999999)
    ])
    def test_sample(self, sample, expected):
        check(sample, day6.part1, expected)

    def test_part1(self):
        run(self.problem, day6.part1)

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 1000000), (sample2, 1002000), (sample3, 1001996),
        (sample4, 1), (sample5, 2000001)
    ])
    def test_sample2(self, sample, expected):
        check(sample, day6.part2, expected)

    def test_part2(self):
        run(self.problem, day6.part2)


class TestDay7:
    problem = "Day7/input.txt"
    problem2 = "Day7/input2.txt"
    sample1 = "Day7/sample1.txt"

    def test_sample(self):
        check(self.sample1, day7.part1, {'d': 72, 'e': 507, 'f': 492,
                                         'g': 114, 'h': 65412, 'i': 65079,
                                         'x': 123, 'y': 456})

    def test_part1(self):
        run(self.problem, day7.part1)

    def test_part2(self):
        run(self.problem2, day7.part2)


class TestDay8:
    problem = "Day8/input.txt"
    sample1 = "Day8/sample1.txt"

    def test_sample(self):
        check(self.sample1, day8.part1, 12)

    def test_part1(self):
        run(self.problem, day8.part1)

    def test_sample2(self):
        check(self.sample1, day8.part2, 19)

    def test_part2(self):
        run(self.problem, day8.part2)


class TestDay9:
    problem = "Day9/input.txt"
    sample1 = "Day9/sample1.txt"

    def test_sample(self):
        check(self.sample1, day9.part1, 605)

    def test_part1(self):
        run(self.problem, day9.part1)

    def test_sample2(self):
        check(self.sample1, day9.part2, 982)

    def test_part2(self):
        run(self.problem, day9.part2)


class TestDay10:
    problem = "Day10/input.txt"
    sample1 = "Day10/sample1.txt"

    def test_sample(self):
        check(self.sample1, day10.part1, 82350)

    def test_part1(self):
        run(self.problem, day10.part1)

    def test_sample2(self):
        check(self.sample1, day10.part2, 1166642)

    def test_part2(self):
        run(self.problem, day10.part2)


class TestDay11:
    problem = "Day11/input.txt"
    sample1 = "Day11/sample1.txt"
    sample2 = "Day11/sample2.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, "abcdffaa"), (sample2, "ghjaabcc")
    ])
    def test_sample(self, sample, expected):
        check(sample, day11.part1, expected)

    def test_part1(self):
        run(self.problem, day11.part1)

    def test_part2(self):
        run(self.problem, day11.part2)


class TestDay12:
    problem = "Day12/input.txt"
    sample1 = "Day12/sample1.txt"
    sample2 = "Day12/sample2.txt"
    sample3 = "Day12/sample3.txt"
    sample4 = "Day12/sample4.txt"
    sample5 = "Day12/sample5.txt"
    sample6 = "Day12/sample6.txt"
    sample7 = "Day12/sample7.txt"
    sample8 = "Day12/sample8.txt"
    sample9 = "Day12/sample9.txt"
    sample10 = "Day12/sample10.txt"
    sample11 = "Day12/sample11.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 6), (sample2, 6), (sample3, 3), (sample4, 3),
        (sample5, 0), (sample6, 0), (sample7, 0), (sample8, 0)
    ])
    def test_sample(self, sample, expected):
        check(sample, day12.part1, expected)

    def test_part1(self):
        run(self.problem, day12.part1)

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 6), (sample9, 4), (sample10, 0), (sample11, 6)
    ])
    def test_sample2(self, sample, expected):
        check(sample, day12.part2, expected)

    def test_part2(self):
        run(self.problem, day12.part2)


class TestDay13:
    problem = "Day13/input.txt"
    sample1 = "Day13/sample1.txt"

    def test_sample(self):
        check(self.sample1, day13.part1, 330)

    def test_part1(self):
        run(self.problem, day13.part1)

    def test_part2(self):
        run(self.problem, day13.part2)


class TestDay14:
    problem = "Day14/input.txt"
    sample1 = "Day14/sample1.txt"

    def test_sample(self):
        check(self.sample1, day14.part1, 2660)

    def test_part1(self):
        run(self.problem, day14.part1)

    def test_part2(self):
        run(self.problem, day14.part2)


class TestDay15:
    problem = "Day15/input.txt"
    sample1 = "Day15/sample1.txt"

    def test_sample(self):
        check(self.sample1, day15.part1, 62842880)

    def test_part1(self):
        run(self.problem, day15.part1)

    def test_sample2(self):
        check(self.sample1, day15.part2, 57600000)

    def test_part2(self):
        run(self.problem, day15.part2)


class TestDay16:
    problem = "Day16/input.txt"

    def test_part1(self):
        run(self.problem, day16.part1)

    def test_part2(self):
        run(self.problem, day16.part2)


class TestDay17:
    problem = "Day17/input.txt"
    sample1 = "Day17/sample1.txt"

    def test_sample(self):
        check(self.sample1, day17.part1, 4)

    def test_part1(self):
        run(self.problem, day17.part1)

    def test_sample2(self):
        check(self.sample1, day17.part2, 3)

    def test_part2(self):
        run(self.problem, day17.part2)


class TestDay18:
    problem = "Day18/input.txt"
    sample1 = "Day18/sample1.txt"

    def test_sample(self):
        check(self.sample1, day18.part1, 4)

    def test_part1(self):
        run(self.problem, day18.part1)

    def test_sample2(self):
        check(self.sample1, day18.part2, 7)

    def test_part2(self):
        run(self.problem, day18.part2)


class TestDay19:
    problem = "Day19/input.txt"
    sample1 = "Day19/sample1.txt"

    def test_sample(self):
        check(self.sample1, day19.part1, 4)

    def test_part1(self):
        run(self.problem, day19.part1)

    def test_sample2(self):
        check(self.sample1, day19.part2, 3)

    def test_part2(self):
        run(self.problem, day19.part2)


class TestDay20:
    problem = "Day20/input.txt"

    def test_part1(self):
        run(self.problem, day20.part1)

    def test_part2(self):
        run(self.problem, day20.part2)


class TestDay21:
    problem = "Day21/input.txt"

    def test_part1(self):
        run(self.problem, day21.part1)

    def test_part2(self):
        run(self.problem, day21.part2)


class TestDay22:
    problem = "Day22/input.txt"

    def test_part1(self):
        run(self.problem, day22.part1)

    def test_part2(self):
        run(self.problem, day22.part2)


class TestDay23:
    problem = "Day23/input.txt"
    sample1 = "Day23/sample1.txt"

    def test_sample(self):
        check(self.sample1, day23.part1, {"a": 2, "b": 0})

    def test_part1(self):
        run(self.problem, day23.part1)

    def test_part2(self):
        run(self.problem, day23.part2)


class TestDay24:
    problem = "Day24/input.txt"
    sample1 = "Day24/sample1.txt"

    def test_sample(self):
        check(self.sample1, day24.part1, 99)

    def test_part1(self):
        run(self.problem, day24.part1)

    def test_sample2(self):
        check(self.sample1, day24.part2, 44)

    def test_part2(self):
        run(self.problem, day24.part2)


class TestDay25:
    problem = "Day25/input.txt"

    def test_part1(self):
        run(self.problem, day25.part1)
