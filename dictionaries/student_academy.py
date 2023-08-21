students_info = {}
number = int(input())

for _ in range(number):
    student_name = input()
    grade = float(input())

    if student_name not in students_info.keys():
        students_info[student_name] = [grade]
    else:
        students_info[student_name] += [grade]

for student, grade in students_info.items():
    averageGrade = sum(grade) / len(grade)
    if averageGrade >= 4.50:
        print(f"{student} -> {averageGrade:.2f}")
    else:
        continue
