from random import shuffle


def search_for_positive_numbers(array: list[int | float] | tuple[int | float]) -> list[int]:
    result = []
    for number in array[::-1]:
        if isinstance(number, (int, float)):
            if number <= 0:
                return 'Sides of a square cannot be negative'
            result.append(number ** 2)
        else:
            return 'Wrong data type, array should contain only numbers'
    return result[::-1]


def square(array: list[int | float] | tuple[int | float]) -> list[int | float]:
    try:
        if isinstance(array, (list, tuple)):
            if not array:
                return 'The array must not be empty'
            return search_for_positive_numbers(array)
        else:
            return 'Invalid data type, function accepts list or tuple'
    except Exception as error:
        # log(error)
        # send(error)
        return 'There was an unknown error and we are already working on fixing it'


if __name__ == '__main__':
    assert square((1, 2, 3)) == [1, 4, 9]
    assert square(
        'sdgdfsg') == 'Invalid data type, function accepts list or tuple'
    assert square(
        (1, 2, 3, 'a')) == 'Wrong data type, array should contain only numbers'
    assert square([]) == 'The array must not be empty'
    assert square((1, 2, -3)) == 'Sides of a square cannot be negative'


# [1,2,10,4,7,5,0,20] == [10,10,10,7,7,20]

def number_lookup_algorithm(array: list[int], k) -> int:
    return [max(array[index:index+k]) for index in range(len(array)+1-k)]


print(number_lookup_algorithm([1, 2, 10, 4, 7, 5, 0, 20], 5))


def check_monotonic_list(array: list[int]) -> bool:
    if array[0] < array[-1]:
        return array == sorted(array)
    else:
        return array == sorted(array, reverse=True)


print(check_monotonic_list([1, 1, 2, 2, 3, 3]))
print(check_monotonic_list([1, 1, 2, 4, 3, 3]))
print(check_monotonic_list([9, 8, 7, 6, 5, 4, 4, 3, 2, 1, 1, 1]))
print(check_monotonic_list([9, 8, 7, 6, 7, 4, 4, 3, 2, 1, 1, 1]))


def count_letter_in_string(s: str) -> dict:
    res = {}
    for i in s:
        res[i] = res.get(i, 0) + 1
    return res


print(count_letter_in_string('fdhetdjdgfbsfdhfgjdfgxvdfsgdtghftcvbdf'))


array = list(range(0, 31))
shuffle(array)
print('del: ', array.pop())
print('del: ', array.pop())

def find_lost_number(array: list[int]) -> int:
    deleted_numbers = []
    array.sort()
    # if array[0] != 0:
    #     return 0
    # elif array[-1] != 30:
    #     return 30
    for index in range(len(array)):
        if array[index] != array[index+1] - 1:
            deleted_numbers.append(array[index] + 1)
            array.insert(index + 1, array[index] + 1)
    return deleted_numbers

print(find_lost_number(array))


# def find_lost_number2(array: list[int]) -> int:
#     len_array = len(array)
#     array_length_before_deletion = len_array + 1
#     array_sum_before_deletion = array_length_before_deletion * (array_length_before_deletion + 1) // 2
#     return array_sum_before_deletion - sum(array)