def create_list_while(n):
    i = 0
    list_of_numbers = []
    while i < n:
        i += 1
        list_of_numbers += [i]
    return list_of_numbers
print(create_list_while(10))
#
def generate_numbers(n):
    if n == 1:
        return [1]
    return generate_numbers(n - 1) + [n]
create_list = [x for x in generate_numbers(20)]
print(create_list)
#
nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
filtered_nums = [x for x in filter(lambda x: x % 2 == 0 and x % 3 == 0, nums)]
print(filtered_nums)
#
def create_list_rec(n, lst=None):
    i = 0
    list = []
    while i < n:
        i += 1
        list += [i]
    return list
print(create_list_rec(10))
#
def sum_recursive(lst):
    sum_of_list = 0
    for i in lst:
        sum_of_list += i
    return sum_of_list
print(sum_recursive([1, 2, 3, 4, 5]))
#
def square_numbers(lst):
   return list(map(lambda x: x ** 2, lst))
print(square_numbers([1, 2, 3, 4]))
#
def create_list(n):
    i = 0
    result = []
    while i < n:
        i += 1
        result += [i]
    return result
print(create_list(10))
