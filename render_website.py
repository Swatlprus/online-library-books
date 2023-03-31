import os
import json
import math
from environs import Env
from more_itertools import chunked
from jinja2 import Environment, FileSystemLoader, select_autoescape


def on_reload(library_books):
    with open(library_books, 'r', encoding='utf-8') as file:
        books_description = json.load(file)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    os.makedirs('./pages', exist_ok=True)

    count_pages = math.ceil(len(books_description) / 20)
    for number, book_page in enumerate(list(chunked(books_description, 20)), start=1):
        rendered_page = template.render({'books': list(chunked(book_page, 2)), 'count_pages': count_pages, 'current_page': number})
        if number == 1:
            with open(f'pages/index.html', 'w', encoding="utf8") as file:
                file.write(rendered_page)
        with open(f'pages/index{number}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == "__main__":
    env = Env()
    env.read_env()
    library_books = env("LIBRARY_BOOK", default='media/books.json')
    on_reload(library_books)