def countdown(n):
    while n != -1:
        yield n
        n -= 1
gen = countdown(5)
print(list(gen))
#
def even_numbers():
    even = 0
    while True:
       yield even
       even += 2
gen = even_numbers()
print(next(gen))
print(next(gen))
#
def square_numbers(n):
    i = 1
    while i <= n:
        yield i ** 2
        i += 1
gen = square_numbers(5)
print(list(gen))
#
def filtered_words(words, min_length):
    for word in words:
        if len(word) >= min_length:
            yield word
words = ["apple", "is", "a", "fruit"]
gen = filtered_words(words, 3)
print(list(gen))
#
