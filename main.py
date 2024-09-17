from os import system

# в отдельном файле
library = {
    'title': {
        'author': None,
        'year': None,
        'availability': None
    },
}
library.clear()

# не забыть убрать в отдельный модуль
add_book_query = '\nКнига с таким названием существует!\n\nВыберите дальнейшее действие введя цифру:'
add_book_action = ['1. Обновить информацию о книге',
                   '2. Не вносить изменения',
                   '3. Показать информацию о книге']
library_management_query = '\nНеобходимо выбрать действие введя его цифру:'
library_management_action = ['1. Добавить книгу в каталог (обновить информацию о книге)',
                             '2. Удалить книгу из каталога',
                             '3. Найти книгу (в том числе выдать и вернуть)',
                             '4. Просмотр всего каталога',
                             '5. Завершить работу (выход)']
issue_return_book_query = '\nНеобходимо выбрать действие введя его цифру:'
issue_return_book_action = ['1. Выдать книгу на руки',
                            '2. Сдать книгу на склад',
                            '3. Вернуться в предыдущее меню']


def choice_of_answer(query, list_of_action):
    choice = ''
    list_of_answer = [str(i + 1) for i in range(len(list_of_action))]
    while choice not in list_of_answer:
        print(query)
        for action in list_of_action:
            print(action)
        choice = input()
    return choice


def issue_book(title):
    library[title]["availability"] = False
    print(f'\nКнига с названием "{title}" выдана на руки!\n')
    input('Для продолжения работы нажмите ввод (enter)\n')


def return_book(title):
    library[title]["availability"] = True
    print(f'\nКнига с названием "{title}" возвращена на склад!\n')
    input('Для продолжения работы нажмите ввод (enter)\n')


def issue_and_return_book(title):
    choice = choice_of_answer(issue_return_book_query, issue_return_book_action)
    if choice == '1':
        issue_book(title)
    elif choice == '2':
        return_book(title)


def book_status(title):
    if library[title]["availability"] is None:
        return 'Книга в библиотеке, но ее статус не определен'
    elif library[title]["availability"]:
        return 'Книга доступна'
    else:
        return 'Книга выдана'


def print_book_info(title):
    print(f'\nКнига: "{title}"\t'
          f'Автор: {library[title]["author"]}\t'
          f'Год издания: {library[title]["year"]}\t'
          f'Статус: {book_status(title)}')


def find_book():
    system('cls||clear')
    print('\nРаздел поиска книги в каталоге\n')
    title = input('Введите название книги:\n')
    if title in library.keys():
        print_book_info(title)
        input('\nДля продолжения работы нажмите ввод (enter)\n')
        issue_and_return_book(title)

    else:
        print(f'\nКниги с названием "{title}" в каталоге нет!\n')
        input('Для продолжения работы нажмите ввод (enter)\n')


def input_book_title_author_year():
    system('cls||clear')
    print('\nРаздел добавления (обновления) книги в каталог\n')
    title = ''
    author = ''
    year = ''
    while not (''.join(title.split()).isalnum()):
        title = input('Введите название книги:\n')
    while not (''.join(author.split()).isalnum()):
        author = input('Укажите автора:\n')
    while not year.isdigit():
        year = input('Укажите год издания:\n')
    return [title, author, year]


def add_book(info_book):
    title = info_book[0]
    author = info_book[1]
    year = info_book[2]
    if title in library.keys():
        choice = choice_of_answer(add_book_query, add_book_action)
        if choice == '3':
            print_book_info(title)
            input('\nДля продолжения работы нажмите ввод (enter)\n')
            return add_book(info_book)
        elif choice == '1':
            library[title] = {'author': author, 'year': year, 'availability': library[title]["availability"]}
            print(f'\nИнформация о книге с названием "{title}" обновлена!\n')
            input('Для продолжения работы нажмите ввод (enter)\n')
        elif choice == '2':
            print(f'\nИзменения в книгу с названием "{title}" не вносились!\n')
            input('Для продолжения работы нажмите ввод (enter)\n')
    else:
        library[title] = {'author': author, 'year': year, 'availability': None}
        print(f'\nКнига с названием "{title}" добавлена в каталог  библиотеки!\n')
        input('Для продолжения работы нажмите ввод (enter)\n')


def remove_book():
    system('cls||clear')
    print('\nРаздел удаления книги из каталога\n')
    title = input('Введите название книги:\n')
    if title in library.keys():
        library.pop(title)
        print(f'Книга с названием "{title}" удалена!\n')
        input('Для продолжения работы нажмите ввод (enter)\n')
    else:
        print(f'\nКниги с названием "{title}" в каталоге нет!\n')
        input('Для продолжения работы нажмите ввод (enter)\n')


def library_catalog_view():
    system('cls||clear')
    print(f'\nПросмотр каталога книг')
    for book_name in library.keys():
        print_book_info(book_name)
    print(f'\nКниг в каталоге:{len(library)} шт.\n')
    input('Для продолжения работы нажмите ввод (enter)\n')


def library_management():
    system('cls||clear')
    print('*' * 100 + '\nТерминал библиотекаря\nУчетная запись № 000-217/2F')
    choice = choice_of_answer(library_management_query, library_management_action)
    if choice == '1':
        add_book(input_book_title_author_year())
    elif choice == '2':
        remove_book()
    elif choice == '3':
        find_book()
    elif choice == '4':
        library_catalog_view()
    elif choice == '5':
        print('Хорошего и продуктивного дня!!!')
        input()
        return 'exit'


if __name__ == '__main__':
    ext = ''
    try:
        while ext != 'exit':
            ext = library_management()
    except Exception as err:
        print(f'Возникла ошибка "{err}"\n\nСвяжитесь с администратором!\n')
        input('Для выхода нажмите ввод (enter)\n')
