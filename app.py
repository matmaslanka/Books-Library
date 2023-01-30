from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd'  to delete a book
- 'q' to quit

Your choice: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        database.indexes()
        if user_input == 'a':
            name = input(f'Please input the name of the book: ')
            author = input(f'Please input the author of the book: ')
            database.add_book(name, author)
            user_input = input(f'\nWhat you want to do next? {USER_CHOICE}')

        elif user_input == 'l':
            database.list_books()
            user_input = input(f'\nWhat you want to do next? {USER_CHOICE}')

        elif user_input == 'r':
            read_book_input = input(f'Please input the name of the book which you read: ').lower()
            database.read_book(read_book_input)
            user_input = input(f'\nWhat you want to do next? {USER_CHOICE}')
        # print(database.books)

        elif user_input == 'd':
            delete_by = input(f'Do you want delete by index, name, author?:')
            database.unexpected_delete(delete_by)
            if database.unexpected_delete(delete_by) is False:
                print("Unexpected Value!")
            else:
                delete_book_input = input(f'Please input the {delete_by} of the book that you want to delete: ').lower()
                database.delete_book(delete_by, delete_book_input)
            user_input = input(f'\nWhat you want to do next? {USER_CHOICE}')

        else:
            user_input = input(f'\nPlease try again! {USER_CHOICE}')


menu()
# def prompt_add_book(): ask for the book name and author
# def list_books(): show all the books in our list
# def prompt_read_book(): ask for book name and change it to "read" in our list
# def prompt_delete_book(): ask for book name and remove book from list
