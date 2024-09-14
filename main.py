library = {
    'title': {
        'author': None,
        'year': None,
        'availability': None
    },
}
library.clear()
add_book_query = 'Книга с таким названием существует!\nВыберите дальнейшее действие введя цифру:\n'
aad_book_action = ['1. Обновить информацию о книге',
                   '2. Не вносить изменения',
                   '3. Показать информацию о книге']
library_management_query = 'Необходимо выбрать действие введя его цифру:\n'
library_management_action = ['1. Добавить книгу в каталог (обновить информацию о книге)',
                             '2. Удалить книгу из каталога',
                             '3. Найти книгу (в том числе выдать и вернуть)',
                             '4. Информация о количестве книг в каталоге',
                             '5. Завершить работу (выход)']
issue_return_book_query = 'Необходимо выбрать действие введя его цифру:\n'
issue_return_book_action = ['1. Выдать книгу на руки',
                            '2. Сдать книгу на склад',
                            '3. Вернуться в предыдущее меню']


def input_book_title_answer_year():
    print('Раздел добавления (обновления) книги в каталог')
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


def choice_of_answer(query, list_of_action):
    choice = ''
    list_of_answer = [str(i + 1) for i in range(len(list_of_action))]
    while choice not in list_of_answer:
        print(query)
        for action in list_of_action:
            print(action)
        choice = input()
    return choice


def add_book(info_book):
    title = info_book[0]
    author = info_book[1]
    year = info_book[2]
    if title in library.keys():
        choice = choice_of_answer(add_book_query, aad_book_action)
        if choice == '3':
            find_book(title, True)
            return add_book([title, author, year])
        elif choice == '1':
            library[title] = {'author': author, 'year': year, 'availability': None}
            print(f'Информация о книге с названием "{title}" обновлена!\n')
            input('Для продолжения работы нажмите ввод (enter)\n')
        elif choice == '2':
            print(f'Изменения в книгу с названием "{title}" не вносились!\n')
            input('Для продолжения работы нажмите ввод (enter)\n')
    else:
        library[title] = {'author': author, 'year': year, 'availability': None}
        print(f'Книга с названием "{title}" добавлена в каталог  библиотеки!\n')
        input('Для продолжения работы нажмите ввод (enter)\n')


def remove_book():
    print('Раздел удаления книги из каталога')
    title = input('Введите название книги:\n')
    if title in library.keys():
        library.pop(title)
        print(f'Книга с названием "{title}" удалена!\n')
        input('Для продолжения работы нажмите ввод (enter)\n')
    else:
        print(f'Книги с названием "{title}" в каталоге нет!\n')
        input('Для продолжения работы нажмите ввод (enter)\n')


def issue_book(title):
    library[title]['availability'] = False
    print(f'Книга с названием "{title}" выдана на руки!\n')
    input('Для продолжения работы нажмите ввод (enter)\n')


def return_book(title):
    library[title]['availability'] = True
    print(f'Книга с названием "{title}" возвращена на склад!\n')
    input('Для продолжения работы нажмите ввод (enter)\n')


def find_book(title, in_another_def):
    if not in_another_def:
        print('Раздел поиска книги в каталоге')
        title = input('Введите название книги:\n')
    if title in library.keys():
        # if library[title]['availability'] is None:
        # status = 'Книга в библиотеке, но ее статус не определен'
        if library[title]['availability']:
            status = 'Книга доступна'
        else:
            status = 'Книга выдана'
        print(f'Книга: "{title}"\n'
              f'Автор: {library[title]['author']}\n'
              f'Год издания: {library[title]['year']}\n'
              f'Статус: {status}\n')
        input('Для продолжения работы нажмите ввод (enter)\n')

        if not in_another_def:
            choice = choice_of_answer(issue_return_book_query, issue_return_book_action)
            if choice == '1':
                issue_book(title)
            elif choice == '2':
                return_book(title)
    else:
        print(f'Книги с названием "{title}" в каталоге нет!\n')
        input('Для продолжения работы нажмите ввод (enter)\n')


def library_management():
    print('*' * 100 + '\nТерминал библиотекаря\nУчетная запись № 000-217/2F\n')
    choice = choice_of_answer(library_management_query, library_management_action)
    if choice == '1':
        add_book(input_book_title_answer_year())
    elif choice == '2':
        remove_book()
    elif choice == '3':
        find_book('', False)
    elif choice == '4':
        print(f'\nКниг в каталоге:{len(library)} шт.\n')
        input('Для продолжения работы нажмите ввод (enter)\n')
    elif choice == '5':
        print('Хорошего и продуктивного дня!!!')
        return 'exit'


if __name__ == '__main__':
    ext = ''
    while ext != 'exit':
        ext = library_management()
