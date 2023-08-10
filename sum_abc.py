def sum_test(a, b, c):
    result = 0
    for i in sorted([a, b, c]):
        if i < 2:
            result += i
        elif result < 2:
            result += i
        else:
            result *= i
    return result

a, b, c = map(int,input().split())
print(sum_test(a, b, c))
print(sum_test(2, 2, 2))
print(sum_test(1, 1, 2))
print(sum_test(1, 1, 3), 6)
print(sum_test(3, 1, 1), 6)
print(sum_test(1, 3, 1), 6)
print(sum_test(3, 3, 3))
print(sum_test(9, 9, 1))
print(sum_test(1, 9, 2))
