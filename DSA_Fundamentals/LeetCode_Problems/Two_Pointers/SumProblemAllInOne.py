"""
# k-Sum Reference: Two Sum (sorted) -> 3Sum -> 4Sum -> general kSum
LeetCode 15 (3Sum), 18 (4Sum)

1. EXPLANATION (plain words)
   Find all unique groups of k numbers that add up to target.
   Brute force checks every group: O(n^k). Too slow.
   Trick: sort once, fix the first (k-2) numbers with loops,
   then find the last two with two pointers (l from the left, r from the right).
   Sorting also puts equal numbers side by side, so duplicates are easy to skip.

2. MATHEMATICS
   After sorting, look only at index order i < j < l < r, so a <= b <= c <= d.
   Each distinct sorted tuple is then produced exactly once.
   For fixed i, j: need = target - nums[i] - nums[j], and we want nums[l] + nums[r] = need.
     s < target  -> every r' <= r is also too small for this l, so l += 1 is safe.
     s > target  -> every l' >= l is also too large for this r, so r -= 1 is safe.
     s == target -> save it, move both pointers.
   Duplicate rule: if a value equals the value just before it at the same level, skip it.

3. TIME COMPLEXITY
   Sort:  O(n log n)
   2Sum (sorted): O(n)        3Sum: O(n^2)        4Sum: O(n^3)        kSum: O(n^(k-1))
   Extra space: O(1) besides the output (and the sort).

4. PROCEDURE
   1) Sort nums.
   2) Loop i (skip if nums[i] == nums[i-1]); for 4Sum also loop j (skip if j > i+1 and
      nums[j] == nums[j-1]).
   3) Set l = next index, r = n - 1.
   4) While l < r: compute s.
        equal   -> save, l += 1, r -= 1, skip equal values on both sides
        s < target -> l += 1
        s > target -> r -= 1

5. TRACE (3Sum, nums = [-1, 0, 1, 2, -1, -4], target = 0)
   sorted = [-4, -1, -1, 0, 1, 2]
   i=0 (-4): l=1 r=5 -> -4-1+2 = -3  < 0 -> l=2
             l=2 r=5 -> -4-1+2 = -3  < 0 -> l=3
             l=3 r=5 -> -4+0+2 = -2  < 0 -> l=4
             l=4 r=5 -> -4+1+2 = -1  < 0 -> l=5, loop ends
   i=1 (-1): l=2 r=5 -> -1-1+2 = 0   save [-1,-1,2]; l=3 r=4
             l=3 r=4 -> -1+0+1 = 0   save [-1,0,1];  l=4 r=3, loop ends
   i=2 (-1): same as nums[1], skipped
   i=3 (0):  l=4 r=5 -> 0+1+2 = 3 > 0 -> r=4, loop ends
   Result: [[-1,-1,2], [-1,0,1]]
"""


def two_sum_sorted(nums, target, start=0):
    """All unique pairs in nums[start:] (already sorted) that add up to target."""
    res = []
    l, r = start, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            res.append([nums[l], nums[r]])
            l += 1
            r -= 1
            while l < r and nums[l] == nums[l - 1]:
                l += 1
            while l < r and nums[r] == nums[r + 1]:
                r -= 1
        elif s < target:
            l += 1
        else:
            r -= 1
    return res


def three_sum(nums, target=0):
    nums = sorted(nums)
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for pair in two_sum_sorted(nums, target - nums[i], i + 1):
            res.append([nums[i]] + pair)
    return res


def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            l, r = j + 1, n - 1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
    return res


def k_sum(nums, target, k):
    """General version: recursion fixes one number per level until k == 2."""
    nums = sorted(nums)

    def helper(start, k, target):
        if len(nums) - start < k:
            return []
        if k == 2:
            return two_sum_sorted(nums, target, start)
        res = []
        for i in range(start, len(nums) - k + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            for rest in helper(i + 1, k - 1, target - nums[i]):
                res.append([nums[i]] + rest)
        return res

    return helper(0, k, target)


if __name__ == "__main__":
    import itertools
    import random

    assert four_sum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert four_sum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

    for _ in range(2000):
        a = [random.randint(-5, 5) for _ in range(random.randint(1, 9))]
        t = random.randint(-8, 8)
        for k, fn in ((3, lambda x, y: three_sum(x, y)), (4, lambda x, y: four_sum(x[:], y)),
                      (2, lambda x, y: k_sum(x, y, 2)), (4, lambda x, y: k_sum(x, y, 4))):
            expected = sorted({tuple(sorted(c)) for c in itertools.combinations(a, k) if sum(c) == t})
            assert expected == sorted(tuple(x) for x in fn(a, t)), (a, t, k)
    print("all checks passed")