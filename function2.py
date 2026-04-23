from app import *
def view_all_students():
    data = load_data()
    students = data["students"]

    if not students:
        print("Список студентов пуст.")
    return
for student in students:
        print(f"ID: {student['id']}\tИмя: {student['name']}\tФамилия: {student['surname']}\tОтчество: {student['patronymic']}"
        f"\tГруппа: {student['group']} \tОценки: {student['rating']}")
