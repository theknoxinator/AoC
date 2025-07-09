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

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 3), (sample2, 4), (sample3, 0), (sample4, 9)
    ])
    def test_sample(self, sample, expected):
        check(sample, day1.part1, expected)

    def test_part1(self):
        run(self.problem, day1.part1)

    @pytest.mark.parametrize("sample,expected", [
        (sample5, 6), (sample6, 0), (sample7, 4), (sample8, 12), (sample9, 4)
    ])
    def test_sample2(self, sample, expected):
        check(sample, day1.part2, expected)

    def test_part2(self):
        run(self.problem, day1.part2)


class TestDay2:
    problem = "Day2/input.txt"
    sample1 = "Day2/sample1.txt"
    sample2 = "Day2/sample2.txt"

    def test_sample(self):
        check(self.sample1, day2.part1, 18)

    def test_part1(self):
        run(self.problem, day2.part1)

    def test_sample2(self):
        check(self.sample2, day2.part2, 9)

    def test_part2(self):
        run(self.problem, day2.part2)


class TestDay3:
    problem = "Day3/input.txt"
    sample1 = "Day3/sample1.txt"
    sample2 = "Day3/sample2.txt"
    sample3 = "Day3/sample3.txt"
    sample4 = "Day3/sample4.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 0), (sample2, 3), (sample3, 2), (sample4, 31)
    ])
    def test_sample(self, sample, expected):
        check(sample, day3.part1, expected)

    def test_part1(self):
        run(self.problem, day3.part1)

    def test_part2(self):
        run(self.problem, day3.part2)


class TestDay4:
    problem = "Day4/input.txt"
    sample1 = "Day4/sample1.txt"
    sample2 = "Day4/sample2.txt"

    def test_sample(self):
        check(self.sample1, day4.part1, 2)

    def test_part1(self):
        run(self.problem, day4.part1)

    def test_sample2(self):
        check(self.sample2, day4.part2, 3)

    def test_part2(self):
        run(self.problem, day4.part2)


class TestDay5:
    problem = "Day5/input.txt"
    sample1 = "Day5/sample1.txt"

    def test_sample(self):
        check(self.sample1, day5.part1, 5)

    def test_part1(self):
        run(self.problem, day5.part1)

    def test_sample2(self):
        check(self.sample1, day5.part2, 10)

    def test_part2(self):
        run(self.problem, day5.part2)


class TestDay6:
    problem = "Day6/input.txt"
    sample1 = "Day6/sample1.txt"

    def test_sample(self):
        check(self.sample1, day6.part1, 5)

    def test_part1(self):
        run(self.problem, day6.part1)

    def test_sample2(self):
        check(self.sample1, day6.part2, 4)

    def test_part2(self):
        run(self.problem, day6.part2)


class TestDay7:
    problem = "Day7/input.txt"
    sample1 = "Day7/sample1.txt"

    def test_sample(self):
        check(self.sample1, day7.part1, "tknk")

    def test_part1(self):
        run(self.problem, day7.part1)

    def test_sample2(self):
        check(self.sample1, day7.part2, 60)

    def test_part2(self):
        run(self.problem, day7.part2)


class TestDay8:
    problem = "Day8/input.txt"
    sample1 = "Day8/sample1.txt"

    def test_sample(self):
        check(self.sample1, day8.part1, 1)

    def test_part1(self):
        run(self.problem, day8.part1)

    def test_sample2(self):
        check(self.sample1, day8.part2, 10)

    def test_part2(self):
        run(self.problem, day8.part2)


class TestDay9:
    problem = "Day9/input.txt"
    sample1 = "Day9/sample1.txt"
    sample2 = "Day9/sample2.txt"
    sample3 = "Day9/sample3.txt"
    sample4 = "Day9/sample4.txt"
    sample5 = "Day9/sample5.txt"
    sample6 = "Day9/sample6.txt"
    sample7 = "Day9/sample7.txt"
    sample8 = "Day9/sample8.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 1), (sample2, 6), (sample3, 5), (sample4, 16),
        (sample5, 1), (sample6, 9), (sample7, 9), (sample8, 3)
    ])
    def test_sample(self, sample, expected):
        check(sample, day9.part1, expected)

    def test_part1(self):
        run(self.problem, day9.part1)

    def test_part2(self):
        run(self.problem, day9.part2)


class TestDay10:
    problem = "Day10/input.txt"
    sample1 = "Day10/sample1.txt"
    sample2 = "Day10/sample2.txt"

    def test_sample(self):
        check(self.sample1, day10.part1, 12)

    def test_part1(self):
        run(self.problem, day10.part1)

    def test_sample2(self):
        check(self.sample2, day10.part2, "63960835bcdc130f0b66d7ff4f6a5a8e")

    def test_part2(self):
        run(self.problem, day10.part2)


class TestDay11:
    problem = "Day11/input.txt"
    sample1 = "Day11/sample1.txt"
    sample2 = "Day11/sample2.txt"
    sample3 = "Day11/sample3.txt"
    sample4 = "Day11/sample4.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 3), (sample2, 0), (sample3, 2), (sample4, 3)
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

    def test_sample(self):
        check(self.sample1, day12.part1, 6)

    def test_part1(self):
        run(self.problem, day12.part1)

    def test_sample2(self):
        check(self.sample1, day12.part2, 2)

    def test_part2(self):
        run(self.problem, day12.part2)


class TestDay13:
    problem = "Day13/input.txt"
    sample1 = "Day13/sample1.txt"

    def test_sample(self):
        check(self.sample1, day13.part1, 24)

    def test_part1(self):
        run(self.problem, day13.part1)

    # def test_sample2(self):
    #     check(self.sample1, day13.part2, 2)
    #
    # def test_part2(self):
    #     run(self.problem, day13.part2)
