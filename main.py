def generate_numbers(n):
    count = 1
    while count <= n:
        yield count
        count += 1
gen = generate_numbers(3)
print(next(gen))
print(next(gen))
print(next(gen))
#or
generate_1 = (x + 1 for x in range(4))
for i in generate_1:
    print(i)
#
def generate_even_numbers(n):
    count = 1
    while count <= n:
        if count % 2 == 0:
            yield count
        count += 1
gen_even = generate_even_numbers(5)
print(next(gen_even))
print(next(gen_even))
#or
generate_2 = (x + 2 for x in range(5))
for i in generate_2:
    print(i)
#
def infinite_sequence(start):
    while True:
        yield start
        start += 1
gen_infinite = infinite_sequence(1)
print(next(gen_infinite))
print(next(gen_infinite))
#
def reverse_list(lst):
    for i in lst[::-1]:
        yield i
gen_reverse = reverse_list(["Areg", "Mels"])
print(next(gen_reverse))
#








