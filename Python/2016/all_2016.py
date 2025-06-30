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
        (sample1, 5), (sample2, 2), (sample3, 12)
    ])
    def test_sample(self, sample, expected):
        check(sample, day1.part1, expected)

    def test_part1(self):
        run(self.problem, day1.part1)

    def test_sample2(self):
        check(self.sample4, day1.part2, 4)

    def test_part2(self):
        run(self.problem, day1.part2)


class TestDay2:
    problem = "Day2/input.txt"
    sample1 = "Day2/sample1.txt"

    def test_sample(self):
        check(self.sample1, day2.part1, "1985")

    def test_part1(self):
        run(self.problem, day2.part1)

    def test_sample2(self):
        check(self.sample1, day2.part2, "5DB3")

    def test_part2(self):
        run(self.problem, day2.part2)


class TestDay3:
    problem = "Day3/input.txt"

    def test_part1(self):
        run(self.problem, day3.part1)

    def test_part2(self):
        run(self.problem, day3.part2)


class TestDay4:
    problem = "Day4/input.txt"
    sample1 = "Day4/sample1.txt"

    def test_sample(self):
        check(self.sample1, day4.part1, 1514)

    def test_part1(self):
        run(self.problem, day4.part1)

    def test_part2(self):
        run(self.problem, day4.part2)


class TestDay5:
    problem = "Day5/input.txt"
    sample1 = "Day5/sample1.txt"

    def test_sample(self):
        check(self.sample1, day5.part1, "18f47a30")

    def test_part1(self):
        run(self.problem, day5.part1)

    def test_sample2(self):
        check(self.sample1, day5.part2, "05ace8e3")

    def test_part2(self):
        run(self.problem, day5.part2)


class TestDay6:
    problem = "Day6/input.txt"
    sample1 = "Day6/sample1.txt"

    def test_sample(self):
        check(self.sample1, day6.part1, "easter")

    def test_part1(self):
        run(self.problem, day6.part1)

    def test_sample2(self):
        check(self.sample1, day6.part2, "advent")

    def test_part2(self):
        run(self.problem, day6.part2)


class TestDay7:
    problem = "Day7/input.txt"
    sample1 = "Day7/sample1.txt"
    sample2 = "Day7/sample2.txt"

    def test_sample(self):
        check(self.sample1, day7.part1, 2)

    def test_part1(self):
        run(self.problem, day7.part1)

    def test_sample2(self):
        check(self.sample2, day7.part2, 3)

    def test_part2(self):
        run(self.problem, day7.part2)


class TestDay8:
    problem = "Day8/input.txt"
    sample1 = "Day8/sample1.txt"

    def test_sample(self):
        check(self.sample1, day8.part1, 6)

    def test_part1(self):
        run(self.problem, day8.part1)

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
        (sample1, 6), (sample2, 7), (sample3, 9), (sample4, 11),
        (sample5, 6), (sample6, 18)
    ])
    def test_sample(self, sample, expected):
        check(sample, day9.part1, expected)

    def test_part1(self):
        run(self.problem, day9.part1)

    @pytest.mark.parametrize("sample,expected", [
        (sample3, 9), (sample6, 20), (sample7, 241920), (sample8, 445)
    ])
    def test_sample2(self, sample, expected):
        check(sample, day9.part2, expected)

    def test_part2(self):
        run(self.problem, day9.part2)


class TestDay10:
    problem = "Day10/input.txt"

    def test_part1(self):
        run(self.problem, day10.part1)

    def test_part2(self):
        run(self.problem, day10.part2)


class TestDay11:
    problem = "Day11/input.txt"

    # Never finished this one, and have no intention to do so, does not actually work
    def test_part1(self):
        run(self.problem, day11.part1)


class TestDay12:
    problem = "Day12/input.txt"
    sample1 = "Day12/sample1.txt"

    def test_sample(self):
        check(self.sample1, day12.part1, {'a': 42, 'b': 0, 'c': 0, 'd': 0})

    def test_part1(self):
        run(self.problem, day12.part1)

    def test_part2(self):
        run(self.problem, day12.part2)


class TestDay13:
    problem = "Day13/input.txt"
    sample1 = "Day13/sample1.txt"

    def test_sample(self):
        check(self.sample1, day13.part1, 11)

    def test_part1(self):
        run(self.problem, day13.part1)

    def test_part2(self):
        run(self.problem, day13.part2)


class TestDay14:
    problem = "Day14/input.txt"
    sample1 = "Day14/sample1.txt"

    def test_sample(self):
        check(self.sample1, day14.part1, 22728)

    def test_part1(self):
        run(self.problem, day14.part1)

    def test_sample2(self):
        check(self.sample1, day14.part2, 22859)

    def test_part2(self):
        run(self.problem, day14.part2)


class TestDay15:
    problem = "Day15/input.txt"
    sample1 = "Day15/sample1.txt"

    def test_sample(self):
        check(self.sample1, day15.part1, 5)

    def test_part1(self):
        run(self.problem, day15.part1)

    def test_part2(self):
        run(self.problem, day15.part2)


class TestDay16:
    problem = "Day16/input.txt"
    sample1 = "Day16/sample1.txt"
    sample2 = "Day16/sample2.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, "100"), (sample2, "01100")
    ])
    def test_sample(self, sample, expected):
        check(sample, day16.part1, expected)

    def test_part1(self):
        run(self.problem, day16.part1)

    def test_part2(self):
        run(self.problem, day16.part2)


class TestDay17:
    problem = "Day17/input.txt"
    sample1 = "Day17/sample1.txt"
    sample2 = "Day17/sample2.txt"
    sample3 = "Day17/sample3.txt"

    @pytest.mark.parametrize("sample,expected", [
        (sample1, "DDRRRD"), (sample2, "DDUDRLRRUDRD"), (sample3, "DRURDRUDDLLDLUURRDULRLDUUDDDRR")
    ])
    def test_sample(self, sample, expected):
        check(sample, day17.part1, expected)

    def test_part1(self):
        run(self.problem, day17.part1)

    @pytest.mark.parametrize("sample,expected", [
        (sample1, 370), (sample2, 492), (sample3, 830)
    ])
    def test_sample2(self, sample, expected):
        check(sample, day17.part2, expected)

    def test_part2(self):
        run(self.problem, day17.part2)


class TestDay18:
    problem = "Day18/input.txt"
    sample1 = "Day18/sample1.txt"

    def test_sample(self):
        check(self.sample1, day18.part1, 38)

    def test_part1(self):
        run(self.problem, day18.part1)

    def test_part2(self):
        run(self.problem, day18.part2)


class TestDay19:
    problem = "Day19/input.txt"
    sample1 = "Day19/sample1.txt"

    def test_sample(self):
        check(self.sample1, day19.part1, 3)

    def test_part1(self):
        run(self.problem, day19.part1)

    def test_sample2(self):
        check(self.sample1, day19.part2, 2)

    def test_part2(self):
        run(self.problem, day19.part2)


class TestDay20:
    problem = "Day20/input.txt"
    sample1 = "Day20/sample1.txt"

    def test_sample(self):
        check(self.sample1, day20.part1, 3)

    def test_part1(self):
        run(self.problem, day20.part1)

    def test_part2(self):
        run(self.problem, day20.part2)


class TestDay21:
    problem = "Day21/input.txt"
    sample1 = "Day21/sample1.txt"

    def test_sample(self):
        check(self.sample1, day21.part1, "decab")

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
        check(self.sample1, day23.part1, {'a': 3, 'b': 0, 'c': 0, 'd': 0})

    def test_part1(self):
        run(self.problem, day23.part1)

    def test_part2(self):
        run(self.problem, day23.part2)


class TestDay24:
    problem = "Day24/input.txt"
    sample1 = "Day24/sample1.txt"

    def test_sample(self):
        check(self.sample1, day24.part1, 14)

    def test_part1(self):
        run(self.problem, day24.part1)

    def test_part2(self):
        run(self.problem, day24.part2)


class TestDay25:
    problem = "Day25/input.txt"

    def test_part1(self):
        run(self.problem, day25.part1)
