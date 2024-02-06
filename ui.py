from logger import (
    input_data,
    print_data,
    copy_data,
    delete_data,
    update_data,
    delete_data_second,
    update_data_second,
)


def interface():
    print(
        "Добрый день! Это бот-помощник. \n"
        "Что вы хотите сделать? \n"
        "1 - Записать данные в первый файл\n"
        "2 - Вывести данные из файлов\n"
        "3 - Копировать данные из первого файла во второй\n"
        "4 - Удалить данные из первого файла\n"
        "5 - Изменить данные в первом файле\n"
        "6 - Удалить данные из второго файла\n"
        "7 - Изменить данные во втором файле"
    )
    command = int(input("Ваш выбор: "))

    while command < 1 or command > 7:
        command = int(input("Ошибка! Ваш выбор: "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        line_number = int(
            input("Введите номер строки для копирования из первого файла во второй: ")
        )
        copy_data(line_number)
    elif command == 4:
        line_number = int(input("Введите номер строки для удаления из первого файла: "))
        delete_data(line_number)
    elif command == 5:
        line_number = int(
            input("Введите номер строки для изменения данных в первом файле: ")
        )
        new_data = input("Введите новые данные: ")
        update_data(line_number, new_data)
    elif command == 6:
        line_number = int(input("Введите номер строки для удаления из второго файла: "))
        delete_data_second(line_number)
    elif command == 7:
        line_number = int(
            input("Введите номер строки для изменения данных во втором файле: ")
        )
        new_data = input("Введите новые данные: ")
        update_data_second(line_number, new_data)


interface()
