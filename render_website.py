import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


def on_reload():
    with open('media/books.json', 'r', encoding='utf-8') as f:
        books = json.load(f)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render({'books': list(chunked(books, 2)) })


    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


if __name__ == "__main__":
    on_reload()