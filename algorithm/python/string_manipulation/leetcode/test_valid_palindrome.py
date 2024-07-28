import pytest
from valid_palindrome import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_a(solution):
    assert solution.isPalindrome("A man, a plan, a canal, Panama") == True

def test_example_b(solution):
    assert solution.isPalindrome("race a car") == False

def test_example_c(solution):
    assert solution.isPalindrome(" ") == True
