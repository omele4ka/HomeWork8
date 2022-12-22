import view

phone_book = []

def get_phone_book() -> list:
    global phone_book
    return phone_book

def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book

def add_contact():
    global phone_book
    contact = view.input_new_contact()
    phone_book.append(contact)

def remove_contact():
    global phone_book
    id = view.input_remove_contact()
    confirm = input(f'Вы точно хотите удалить контакт {phone_book[id-1][0]} (y/n)')
    if confirm.lower() == 'y':
        del_contact = phone_book.pop(id-1)
        print(f'Контакт {del_contact} удален\n')

def what_to_change_menu(change, id):
    global phone_book
    match change:
        case 1:
            phone_book[id - 1][0] = input('Введите новое имя:  ')
        case 2:
            phone_book[id - 1][0] = input('Введите новый номер телефона:  ')
        case 3:
            phone_book[id - 1][0] = input('Введите новый комментарий:  ')
        case 0:
            return True

def change_contact():
    global phone_book
    id = view.input_change_contact()
    confirm = input(f'Вы точно хотите изменить контакт {phone_book[id-1][0]} (y/n)')
    if confirm.lower() == 'y':
        while True:
            change = view.what_to_change()
            if what_to_change_menu(change, id):
                break
        print('Контакт был изменен')

def find_contact():
    global phone_book
    who_to_find = view.input_find_contact()
    nobody_found = True
    for id, contact in enumerate(phone_book):
        for item in contact:
            if who_to_find in item.lower():
                nobody_found = False
                print((id+1), * contact)
        if nobody_found:
            print('Таких здесь нет')

