def create_list_while(n):
    start = 0
    list_of_numbers = []
    while start < n:
        start += 1
        list_of_numbers.append(start)
    return list_of_numbers
print(create_list_while(6))
#
def reverse_list(lst):
    i = len(lst) - 1
    new_list = []
    while i >= 0:
        new_list.append(lst[i])
        i -= 1
    return new_list
print(reverse_list([1, 2, 3, 4, 5]))
#
nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)
#
def create_list_rec(n, lst=[]):
    i = 0
    while i < n:
        i += 1
        lst.append(i)
    return lst
print(create_list_rec(10))
#
def sum_recursive(lst):
    return sum(lst)
print(sum_recursive([1, 2, 3, 4, 5]))
#
def square_numbers(lst):
    return list(map(lambda x: x ** 2, lst))
print(square_numbers([1, 2, 3, 4]))
#
def filter_evens(lst):
    return list(filter(lambda x: x % 2 == 0, lst))
print(filter_evens([1, 2, 3, 4, 5, 6]))
#
