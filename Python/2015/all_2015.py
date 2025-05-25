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

skip_completed = pytest.mark.skipif(True, reason="Day completed")


@skip_completed
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


@skip_completed
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


@skip_completed
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


@skip_completed
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


@skip_completed
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


@skip_completed
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


@skip_completed
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


@skip_completed
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


@skip_completed
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
