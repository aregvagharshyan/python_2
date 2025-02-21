sum_of_range = sum(range(1, 11))
print(sum_of_range)
#
for i in range(5, 51):
    if i % 5 == 0:
        print(i)
#or#
for i in range(5, 51, 5):
    print(i)
#
for i in range(19, 0, -1):
    if i % 2 == 1:
        print(i)
#
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
new_list = [my_list[i] for i in range(0, len(my_list) + 1, 2)]
print(new_list)
#or#
for i in range(0, len(my_list) + 1, 2):
    print(my_list[i])
#
for i in range(100, 49, -5):
    print(i)
#
def in_range(num, start, stop):
    return start >= num < stop
print(in_range(7, 7, 10))
#
create_list = []
for i in range(1, 21):
    create_list.append(i)
print(create_list)
#or#
create_list_2 = [x for x in range(1, 21)]
print(create_list_2)