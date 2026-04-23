import json

DATA_FILE = "students.json"

def load_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"students": [], "next_id": 1}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


from function1 import *
from function2 import *
from function3 import *
from function4 import *

print("Приложение по работе со студентами.")
while True:
    print("\nФункционал:")
    print("1 -> Добавление нового студента.")
    print("2 -> Просмотр всех студентов.")
    print("3 -> Просмотр одного студента, включая его средний балл.")
    print("4 -> Удаление студента.")
    print("5 -> Выход.")

    choice = input("Выберите функцию: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_all_students()
    elif choice == '3':
        view_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("До свидания!")
        break
    else:
        print("Такой функции нет! Попробуйте снова.")