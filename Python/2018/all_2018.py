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


class TestDay11:
    problem = "Day11/input.txt"
    sample1 = "Day11/sample1.txt"

    def test_sample(self):
        check(self.sample1, day11.part1, "21,61")

    def test_part1(self):
        run(self.problem, day11.part1)

    def test_sample2(self):
        check(self.sample1, day11.part2, "232,251,12")

    def test_part2(self):
        run(self.problem, day11.part2)


class TestDay12:
    problem = "Day12/input.txt"
    sample1 = "Day12/sample1.txt"

    def test_sample(self):
        check(self.sample1, day12.part1, 325)

    def test_part1(self):
        run(self.problem, day12.part1)

    def test_part2(self):
        run(self.problem, day12.part2)


class TestDay13:
    problem = "Day13/input.txt"
    sample1 = "Day13/sample1.txt"

    def test_sample(self):
        check(self.sample1, day13.part1, "7,3", strip_file=False)

    def test_part1(self):
        run(self.problem, day13.part1, strip_file=False)

    def test_part2(self):
        run(self.problem, day13.part2, strip_file=False)


class TestDay14:
    problem = "Day14/input.txt"
    sample1 = "Day14/sample1.txt"

    def test_sample(self):
        check(self.sample1, day14.part1, "5941429882")

    def test_part1(self):
        run(self.problem, day14.part1)

    def test_sample2(self):
        check(self.sample1, day14.part2, 86764)

    def test_part2(self):
        run(self.problem, day14.part2)


class TestDay15:
    problem = "Day15/input.txt"
    sample1 = "Day15/sample1.txt"

    def test_sample(self):
        check(self.sample1, day15.part1, 18740)

    def test_part1(self):
        run(self.problem, day15.part1)

    def test_part2(self):
        run(self.problem, day15.part2)


class TestDay16:
    problem = "Day16/input.txt"
    sample1 = "Day16/sample1.txt"

    def test_sample(self):
        check(self.sample1, day16.part1, 1)

    def test_part1(self):
        run(self.problem, day16.part1)

    def test_part2(self):
        run(self.problem, day16.part2)


class TestDay17:
    problem = "Day17/input.txt"
    sample1 = "Day17/sample1.txt"

    def test_sample(self):
        check(self.sample1, day17.part1, 57)

    def test_part1(self):
        run(self.problem, day17.part1)

    def test_part2(self):
        run(self.problem, day17.part2)


class TestDay18:
    problem = "Day18/input.txt"
    sample1 = "Day18/sample1.txt"

    def test_sample(self):
        check(self.sample1, day18.part1, 1147)

    def test_part1(self):
        run(self.problem, day18.part1)

    def test_part2(self):
        run(self.problem, day18.part2)


class TestDay19:
    problem = "Day19/input.txt"
    sample1 = "Day19/sample1.txt"

    def test_sample(self):
        check(self.sample1, day19.part1, 7)

    def test_part1(self):
        run(self.problem, day19.part1)

    def test_part2(self):
        run(self.problem, day19.part2)


class TestDay20:
    problem = "Day20/input.txt"
    sample1 = "Day20/sample1.txt"
    sample2 = "Day20/sample2.txt"
    sample3 = "Day20/sample3.txt"

    @pytest.mark.parametrize("sample,expected", {
        (sample1, 31), (sample2, 23), (sample3, 18)
    })
    def test_sample(self, sample, expected):
        check(sample, day20.part1, expected)

    def test_part1(self):
        run(self.problem, day20.part1)

    @pytest.mark.parametrize("sample,expected", {
        (sample1, 39), (sample2, 25), (sample3, 13)
    })
    def test_sample(self, sample, expected):
        check(sample, day20.part2, expected)

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
    sample1 = "Day22/sample1.txt"

    def test_sample(self):
        check(self.sample1, day22.part1, 114)

    def test_part1(self):
        run(self.problem, day22.part1)

    def test_sample2(self):
        check(self.sample1, day22.part2, 45)

    def test_part2(self):
        run(self.problem, day22.part2)


class TestDay23:
    problem = "Day23/input.txt"
    sample1 = "Day23/sample1.txt"
    sample2 = "Day23/sample2.txt"

    def test_sample(self):
        check(self.sample1, day23.part1, 7)

    def test_part1(self):
        run(self.problem, day23.part1)

    def test_sample2(self):
        check(self.sample2, day23.part2, 36)

    def test_part2(self):
        run(self.problem, day23.part2)


class TestDay24:
    problem = "Day24/input.txt"
    sample1 = "Day24/sample1.txt"

    def test_sample(self):
        check(self.sample1, day24.part1, 5216)

    def test_part1(self):
        run(self.problem, day24.part1)

    def test_sample2(self):
        check(self.sample1, day24.part2, 51)

    def test_part2(self):
        run(self.problem, day24.part2)


class TestDay25:
    problem = "Day25/input.txt"
    sample1 = "Day25/sample1.txt"
    sample2 = "Day25/sample2.txt"
    sample3 = "Day25/sample3.txt"

    @pytest.mark.parametrize("sample,expected", {
        (sample1, 4), (sample2, 3), (sample3, 8)
    })
    def test_sample(self, sample, expected):
        check(sample, day25.part1, expected)

    def test_part1(self):
        run(self.problem, day25.part1)
