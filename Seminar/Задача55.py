# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1. UI (user interface)
# 2. Создать файл 
# 3. Читать файл 
# 4. Вывод данных на экран:
# - считать файл
# - сохранить в переменной
# - вывести на экран
# 5. Запись контакта: 
# - запросить данные 
# - сохранить в переменную 
# - записать в файл 
# 6. Поиск контакта:
# - запросить данные поиска
# - сохранить в переменную
# - считать файл
# - сохранить в переменную
# - произвести поиск


def surname_data():
    return input('Введите фамилию: ')

def name_data():
    return input('Введите имя: ')

def patronymic_data():
    return input('Введите отчество: ')

def phone_number_data():
    return input('Введите номер телефона: ')

def address_data():
    return input('Введите адрес: ')

def input_contact():
    surname = surname_data()
    name = name_data()
    patronymic = patronymic_data()
    phone_number = phone_number_data()
    address = address_data()
    return f'{surname} {name} {patronymic} {phone_number} {address}'

def add_contact():
    contact = input_contact()
    with open('Phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(contact + '\n\n')

def read_file():
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        return data.read()

def print_contacts():
    data = read_file()
    print()
    print(data)

def search_contact():
    print('Варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По номеру телефона\n'
        '5. По адресу')
    choice = input('Выберите вариант поиска: ')
    i_choice = int(choice) - 1
    search = input('Введите данные для поиска: ')
    print()
    data_str = read_file().rstrip()
    if search not in data_str:
        print('Такого нет')
    else:
        data_lst = data_str.split('\n\n')
        for contact_str in data_lst:
            contact_lst = contact_str.replace('\n', ' ').split()
            if search in contact_lst[i_choice]:
                print()
                print(contact_str)
                choice_search = input('Контакт верный? 1 - Да, 2 - Нет: ')
                if choice_search == '1':
                    return contact_str
        print('Контакт не найден')

def change_contact():
    print('Какую запись требуется изменить?')
    contact = search_contact()
    if contact:
        print(contact)
        new_contact = contact.replace('\n', ' ').split()
        print('Варианты замены:\n'
        '1. Фамилия\n'
        '2. Имя\n'
        '3. Отчество\n'
        '4. Номер телефона\n'
        '5. Адрес\n'
        '6. Контакт полностью')
        choice = input('Выберите вариант замены: ')
        print('Требуются данные для замены.')
        if choice != '6':
            i_choice = int(choice) - 1
            change = input('Введите изменяемую часть контакта: ')
            new_contact [i_choice] = change
            new_contact = f'{new_contact[0]} {new_contact[1]} {new_contact[2]} {new_contact[3]} {new_contact[4]}'
        else:
            new_contact = input_contact()
        note_str = read_file()
        with open('Phonebook.txt', 'w', encoding='utf-8') as new_note_str:
            note_str = note_str.replace(contact, new_contact)
            new_note_str.write(note_str)
            print()

def delete_contact():
    print('Какую запись требуется удалить?')
    contact = search_contact()
    if contact:
        print(contact)
        note_str = read_file()
        with open('Phonebook.txt', 'w', encoding='utf-8') as new_note_str:
            note_str = note_str.replace(contact + '\n\n', '')
            new_note_str.write(note_str)

def user_interface():
    with open('Phonebook.txt', 'a', encoding='utf-8'):
        pass
    cmd = None
    while cmd != '6':
        print('Меню:\n'
            '1. Запись контакта\n'
            '2. Вывести данные на экран\n'
            '3. Поиск контакта\n'
            '4. Изменить контакт\n'
            '5. Удалить контакт\n'
            '6. Выход')
        cmd = input('Введите номер операции: ')
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')
        if cmd == '1':
            add_contact()
        elif cmd == '2':
            print_contacts()
        elif cmd == '3':
            search_contact()
        elif cmd == '4':
            change_contact()
        elif cmd == '5':
            delete_contact()
        elif cmd == '6':
            print('Всего доброго!')
    
user_interface()
