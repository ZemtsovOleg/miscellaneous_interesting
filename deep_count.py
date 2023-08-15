#  на выходе мы получаем плоский упорядоченый список
def flatten(a):
    queue, out = [a], []
    while queue:
        elem = queue.pop()
        if isinstance(elem, list):
            queue.extend(elem)
        else:
            out.append(elem)
    return out[::-1]


print(flatten([1, "abc", [[100, 200], 10, 20], [30, 40]]))


# значения элементов каждого уровня шли в той же последовательности, что и в коллекции data
def flatten(data):
    res = []
    for elem in data:
        if not isinstance(elem, list):
            res.append(elem)
        else:
            data.extend(elem)
    return res


print(flatten([1, "abc", [[100, 200], 10, 20], [30, 40]]))


def deep_count(a):
    lst, count = [a], 0
    while lst:
        elem = lst.pop()
        for item in elem:
            if isinstance(item, list):
                lst.append(item)
                count += 1
            else:
                count += 1
    return count

# print(deep_count([]), 0)
# print(deep_count([1, 2, 3]), 3)
# print(deep_count(["x", "y", ["z"]]), 4)
print(deep_count([1, 2, [3, 4, [5]]]), 7)
# print(deep_count([[[[[[[[[]]]]]]]]]), 8)


def flatten_rec(lst):
    out = []
    for v in lst:
        if isinstance(v, list):
            out.extend(flatten_rec(v))
        else:
            out.append(v)
    return out


print(flatten_rec([1, 2, [3, 4, [5]]]))


# глубина вложенного списка

a = [1,[3,[2,3,[4]]],2,[2,3,4,[3,4,[2,3],5]]]

def rec(spicok, level=1):
    print(*spicok, 'level=', level)
    for i in spicok:
        if type(i) == list:
            rec(i, level+1)

rec(a)