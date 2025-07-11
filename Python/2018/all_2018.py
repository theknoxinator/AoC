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


class TestDay1:
    problem = "Day1/input.txt"
    sample1 = "Day1/sample1.txt"
    sample2 = "Day1/sample2.txt"
    sample3 = "Day1/sample3.txt"
    sample4 = "Day1/sample4.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 3), (sample2, 3), (sample3, 0), (sample4, -6)
    ])
    def test_sample(self, sample, expected):
        check(sample, day1.part1, expected)

    def test_part1(self):
        run(self.problem, day1.part1)

    def test_sample2(self):
        check(self.sample1, day1.part2, 2)

    def test_part2(self):
        run(self.problem, day1.part2)


class TestDay2:
    problem = "Day2/input.txt"
    sample1 = "Day2/sample1.txt"

    def test_sample(self):
        check(self.sample1, day2.part1, 12)

    def test_part1(self):
        run(self.problem, day2.part1)

    def test_part2(self):
        run(self.problem, day2.part2)


class TestDay3:
    problem = "Day3/input.txt"
    sample1 = "Day3/sample1.txt"

    def test_sample(self):
        check(self.sample1, day3.part1, 4)

    def test_part1(self):
        run(self.problem, day3.part1)

    def test_sample2(self):
        check(self.sample1, day3.part2, '#3')

    def test_part2(self):
        run(self.problem, day3.part2)


class TestDay4:
    problem = "Day4/input.txt"
    sample1 = "Day4/sample1.txt"

    def test_sample(self):
        check(self.sample1, day4.part1, 240)

    def test_part1(self):
        run(self.problem, day4.part1)

    def test_sample2(self):
        check(self.sample1, day4.part2, 4455)

    def test_part2(self):
        run(self.problem, day4.part2)


class TestDay5:
    problem = "Day5/input.txt"
    sample1 = "Day5/sample1.txt"

    def test_sample(self):
        check(self.sample1, day5.part1, 10)

    def test_part1(self):
        run(self.problem, day5.part1)

    def test_sample2(self):
        check(self.sample1, day5.part2, 4)

    def test_part2(self):
        run(self.problem, day5.part2)


class TestDay6:
    problem = "Day6/input.txt"
    sample1 = "Day6/sample1.txt"

    def test_sample(self):
        check(self.sample1, day6.part1, 17)

    def test_part1(self):
        run(self.problem, day6.part1)

    def test_sample2(self):
        check(self.sample1, day6.part2, 16)

    def test_part2(self):
        run(self.problem, day6.part2)


class TestDay7:
    problem = "Day7/input.txt"
    sample1 = "Day7/sample1.txt"

    def test_sample(self):
        check(self.sample1, day7.part1, "CABDFE")

    def test_part1(self):
        run(self.problem, day7.part1)

    def test_sample2(self):
        check(self.sample1, day7.part2, 258)

    def test_part2(self):
        run(self.problem, day7.part2)


class TestDay8:
    problem = "Day8/input.txt"
    sample1 = "Day8/sample1.txt"

    def test_sample(self):
        check(self.sample1, day8.part1, 138)

    def test_part1(self):
        run(self.problem, day8.part1)

    def test_sample2(self):
        check(self.sample1, day8.part2, 66)

    def test_part2(self):
        run(self.problem, day8.part2)


class TestDay9:
    problem = "Day9/input.txt"
    sample1 = "Day9/sample1.txt"
    sample2 = "Day9/sample2.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 8317), (sample2, 146373)
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

    def test_sample(self):
        check(self.sample1, day10.part1, 3)

    def test_part1(self):
        run(self.problem, day10.part1)

    def test_part2(self):
        run(self.problem, day10.part2)
