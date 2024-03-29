from check import *
from loger import *        


        
def interface():
    with open("phonebook.txt", "a", encoding='utf-8'):
        pass
    choice = ''
    print(
        "Варианты действия: \n" \
        "1 - Ввод данных контакта \n" \
        "2 - Вывести данные на экран \n" \
        "3 - Поиск контакта \n" \
        "4 - Выход"
        )
    print()
    choice = input("Выберите номер действия: ")
    print()
    while choice not in ('1', '2', '3', '4'):
        print("Некорректный ввод данных!")
        choice = input("Выберите номер действия: ")
        print()
    match choice:
        case '1':
            data_input()
        case '2':
            print_data()
        case '3':
            search_contact()
        case '4':
            print('Всего доброго!')