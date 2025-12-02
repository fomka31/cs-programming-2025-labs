#Task_10

stud_list = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]

stud_dict = dict()

for name,grade in stud_list:
    stud_dict[name] = (sum(i for i in grade) / len(grade)).__round__(3)

sorted_students = sorted(stud_dict.items(), key=lambda student: student[1], reverse=True)
best_student_name, best_student_score = sorted_students[0]

print(f'Лучший ученик: {best_student_name}, его(её) средний балл: {best_student_score}')