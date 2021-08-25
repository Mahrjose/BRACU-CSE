student_mark = int(input("Please Enter the student's mark: "))

if student_mark >= 90 and student_mark <= 100:
    print("A")
elif student_mark >= 80 and student_mark <= 89:
    print("B")
elif student_mark >= 70 and student_mark <= 79:
    print("C")
elif student_mark >= 60 and student_mark <= 69:
    print("D")
elif student_mark >= 50 and student_mark <= 59:
    print("E")
elif student_mark < 50 and student_mark >= 0:
    print("F")
else:
    print("Error: Please enter Student marks in the range between 0 to 100 ")
