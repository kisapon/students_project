from app import *
def add_student():
    data = load_data()

    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    group = input("Введите группу: ")
    rating = []
    for i in range(1, 5):
        rate = int(input(f"Введите {i}-ую оценку: "))
        rating.append(rate)

    student = {
    "id": data["next_id"],
    "name": name,
    "surname": surname,
    "patronymic": patronymic,
    "group": group,
    "rating": rating
    }

    data["students"].append(student)
    data["next_id"] += 1
    save_data(data)

    print("Студент добавлен. Его ID:", student["id"])


БЕБЕБЕБЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ
