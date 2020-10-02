# -*- coding: utf-8 -*-
from typing import List


def longestCommonPrefix1(strs: List[str]) -> str:
    if not strs:
        return ''
    flag = 0
    while True:
        temp = strs[0][flag:flag + 1]
        for i in range(1, len(strs)):
            if strs[i][flag:flag + 1] != temp:
                if flag == 0:
                    return ''
                else:
                    return strs[i][0:flag]
        flag = flag + 1


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    s1 = min(strs)
    s2 = max(strs)
    for i, x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1


if __name__ == '__main__':
    lis = ["flower", "flow", "flight"]
    # lis = ["dog", "racecar", "car"]
    print(longestCommonPrefix(lis))
