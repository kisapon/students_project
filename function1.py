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

KZKZKZKKZZKZKZKKZKZKZKKZK

    data["students"].append(student)
    data["next_id"] += 1
    save_data(data)

    print("Студент добавлен. Его ID:", student["id"])
