from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    list = []
    for i in range(n):
        list.append(nums[i])
        list.append(nums[i + n])
    return list


if __name__ == '__main__':
    # nums = [2, 5, 1, 3, 4, 7]
    # n = 3

    # nums = [1,2,3,4,4,3,2,1]
    # n = 4

    nums = [1,1,2,2]
    n = 2
    print(shuffle(nums, n))
