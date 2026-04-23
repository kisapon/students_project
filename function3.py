from app import  *
def view_student():
    student_id = int(input("Введите ID студента: "))
    data = load_data()

    for student in data["students"]:
        if student["id"] == student_id:
            average = round(sum(student["rating"]) / len(student["rating"]), 2)
            print(f"ID: {student['id']}\tИмя: {student['name']}\tФамилия: {student['surname']}\tОтчество: {student['patronymic']}"
                  f"\tГруппа: {student['group']}\tОценки: {student['rating']}\t Средний балл: {average}")
        return print("Студент с таким ID не найден.")