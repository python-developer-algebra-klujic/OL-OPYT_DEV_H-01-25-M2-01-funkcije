
subjects = ['Matematika', 'Fizika', 'Kemija', 'Fizika']
students = ['Ana', 'Marko', 'Mirko', 'Slavko']
grades = [5, 4, 4, 3]

# CILJ
# students_score = [
#     ('Matematika', 'Ana', 5),
#     ('Fizika', 'Marko', 4),
#     ('Kemija', 'Mirko', 4),
#     ('Fizika', 'Slavko', 3),
# ]

# students_score = []

# subjects_len = len(subjects)
# students_len = len(students)
# grades_len = len(grades)

# range_limit = max([subjects_len, subjects_len, grades_len])

# for i in range(range_limit):
#     student = students[i]
#     subject = subjects[i]
#     grade = grades[i]

#     students_score.append((subject, student, grade))

# print(students_score)

# zip-anje lista
students_score = zip(subjects, students, grades)

# print(list(students_score))
# print()

subjects_01, students_01, grades_01 = zip(*students_score)

print(list(subjects_01))
print(students_01)
print(grades_01)
