def rank_students(students, scores):
    average_result = tuple(sum(x) / 3 for x in scores)
    result = tuple(zip(students, average_result))
    sorted_result = tuple(sorted(result, key = lambda x: x[1], reverse = True))
    return sorted_result

students = ("Alice", "Bob", "Charlie", "David")
scores = ((85, 90, 78), (80, 85, 88), (92, 96, 94), (70, 75, 72))
print(rank_students(students, scores))
#
def rotate_matrix(matrix):
    rotated = tuple(zip(*reversed(matrix)))
    return rotated

matrix = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
    (13, 14, 15, 16)
)
print(rotate_matrix(matrix))
#
def transform_tuple(numbers):
    result = tuple(x * 2 if x % 2 == 0 else x * 3 for x in numbers)
    return result
print(transform_tuple((1, 2, 3, 4, 5)))
#
data = (10, 20, 30, 40, 50, 60, 70)
x, *middle, y = data
middle = tuple(middle)
print(middle)
#
def sort_tuple(*args):
    return tuple(sorted(args))

print(sort_tuple(12, 3, 8, 19, 5))
#
names = ("Alice", "Bob", "Charlie", "David")
ages = (25, 30, 22, 27)
zipped = tuple(zip(names, ages))
print(zipped)
a, b = zip(*zipped)
print(a)
print(b)
#
words = ("apple", "banana", "cherry", "date", "elderberry", "fig", "grape")
_, d, _, f, _, c, _ = words
even_index = tuple(enumerate((d, f, c,)))
print(even_index)
#
students = (
    ("Alice", 25, (85, 90, 88)),
    ("Bob", 22, (78, 82, 80)),
    ("Charlie", 23, (92, 95, 94)),
)

def calculate_averages(student_records):
    average_result = tuple(sum(x[2]) / len(x[2]) for x in students)
    students_name = tuple(x[0] for x in students)
    result = list(zip(students_name, average_result))
    return result
print(calculate_averages(students))
#
numbers = (4, 2, 6, 4, 7, 4, 2, 6, 4, 8, 4, 6)
count = tuple((numbers.count(x) for x in numbers))
frequent = tuple(zip(numbers, count))
print(frequent)
#



