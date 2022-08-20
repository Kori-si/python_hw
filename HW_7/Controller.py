from view import book
from view import new_contact
from view import search

def book_the_directory():
    book()
    print()
    start()

def new_contact_in_directory():
    new_contact()
    print()
    start()

def search_in_directory():
    search()
    print()
    start()

def exit():
    print('Все-го хо-ро-ше-го')

def start():
    print('Телефонная книга')
    menu = int(input("Выбирите действие:"
                     "\n1 - показать все контакты"
                     "\n2 - добавить контакт"
                     "\n3 - найти контакт"
                     "\n4 - выход\n"))
    if menu == 1:
        book_the_directory()
    elif menu == 2:
        new_contact_in_directory()
    elif menu == 3:
        search_in_directory()
    elif menu == 4:
        exit()
