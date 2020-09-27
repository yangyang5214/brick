def reverse(x):
    if x == 0:
        return x
    stack = []
    s = str(x)
    for i in s:
        stack.append(i)

    if stack[-1] == '0':
        stack.pop()

    if stack[0] == '-':
        result = int('-' + ''.join(stack[:0:-1]))
    else:
        result = int(''.join(stack[::-1]))

    if result > pow(2, 31) or result < pow(-2, 31):
        return 0
    return result


if __name__ == '__main__':
    print(reverse(-123))
    print(reverse(120))
    print(reverse(123))
