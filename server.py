
from environs import Env
from livereload import Server
from render_website import on_reload


def start_server():
    server = Server()
    env = Env()
    env.read_env()
    library_books = env('LIBRARY_BOOKS', 'media/books.json')
    number_book_on_page = env('NUMBER_BOOKS_ON_PAGE', 20)
    columns_on_page = env('COLUMNS_ON_PAGE', 2)
    on_reload(library_books, number_book_on_page, columns_on_page)
    server.watch('template.html', on_reload(library_books,
                                            number_book_on_page,
                                            columns_on_page))
    server.serve(root='.', default_filename='./pages/index.html')


if __name__ == '__main__':
    start_server()
