# Создан словарь и очищен для того что бы было изначальное понимание какие поля будут использованы для библиотеки
library = {
    'title': {
        'author': None,
        'year': None,
        'availability': None
    },
}
library.clear()


def add_book(title, author, year):  # В дальнейшем уберу аргументы,
    # так как проверку и ввод аргументов удобнее проводить внутри функции
    if title in library.keys():
        choice = ''
        while choice not in ['1', '2']:
            choice = input('Книга с таким названием существует!\n'
                           'Выберите дальнейшее действие введя цифру:\n'
                           '1. Обновить информацию о книге\n'
                           '2. Не вносить изменения\n'
                           '3. Показать информацию о книге (в разработке)\n')  # здесь будет функция find_book()
            if choice == '3':
                print('\nФункция находится в разработке.\n')
                input('Для возврата в предыдущее меню нажмите ввод (enter)\n')
        if choice == '1':
            library[title] = {'author': author, 'year': year, 'availability': None}
            print('Информация о книге обновлена!\n')
        if choice == '2':
            print('Изменения не вносились!\n')
    else:
        library[title] = {'author': author, 'year': year, 'availability': None}
        print('Книга добавлена в каталог  библиотеки!\n')


def remove_book(title):
    if title in library.keys():
        library.pop(title)
        print(f'Книга с названием "{title}" удалена!\n')
    else:
        print(f'Книги с названием "{title}" в каталоге нет!\n')


def issue_book(title):
    library[title]['availability'] = False


def return_book(title):
    library[title]['availability'] = True


if __name__ == '__main__':
    # Добавления новой книги
    add_book('История тестировщика', 'Yaroslav', 1989)
    print(library)

    # Добавление книги которая существует с другим автором
    add_book('История тестировщика', 'Ярослав', 1989)
    print(library)

    # Добавление еще одной книги для других функций
    add_book('Иная книга', 'Ярослав', 1989)
    print(library)

    # Удаление книги с именем 'Иная книга'
    remove_book('Иная книга')
    print(library)

    # Повторое удаление книги с именем 'Иная книга'
    remove_book('Иная книга')
    print(library)

    # Выдача книги и ее возврат в плане структуры будут в иерархии функции find_book()
    # то есть, нашел книгу и три действия: выдать на руки, вернуть на склад или возврат в предыдущее меню
    issue_book('История тестировщика')
    print(library)
    return_book('История тестировщика')
    print(library)
    # Приношу извинения за сумбурный код, но просили придерживаться метода последовательной разработки,
    # а в голове уже финишный код (его наброски)
