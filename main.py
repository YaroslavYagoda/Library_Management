# Создан словарь и очищен для того что бы было изначальное понимание какие поля будут использованы для библиотеки
library = {
    'title': {
        'author': None,
        'year': None,
        'availability': None
    },
}
library.clear()


def add_book(title, author, year):
    if title in library.keys():
        if input('Книга с таким названием существует!\n'
                 'Если хотите обновить введите "да" (для отмены - что угодно):\n').lower() in ('yes', 'да'):
            library[title] = {'author': author, 'year': year, 'availability': None}
    else:
        library[title] = {'author': author, 'year': year, 'availability': None}


def remove_book(title):
    if title in library.keys():
        library.pop(title)
        print(f'Книга с названием "{title}" удалена!')
    else:
        print(f'Книги с названием "{title}" в каталоге нет!')


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