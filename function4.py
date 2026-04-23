from app import *
def delete_student():
    student_id = int(input("Введите ID студента: "))
    data = load_data()

    for student in data["students"]:
        if student["id"] == student_id:
            data["students"].remove(student)
            save_data(data)
        print("Студент удален.")
    return print("Студент с таким ID не найден.")
