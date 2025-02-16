def most_frequent(tup, n):
    result = tuple(tup.count(x) for x in tup)
    result_zip = tuple(set(zip(tup, result)))
    sorted_result = sorted(result_zip, key=lambda x: x[1], reverse=True)
    n_result = [x for x in sorted_result[:n]]
    return n_result

t = (4, 2, 2, 8, 4, 4, 5, 6, 2, 8, 8, 8, 4, 4, 7, 7)
print(most_frequent(t, 3))
#
def sort_by_second(tup):
    result = tuple(sorted(tup, key = lambda x: x[1]))
    return result

data = (("Alice", 28), ("Bob", 25), ("Charlie", 30), ("David", 22))
print(sort_by_second(data))
#
def summarize(*args):
    x, y, z = args
    return len(x + y + z), x + y + z

print(summarize((1, 2, 3), (4, 5), (6, 7, 8, 9)))
#
def rotate_matrix(matrix):
    result = tuple(zip(matrix[0], matrix[1], matrix[2]))
    reversed_result = tuple((tuple(reversed(x)) for x in result))
    return reversed_result

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(rotate_matrix(matrix))
#
