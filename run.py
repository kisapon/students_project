from app import *
from function1 import add_student
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
