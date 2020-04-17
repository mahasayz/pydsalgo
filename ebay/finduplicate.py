from typing import List


def findDuplicate(nums: List[int]) -> int:
    sum = 0
    for num in nums:
        sum += num

    n = len(nums)
    expected_sum = n * (n + 1) / 2

    return expected_sum-sum


if __name__=="__main__":
    print(findDuplicate([1, 2, 3, 4, 5, 6, 7, 1]))