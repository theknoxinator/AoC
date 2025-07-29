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

    def test_sample2(self):
        check(self.sample1, day13.part2, 10)

    def test_part2(self):
        run(self.problem, day13.part2)


class TestDay14:
    problem = "Day14/input.txt"
    sample1 = "Day14/sample1.txt"

    def test_sample(self):
        check(self.sample1, day14.part1, 8108)

    def test_part1(self):
        run(self.problem, day14.part1)

    def test_sample2(self):
        check(self.sample1, day14.part2, 1242)

    def test_part2(self):
        run(self.problem, day14.part2)


class TestDay15:
    problem = "Day15/input.txt"
    sample1 = "Day15/sample1.txt"

    def test_sample(self):
        check(self.sample1, day15.part1, 588)

    def test_part1(self):
        run(self.problem, day15.part1)

    def test_sample2(self):
        check(self.sample1, day15.part2, 309)

    def test_part2(self):
        run(self.problem, day15.part2)


class TestDay16:
    problem = "Day16/input.txt"
    sample1 = "Day16/sample1.txt"

    def test_sample(self):
        check(self.sample1, day16.part1, "baedc")

    def test_part1(self):
        run(self.problem, day16.part1)

    def test_part2(self):
        run(self.problem, day16.part2)


class TestDay17:
    problem = "Day17/input.txt"
    sample1 = "Day17/sample1.txt"

    def test_sample(self):
        check(self.sample1, day17.part1, 638)

    def test_part1(self):
        run(self.problem, day17.part1)

    def test_sample2(self):
        check(self.sample1, day17.part2, 1222153)

    def test_part2(self):
        run(self.problem, day17.part2)


class TestDay18:
    problem = "Day18/input.txt"
    sample1 = "Day18/sample1.txt"
    sample2 = "Day18/sample2.txt"

    def test_sample(self):
        check(self.sample1, day18.part1, 4)

    def test_part1(self):
        run(self.problem, day18.part1)

    def test_sample2(self):
        check(self.sample2, day18.part2, 3)

    def test_part2(self):
        run(self.problem, day18.part2)


class TestDay19:
    problem = "Day19/input.txt"
    sample1 = "Day19/sample1.txt"

    def test_sample(self):
        check(self.sample1, day19.part1, "ABCDEF", strip_file=False)

    def test_part1(self):
        run(self.problem, day19.part1, strip_file=False)

    def test_sample2(self):
        check(self.sample1, day19.part2, 38, strip_file=False)

    def test_part2(self):
        run(self.problem, day19.part2, strip_file=False)


class TestDay20:
    problem = "Day20/input.txt"
    sample1 = "Day20/sample1.txt"
    sample2 = "Day20/sample2.txt"

    def test_sample(self):
        check(self.sample1, day20.part1, 0)

    def test_part1(self):
        run(self.problem, day20.part1)

    def test_sample2(self):
        check(self.sample2, day20.part2, 1)

    def test_part2(self):
        run(self.problem, day20.part2)


class TestDay21:
    problem = "Day21/input.txt"
    sample1 = "Day21/sample1.txt"

    def test_sample(self):
        check(self.sample1, day21.part1, 12)

    def test_part1(self):
        run(self.problem, day21.part1)

    def test_part2(self):
        run(self.problem, day21.part2)


class TestDay22:
    problem = "Day22/input.txt"
    sample1 = "Day22/sample1.txt"

    def test_sample(self):
        check(self.sample1, day22.part1, 5587)

    def test_part1(self):
        run(self.problem, day22.part1)

    def test_sample2(self):
        check(self.sample1, day22.part2, 2511944)

    def test_part2(self):
        run(self.problem, day22.part2)


class TestDay23:
    problem = "Day23/input.txt"
    problem2 = "Day23/modified_input.txt"

    def test_part1(self):
        run(self.problem, day23.part1)

    def test_part2(self):
        run(self.problem2, day23.part2)


class TestDay24:
    problem = "Day24/input.txt"
    sample1 = "Day24/sample1.txt"

    def test_sample(self):
        check(self.sample1, day24.part1, 31)

    def test_part1(self):
        run(self.problem, day24.part1)

    def test_sample2(self):
        check(self.sample1, day24.part2, 19)

    def test_part2(self):
        run(self.problem, day24.part2)


class TestDay25:
    problem = "Day25/input.txt"
    sample1 = "Day25/sample1.txt"

    def test_sample(self):
        check(self.sample1, day25.part1, 3)

    def test_part1(self):
        run(self.problem, day25.part1)
