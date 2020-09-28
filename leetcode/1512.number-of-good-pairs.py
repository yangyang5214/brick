from typing import List


def num_identical_pairs1(nums: List[int]) -> int:
    result = 0
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] == nums[j] and i < j:
                result = result + 1
    return result


def num_identical_pairs(nums: List[int]) -> int:
    hash_map = {}
    result = 0
    for i in range(len(nums)):
        if not hash_map.get(nums[i]):
            hash_map[nums[i]] = 1
        else:
            v = hash_map.get(nums[i])
            hash_map[nums[i]] = v + 1
            result = result + v
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 1, 3]
    # nums = [1, 1, 1, 1]
    # nums = [1, 2, 3]
    print(num_identical_pairs(nums))
