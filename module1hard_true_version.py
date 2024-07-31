students = {'Johhny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_stud = (list(students))
sort_stud = (sorted(sort_stud))

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades_0 = sum(grades[0]) / len(grades[0])
grades_1 = sum(grades[1]) / len(grades[1])
grades_2 = sum(grades[2]) / len(grades[2])
grades_3 = sum(grades[3]) / len(grades[3])
grades_4 = sum(grades[4]) / len(grades[4])

dict_book = dict.fromkeys(sort_stud)

dict_book['Aaron'] = grades_0
dict_book['Bilbo'] = grades_1
dict_book['Johhny'] = grades_3
dict_book['Khendrik'] = grades_2
dict_book['Steve'] = grades_4
print(dict_book)
