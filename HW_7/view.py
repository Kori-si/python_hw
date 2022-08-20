import csv

data = r'data\phone_book.csv'

def book():
    with open(data, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        print("\nФамилия Имя | Телефон")
        for row in reader:
            print(row['Surname'], row['Name'], '|', row['Telephone'])

def new_contact():
    list = []
    surname = input('Фамилия: ')
    list.append(surname)
    name = input('Имя: ')
    list.append(name)
    telephone = input('Телефон: ')
    list.append(telephone)
    with open(data, mode="a", encoding='utf-8') as csvfile:
        file_writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        file_writer.writerow(list)

def search():
    contact = input('Введите Фамилию, Имя или Телефон: ')
    list = []
    with open(data, mode="r", encoding='utf-8') as csvfile:
        sear = csv.DictReader(csvfile, delimiter=";")
        for cont in sear:
            if contact in cont['Surname'] or contact in cont['Name'] or contact in cont['Telephone']:
                list.append(cont)
        print(list)

