import pytest
from common import *
import day1
import day2


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


class TestDay2:
    problem = "Day2/input.txt"
    sample1 = "day2/sample1.txt"

    def test_sample(self):
        check(self.sample1, day2.part1, 150)

    def test_part1(self):
        run(self.problem, day2.part1)

    def test_sample2(self):
        check(self.sample1, day2.part2, 900)

    def test_part2(self):
        run(self.problem, day2.part2)
