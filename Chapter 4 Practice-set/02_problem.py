student_marks = [] # blank list
for i in range(0, 6):
    marks = int(input("Enter students marks: "))
    student_marks.append(marks)

student_marks.sort()
print(f"List of student marks {student_marks}")
