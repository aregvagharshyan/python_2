def analyze_tuple(tup):
    max_count = max(tup.count(x) for x in tup)
    index = tup.index(max(tup))
    reverse = tup[::-1]
    return max_count, index, reverse
t = (10, 20, 30, 20, 10, 40, 50, 10)
print(analyze_tuple(t))
#
def person_info(data):
    tuple_2 = ('name', 'age', 'job', 'city', 'extra')
    result = zip(tuple_2, data)
    for i, z in result:
        print(f'{i}: {z}')
person = ("Alice", 28, "Engineer", "New York", "Hobby: Chess", "Likes: Music")
person_info(person)
#
def swap(a, b):
    a, b = b, a
    return a, b
x, y = swap(5, 10)
print(x, y)
#
def pair_students(names, scores):
    scores = sorted(scores, reverse = True)
    names = sorted(names, key = len)
    result = list(zip(names, scores))
    return result
names = ("Alice", "Bob", "Charlie")
scores = (85, 92, 78)
print(pair_students(names, scores))
#
def rank_teams(teams):
    result = enumerate(teams, start = 1)
    for index, team in result:
        print(f'{index}. {team}')
teams = ("Lions", "Tigers", "Bears", "Wolves")
rank_teams(teams)
