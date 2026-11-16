# Letter Combinations of a Phone Number 

from unittest import result


class Solution:

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        path = []

        def backTrack(index : int) -> None:
            if index == len(digits):
                result.append("".join(path))
                return

            letters = phone_map[digits[index]]
            for letter in letters:
                path.append(letter)
                backTrack(index + 1)
                path.pop()

        backTrack(0)
        return result

obj = Solution()
print(obj.letterCombinations("23"))
print(obj.letterCombinations("23456789"))