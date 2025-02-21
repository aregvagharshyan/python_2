countries = {'Armenia': 'Yerevan', 'France': 'Paris', 'Japan': 'Tokyo'}
print(countries)
print(countries['France'])
for key, value in countries.items():
    print(f'Country: {key}, Capital: {value}')
#
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
grades.update({'David': 88})
grades.update({'Alice': 90})
grades.pop('Charlie')
average = 0
for value in grades.values():
    average += value
    average_grade = average / len(grades)
print(average_grade)
top_grade = max(grades.values())
top_students = [name for name, grade in grades.items() if grade == top_grade]
print(top_students)

