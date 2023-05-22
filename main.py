documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}



def get_names():
    num_doc = input('Введите номер документа: ')
    for output in documents:
        if output['number'] == num_doc:
            return (f"Документ принадлежит: {output['name']}")
    return 'Такого документа не существует'


def get_shelves():
    num_shelf = input('Введите номер документа: ')
    for key, value in directories.items():
        if num_shelf in value:
            return (f"Документ лежит на полке: {key}")
    return 'Такого документа не существует'


def get_list():
    for docs in documents:
        return (f'{docs["type"]} {docs["number"]} {docs["name"]}')


def add_doc():
    doc_typ = input('Введите тип документа: ')
    doc_num = input('Введите номер документа: ')
    doc_name = input('Введите имя владельца документа: ')
    doc_shelf = input('Введите номер полки для хранения документа: ')
    if doc_shelf not in directories:
        return ('Нет такой полки')
    else:
        documents.append({"type": doc_typ, "number": doc_num, "name": doc_name, })
        directories[doc_shelf].append(doc_num)
        return ('Документ добавлен')


def main():
    while True:
        return ('Возможные команды: p, s, l, a, q')
        command = input('Введите команду: ')
        if command == 'p':
            return (get_names())
        elif command == 's':
            return (get_shelves())
        elif command == 'l':
            get_list()
        elif command == 'a':
            add_doc()
        elif command == 'q':
            return ('Выход')
            break




