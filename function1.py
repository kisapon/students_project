from app import *

def add_student():
    data = load_data()

    id = int(input("Введите ID: "))
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    group = input("Введите группу: ")
    rating = []
    for i in range(1, 5):
        rate = int(input(f"Введите {i}-ую оценку: "))
        rating.append(rate)
    student = {
    "id": id,
    "name": name,
    "surname": surname,
    "patronymic": patronymic,
    "group": group,
    "rating": rating
    }

    print("Студент добавлен. Его ID:", student["id"])


    data["students"].append(student)
    save_data(data)

    print("Студент добавлен. Его ID:", student["id"])
    return student
