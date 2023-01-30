"""
Concerned with storing and retrieving books from a list
"""

books = []


def indexes():
    for index, book in enumerate(books, start=1):
        book['index'] = str(index)


def add_book(name, author):
    books.append({'name': name.lower(), 'author': author.lower(), 'read': False})


def list_books():
    for book in books:
        if book['read'] is False:
            status = 'Book is still unread'
        else:
            status = 'Book has been already read'
        print(f"\n{book['index']}."
              f"\nName of the book is: {book['name'].title()},"
              f"\nAuthor of the book is: {book['author'].title()}"
              f"\n{status}")


def read_book(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
        else:
            print("Book unknown! ")


def delete_book(delete_by, value):
    for book in books:
        if delete_by == 'index':
            if value == book['index']:
                books.remove(book)
        elif delete_by == 'name':
            if value == book['name']:
                books.remove(book)
        elif delete_by == 'author':
            if value == book['author']:
                books.remove(book)
        else:
            print("Book unknown! ")


def unexpected_delete(delete_by):
    if delete_by == 'index':
        return True
    elif delete_by == 'name':
        return True
    elif delete_by == 'author':
        return True
    else:
        return False
