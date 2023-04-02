import os
import json
import math
from environs import Env
from more_itertools import chunked
from jinja2 import Environment, FileSystemLoader, select_autoescape


def render_page(rendered_page, number):
    with open(f'pages/index{number}.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)


def on_reload(library_books, number_book_on_page, columns_on_page):
    with open(library_books, 'r', encoding='utf-8') as file:
        book_descriptions = json.load(file)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    os.makedirs('./pages', exist_ok=True)

    pages_count = math.ceil(len(book_descriptions) / int(number_book_on_page))
    chunked_book_descriptions = list(chunked(book_descriptions,
                                             int(number_book_on_page)))

    for number, book_page in enumerate(chunked_book_descriptions, start=1):
        books_description_on_page = list(chunked(book_page,
                                                 int(columns_on_page)))
        rendered_page = template.render({'books': books_description_on_page,
                                         'pages_count': pages_count,
                                         'current_page': number})
        if number == 1:
            render_page(rendered_page, number='')
        render_page(rendered_page, number)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    library_books = env('LIBRARY_BOOKS', 'media/books.json')
    number_book_on_page = env('NUMBER_BOOKS_ON_PAGE', 20)
    columns_on_page = env('COLUMNS_ON_PAGE', 2)
    on_reload(library_books, number_book_on_page, columns_on_page)
