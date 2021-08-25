user_input = int(input())
exam_marks = {
    "Cierra Vega": 175,
    "Alden Cantrell": 200,
    "Kierra Gentry": 165,
    "Pierre Cox": 190,
}

new_marks = exam_marks.copy()

for key in exam_marks.keys():
    if new_marks[key] < user_input:
        del new_marks[key]
print(new_marks)
