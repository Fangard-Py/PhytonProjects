students = {'Johhny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_stud = (list(students))
sort_stud = (sorted(sort_stud))

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades_0 = set(grades[0])
grades_0 = list(grades_0)
sum_grad = sum(grades_0)
last_grad = sum_grad / len(grades_0)

grades_1 = set(grades[1])
grades_1 = list(grades_1)
sum_grad = sum(grades_1)
last_grad1 = sum_grad / len(grades_1)

grades_2 = set(grades[2])
grades_2 = list(grades_2)
sum_grad = sum(grades_2)
last_grad2 = sum_grad / len(grades_2)

grades_3 = set(grades[3])
grades_3 = list(grades_3)
sum_grad = sum(grades_3)
last_grad3 = sum_grad / len(grades_3)

grades_4 = set(grades[4])
grades_4 = list(grades_4)
sum_grad = sum(grades_4)
last_grad4 = sum_grad / len(grades_4)

dict_book = dict.fromkeys(sort_stud)

dict_book['Aaron'] = last_grad
dict_book['Bilbo'] = last_grad1
dict_book['Johhny'] = last_grad3
dict_book['Khendrik'] = last_grad2
dict_book['Steve'] = last_grad4
print(dict_book)
