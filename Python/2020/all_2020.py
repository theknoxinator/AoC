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


class TestDay1:
    problem = "Day1/input.txt"
    sample1 = "Day1/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day1.part1, 514579)

    def test_part1(self):
        run(self.problem, day1.part1)

    def test_sample2(self):
        check(self.sample1, day1.part2, 241861950)

    def test_part2(self):
        run(self.problem, day1.part2)


class TestDay2:
    problem = "Day2/input.txt"
    sample1 = "Day2/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day2.part1, 2)

    def test_part1(self):
        run(self.problem, day2.part1)

    def test_sample2(self):
        check(self.sample1, day2.part2, 1)

    def test_part2(self):
        run(self.problem, day2.part2)


class TestDay3:
    problem = "Day3/input.txt"
    sample1 = "Day3/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day3.part1, 7)

    def test_part1(self):
        run(self.problem, day3.part1)

    def test_sample2(self):
        check(self.sample1, day3.part2, 336)

    def test_part2(self):
        run(self.problem, day3.part2)


class TestDay4:
    problem = "Day4/input.txt"
    sample1 = "Day4/sample1.txt"
    sample2 = "Day4/sample2.txt"

    def test_sample1(self):
        check(self.sample1, day4.part1, 2)

    def test_part1(self):
        run(self.problem, day4.part1)

    def test_sample2(self):
        check(self.sample2, day4.part2, 4)

    def test_part2(self):
        run(self.problem, day4.part2)


class TestDay5:
    problem = "Day5/input.txt"
    sample1 = "Day5/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day5.part1, 820)

    def test_part1(self):
        run(self.problem, day5.part1)

    def test_part2(self):
        run(self.problem, day5.part2)


class TestDay6:
    problem = "Day6/input.txt"
    sample1 = "Day6/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day6.part1, 11)

    def test_part1(self):
        run(self.problem, day6.part1)

    def test_sample2(self):
        check(self.sample1, day6.part2, 6)

    def test_part2(self):
        run(self.problem, day6.part2)


class TestDay7:
    problem = "Day7/input.txt"
    sample1 = "Day7/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day7.part1, 4)

    def test_part1(self):
        run(self.problem, day7.part1)

    def test_sample2(self):
        check(self.sample1, day7.part2, 32)

    def test_part2(self):
        run(self.problem, day7.part2)


class TestDay8:
    problem = "Day8/input.txt"
    sample1 = "Day8/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day8.part1, 5)

    def test_part1(self):
        run(self.problem, day8.part1)

    def test_sample2(self):
        check(self.sample1, day8.part2, 8)

    def test_part2(self):
        run(self.problem, day8.part2)


class TestDay9:
    problem = "Day9/input.txt"
    sample1 = "Day9/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day9.part1, 127)

    def test_part1(self):
        run(self.problem, day9.part1)

    def test_sample2(self):
        check(self.sample1, day9.part2, 62)

    def test_part2(self):
        run(self.problem, day9.part2)


class TestDay10:
    problem = "Day10/input.txt"
    sample1 = "Day10/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day10.part1, 220)

    def test_part1(self):
        run(self.problem, day10.part1)

    def test_sample2(self):
        check(self.sample1, day10.part2, 19208)

    def test_part2(self):
        run(self.problem, day10.part2)


class TestDay11:
    problem = "Day11/input.txt"
    sample1 = "Day11/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day11.part1, 37)

    def test_part1(self):
        run(self.problem, day11.part1)

    def test_sample2(self):
        check(self.sample1, day11.part2, 26)

    def test_part2(self):
        run(self.problem, day11.part2)


class TestDay12:
    problem = "Day12/input.txt"
    sample1 = "Day12/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day12.part1, 25)

    def test_part1(self):
        run(self.problem, day12.part1)

    def test_sample2(self):
        check(self.sample1, day12.part2, 286)

    def test_part2(self):
        run(self.problem, day12.part2)


class TestDay13:
    problem = "Day13/input.txt"
    sample1 = "Day13/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day13.part1, 295)

    def test_part1(self):
        run(self.problem, day13.part1)

    def test_sample2(self):
        check(self.sample1, day13.part2, 1068781)

    def test_part2(self):
        run(self.problem, day13.part2)


class TestDay14:
    problem = "Day14/input.txt"
    sample1 = "Day14/sample1.txt"
    sample2 = "Day14/sample2.txt"

    def test_sample1(self):
        check(self.sample1, day14.part1, 165)

    def test_part1(self):
        run(self.problem, day14.part1)

    def test_sample2(self):
        check(self.sample2, day14.part2, 208)

    def test_part2(self):
        run(self.problem, day14.part2)


class TestDay15:
    problem = "Day15/input.txt"
    sample1 = "Day15/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day15.part1, "1836")

    def test_part1(self):
        run(self.problem, day15.part1)

    def test_sample2(self):
        check(self.sample1, day15.part2, "362")

    def test_part2(self):
        run(self.problem, day15.part2)


class TestDay16:
    problem = "Day16/input.txt"
    sample1 = "Day16/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day16.part1, 71)

    def test_part1(self):
        run(self.problem, day16.part1)

    def test_part2(self):
        run(self.problem, day16.part2)


class TestDay17:
    problem = "Day17/input.txt"
    sample1 = "Day17/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day17.part1, 112)

    def test_part1(self):
        run(self.problem, day17.part1)

    def test_sample2(self):
        check(self.sample1, day17.part2, 848)

    def test_part2(self):
        run(self.problem, day17.part2)


class TestDay18:
    problem = "Day18/input.txt"
    sample1 = "Day18/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day18.part1, 26457)

    def test_part1(self):
        run(self.problem, day18.part1)

    def test_sample2(self):
        check(self.sample1, day18.part2, 694173)

    def test_part2(self):
        run(self.problem, day18.part2)


class TestDay19:
    problem = "Day19/input.txt"
    sample1 = "Day19/sample1.txt"
    sample2 = "Day19/sample2.txt"

    def test_sample1(self):
        check(self.sample1, day19.part1, 2)

    def test_part1(self):
        run(self.problem, day19.part1)

    def test_sample2(self):
        check(self.sample2, day19.part2, 12)

    def test_part2(self):
        run(self.problem, day19.part2)


class TestDay20:
    problem = "Day20/input.txt"
    sample1 = "Day20/sample1.txt"

    def test_sample1(self):
        check(self.sample1, day20.part1, 20899048083289)

    def test_part1(self):
        run(self.problem, day20.part1)

    # def test_sample2(self):
    #     check(self.sample1, day20.part2, 273)
    #
    # def test_part2(self):
    #     run(self.problem, day20.part2)
