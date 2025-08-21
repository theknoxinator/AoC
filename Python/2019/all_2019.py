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


class TestDay1:
    problem = "Day1/input.txt"
    sample1 = "Day1/sample1.txt"

    def test_sample(self):
        check(self.sample1, day1.part1, 34241)

    def test_part1(self):
        run(self.problem, day1.part1)

    def test_sample2(self):
        check(self.sample1, day1.part2, 51316)

    def test_part2(self):
        run(self.problem, day1.part2)


class TestDay2:
    problem = "Day2/input.txt"
    sample1 = "Day2/sample1.txt"

    def test_sample(self):
        check(self.sample1, day2.part1, 30)

    def test_part1(self):
        run(self.problem, day2.part1)

    def test_part2(self):
        run(self.problem, day2.part2)


class TestDay3:
    problem = "Day3/input.txt"
    sample1 = "Day3/sample1.txt"

    def test_sample(self):
        check(self.sample1, day3.part1, 135)

    def test_part1(self):
        run(self.problem, day3.part1)

    def test_sample2(self):
        check(self.sample1, day3.part2, 410)

    def test_part2(self):
        run(self.problem, day3.part2)


class TestDay4:
    problem = "Day4/input.txt"
    sample1 = "Day4/sample1.txt"
    sample2 = "Day4/sample2.txt"

    def test_sample(self):
        check(self.sample1, day4.part1, 1)

    def test_part1(self):
        run(self.problem, day4.part1)

    def test_sample2(self):
        check(self.sample2, day4.part2, 2)

    def test_part2(self):
        run(self.problem, day4.part2)


class TestDay5:
    problem = "Day5/input.txt"
    sample1 = "Day5/sample1.txt"
    sample2 = "Day5/sample2.txt"

    def test_sample(self):
        check(self.sample1, day5.part1, "1")

    def test_part1(self):
        run(self.problem, day5.part1)

    def test_sample2(self):
        check(self.sample2, day5.part2, "999")

    def test_part2(self):
        run(self.problem, day5.part2)


class TestDay6:
    problem = "Day6/input.txt"
    sample1 = "Day6/sample1.txt"
    sample2 = "Day6/sample2.txt"

    def test_sample(self):
        check(self.sample1, day6.part1, 42)

    def test_part1(self):
        run(self.problem, day6.part1)

    def test_sample2(self):
        check(self.sample2, day6.part2, 4)

    def test_part2(self):
        run(self.problem, day6.part2)


class TestDay7:
    problem = "Day7/input.txt"
    sample1 = "Day7/sample1.txt"
    sample2 = "Day7/sample2.txt"

    def test_sample(self):
        check(self.sample1, day7.part1, 65210)

    def test_part1(self):
        run(self.problem, day7.part1)

    def test_sample2(self):
        check(self.sample2, day7.part2, 139629729)

    def test_part2(self):
        run(self.problem, day7.part2)


class TestDay8:
    problem = "Day8/input.txt"
    sample1 = "Day8/sample1.txt"

    def test_sample(self):
        check(self.sample1, day8.part1, 1)

    def test_part1(self):
        run(self.problem, day8.part1)

    def test_part2(self):
        run(self.problem, day8.part2)


class TestDay9:
    problem = "Day9/input.txt"
    sample1 = "Day9/sample1.txt"

    def test_sample(self):
        check(self.sample1, day9.part1, "1219070632396864")

    def test_part1(self):
        run(self.problem, day9.part1)

    def test_part2(self):
        run(self.problem, day9.part2)


class TestDay10:
    problem = "Day10/input.txt"
    sample1 = "Day10/sample1.txt"
    sample2 = "Day10/sample2.txt"
    sample3 = "Day10/sample3.txt"
    sample4 = "Day10/sample4.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 33), (sample2, 35), (sample3, 41), (sample4, 210)
    ])
    def test_sample(self, sample, expected):
        check(sample, day10.part1, expected)

    def test_part1(self):
        run(self.problem, day10.part1)

    def test_sample2(self):
        check(self.sample4, day10.part2, 802)

    def test_part2(self):
        run(self.problem, day10.part2)


class TestDay11:
    problem = "Day11/input.txt"

    def test_part1(self):
        run(self.problem, day11.part1)

    def test_part2(self):
        run(self.problem, day11.part2)


class TestDay12:
    problem = "Day12/input.txt"
    sample1 = "Day12/sample1.txt"

    def test_sample(self):
        check(self.sample1, day12.part1, 1940)

    def test_part1(self):
        run(self.problem, day12.part1)

    def test_sample2(self):
        check(self.sample1, day12.part2, 4686774924)

    def test_part2(self):
        run(self.problem, day12.part2)


class TestDay13:
    problem = "Day13/input.txt"

    def test_part1(self):
        run(self.problem, day13.part1)

    def test_part2(self):
        run(self.problem, day13.part2)


class TestDay14:
    problem = "Day14/input.txt"
    sample1 = "Day14/sample1.txt"
    sample2 = "Day14/sample2.txt"
    sample3 = "Day14/sample3.txt"

    @pytest.mark.parametrize("sample,expected", {
        (sample1, 13312), (sample2, 180697), (sample3, 2210736)
    })
    def test_sample(self, sample, expected):
        check(sample, day14.part1, expected)

    def test_part1(self):
        run(self.problem, day14.part1)

    @pytest.mark.parametrize("sample,expected", {
        (sample1, 82892753), (sample2, 5586022), (sample3, 460664)
    })
    def test_sample2(self, sample, expected):
        check(sample, day14.part2, expected)

    def test_part2(self):
        run(self.problem, day14.part2)


class TestDay15:
    problem = "Day15/input.txt"

    def test_part1(self):
        run(self.problem, day15.part1)

    def test_part2(self):
        run(self.problem, day15.part2)


class TestDay16:
    problem = "Day16/input.txt"
    sample1 = "Day16/sample1.txt"
    sample2 = "Day16/sample2.txt"
    sample3 = "Day16/sample3.txt"
    sample4 = "Day16/sample4.txt"

    @pytest.mark.parametrize("sample,expected", {
        (sample1, '24176176'), (sample2, '73745418'), (sample3, '52432133')
    })
    def test_sample(self, sample, expected):
        check(sample, day16.part1, expected)

    def test_part1(self):
        run(self.problem, day16.part1)

    def test_sample2(self):
        check(self.sample4, day16.part2, '84462026')

    def test_part2(self):
        run(self.problem, day16.part2)
