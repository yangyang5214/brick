from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    max = candies[0]
    for i in range(1, len(candies)):
        if candies[i] > max:
            max = candies[i]
    result = []
    for i in range(len(candies)):
        if candies[i] + extraCandies < max:
            result.append(False)
        else:
            result.append(True)
    return result


if __name__ == '__main__':
    # candies = [2, 3, 5, 1, 3]
    # extraCandies = 3

    # candies = [4,2,1,1,2]
    # extraCandies = 1

    candies = [12, 1, 12]
    extraCandies = 10

    print(kidsWithCandies(candies, extraCandies))
