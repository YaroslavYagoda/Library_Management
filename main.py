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
        if input('Книга с таким названием существует, обновить сведения о ней?(да/нет)').lower() in ('yes', 'да'):
            library[title] = {'author': author, 'year': year, 'availability': None}
    else:
        library[title] = {'author': author, 'year': year, 'availability': None}


def remove_book(title):
    if title in library.keys():
        library.pop(title)
        print(f'Книга с названием "{title}" удалена!')
    else:
        print(f'Книги с названием "{title}" в каталоге нет!')


def issue_book(title):
    library[title]['availability'] = False


def return_book(title):
    library[title]['availability'] = True


def find_book(title):
    if title in library.keys():
        if library[title]['availability'] is None:
            status = 'Книга в библиотеке, но ее статус не определен'
        elif library[title]['availability']:
            status = 'Книга доступна'
        else:
            status = 'Книга выдана'
        print(f'Книга с названием "{title}"\n'
              f'Автор: {library[title]['author']}\n'
              f'Год издания: {library[title]['year']}\n'
              f'Статус: {status}')
    else:
        print(f'Книги с названием "{title}" в каталоге нет!')


if __name__ == '__main__':
    # Раздел добавления книги
    add_book('ман', 'igor', 1989)
    add_book('ман', 'igoawetqwetr', 1989)
    add_book('екуке', 'igoawetqwetr', 1989)

    # Раздел удаления книги
    remove_book('екуке')
    remove_book('qwerqwer')

    # Раздел поиска книги и изменение ее статуса (не определена, В наличии, На Выдаче)
    find_book('ман')
    return_book('ман')
    find_book('ман')
    issue_book('ман')
    find_book('ман')
