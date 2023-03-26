import os
import json
from more_itertools import chunked
from jinja2 import Environment, FileSystemLoader, select_autoescape


def on_reload():
    with open('media/books.json', 'r', encoding='utf-8') as f:
        books = json.load(f)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    pages = os.makedirs('./pages')
    
    for number, book_page in enumerate(list(chunked(books, 20)), start=1):
                                       
        rendered_page = template.render({'books': list(chunked(book_page, 2))})
        with open(f'pages/index{number}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == "__main__":
    on_reload()