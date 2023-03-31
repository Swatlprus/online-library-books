import os
import json
import math
from environs import Env
from more_itertools import chunked
from jinja2 import Environment, FileSystemLoader, select_autoescape


def on_reload(library_books, number_book_on_page, columns_on_page):
    with open(library_books, 'r', encoding='utf-8') as file:
        books_description = json.load(file)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    os.makedirs('./pages', exist_ok=True)

    pages_count = math.ceil(len(books_description) / int(number_book_on_page))
    chunked_books = list(chunked(books_description, int(number_book_on_page)))

    for number, book_page in enumerate(chunked_books, start=1):
        chunked_books_page = list(chunked(book_page, int(columns_on_page)))
        rendered_page = template.render({'books': chunked_books_page,
                                         'pages_count': pages_count,
                                         'current_page': number})
        if number == 1:
            index_page = 'pages/index.html'
        else:
            index_page = f'pages/index{number}.html'

        with open(index_page, 'w', encoding='utf8') as file:
            file.write(rendered_page)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    library_books = env('LIBRARY_BOOKS', 'media/books.json')
    number_book_on_page = env('NUMBER_BOOKS_ON_PAGE', 20)
    columns_on_page = env('COLUMNS_ON_PAGE', 2)
    on_reload(library_books, number_book_on_page, columns_on_page)
