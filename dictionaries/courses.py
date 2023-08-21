courses = {}

while True:
    data = input().split(" : ")
    if data[0] == "end":
        break

    course_name, student_name = data[0], data[1]

    if course_name not in courses.keys():
        courses[course_name] = [student_name]

    else:
        courses[course_name] += [student_name]

for each_course, students in courses.items():
    print(f"{each_course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
