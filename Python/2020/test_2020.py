import pytest
from common import *
import day1


skip_completed = pytest.mark.skipif(True, reason="Day completed")


@skip_completed
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
