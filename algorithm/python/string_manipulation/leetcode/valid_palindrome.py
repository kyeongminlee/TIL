# https://leetcode.com/problems/valid-palindrome
import collections
import re


class Solution:

    # def isPalindrome(self, s: str) -> bool:
    #     only_alnums = []
    #     for char in s:
    #         if char.isalnum():
    #             only_alnums.append(char.lower())
    #
    #     while len(only_alnums) > 1:
    #         if only_alnums.pop(0) != only_alnums.pop():
    #             return False
    #
    #     return True

    # def isPalindrome(self, s: str) -> bool:
    #     # 자료형 데크로 선언
    #     only_alnums: Deque = collections.deque()
    #
    #     for char in s:
    #         if char.isalnum():
    #             only_alnums.append(char.lower())
    #
    #     while len(only_alnums) > 1:
    #         if only_alnums.popleft() != only_alnums.pop():
    #             return False
    #
    #     return True

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]