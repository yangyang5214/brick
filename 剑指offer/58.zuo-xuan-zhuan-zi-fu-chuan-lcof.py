def reverse_left_words(s: str, n: int) -> str:
    return s[n:] + s[0:n]


if __name__ == '__main__':
    s = 'abcdefg'
    n = 2
    print(reverse_left_words(s, n))
