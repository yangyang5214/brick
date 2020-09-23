from typing import List


def running_sum(nums: List[int]) -> List[int]:
    if len(nums) < 1:
        return nums
    results = [nums[0]]
    for i in range(1, len(nums)):
        results.append(results[i - 1] + nums[i])
    return results


if __name__ == '__main__':
    # nums = [1, 2, 3, 4]
    # nums = [1,1,1,1,1]
    nums = [3, 1, 2, 10, 1]
    print(running_sum(nums))
