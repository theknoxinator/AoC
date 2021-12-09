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


skip_completed = pytest.mark.skipif(True, reason="Day completed")


@skip_completed
class TestDay1:
    problem = "Day1/input.txt"
    sample1 = "Day1/sample1.txt"

    def test_sample(self):
        check(self.sample1, day1.part1, 7)

    def test_part1(self):
        run(self.problem, day1.part1)

    def test_sample2(self):
        check(self.sample1, day1.part2, 5)

    def test_part2(self):
        run(self.problem, day1.part2)


@skip_completed
class TestDay2:
    problem = "Day2/input.txt"
    sample1 = "Day2/sample1.txt"

    def test_sample(self):
        check(self.sample1, day2.part1, 150)

    def test_part1(self):
        run(self.problem, day2.part1)

    def test_sample2(self):
        check(self.sample1, day2.part2, 900)

    def test_part2(self):
        run(self.problem, day2.part2)


@skip_completed
class TestDay3:
    problem = "Day3/input.txt"
    sample1 = "Day3/sample1.txt"

    def test_sample(self):
        check(self.sample1, day3.part1, 198)

    def test_part1(self):
        run(self.problem, day3.part1)

    def test_sample2(self):
        check(self.sample1, day3.part2, 230)

    def test_part2(self):
        run(self.problem, day3.part2)


@skip_completed
class TestDay4:
    problem = "Day4/input.txt"
    sample1 = "Day4/sample1.txt"

    def test_sample(self):
        check(self.sample1, day4.part1, 4512)

    def test_part1(self):
        run(self.problem, day4.part1)

    def test_sample2(self):
        check(self.sample1, day4.part2, 1924)

    def test_part2(self):
        run(self.problem, day4.part2)


@skip_completed
class TestDay5:
    problem = "Day5/input.txt"
    sample1 = "Day5/sample1.txt"

    def test_sample(self):
        check(self.sample1, day5.part1, 5)

    def test_part1(self):
        run(self.problem, day5.part1)

    def test_sample2(self):
        check(self.sample1, day5.part2, 12)

    def test_part2(self):
        run(self.problem, day5.part2)


@skip_completed
class TestDay6:
    problem = "Day6/input.txt"
    sample1 = "Day6/sample1.txt"

    def test_sample(self):
        check(self.sample1, day6.part1, 5934)

    def test_part1(self):
        run(self.problem, day6.part1)

    def test_sample2(self):
        check(self.sample1, day6.part2, 26984457539)

    def test_part2(self):
        run(self.problem, day6.part2)


@skip_completed
class TestDay7:
    problem = "Day7/input.txt"
    sample1 = "Day7/sample1.txt"

    def test_sample(self):
        check(self.sample1, day7.part1, 37)

    def test_part1(self):
        run(self.problem, day7.part1)

    def test_sample2(self):
        check(self.sample1, day7.part2, 168)

    def test_part2(self):
        run(self.problem, day7.part2)


class TestDay8:
    problem = "Day8/input.txt"
    sample1 = "Day8/sample1.txt"

    def test_sample(self):
        check(self.sample1, day8.part1, 26)

    def test_part1(self):
        run(self.problem, day8.part1)

    def test_sample2(self):
        check(self.sample1, day8.part2, 61229)

    def test_part2(self):
        run(self.problem, day8.part2)
