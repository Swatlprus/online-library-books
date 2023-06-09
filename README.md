# Сайт онлайн-библиотеки

Данный проект это сайт онлайн-библиотеки на основе сайта [tululu.org](https://tululu.org/).

Сайт развернутый на GitHub Pages. В нем находятся статичные данные - https://swatlprus.github.io/online-library-books/pages/

## Установить/Скачать

Нажимаем в репозитории "Code", далее выбираем "Download ZIP". Разархивируем и открываем файл /pages/index.html.

Либо можно скачать через терминал с помощью команды

```shell
git clone https://github.com/Swatlprus/online_library.git
```

## Настройка переменных окружения

Файл .env нужно создать в корне сайта. Он не является обязательным, так как значения по умолчанию прописаны в файле render_website.py

Пример, как выглядит файл .env:
```
LIBRARY_BOOKS=media/books.json
NUMBER_BOOKS_ON_PAGE=20
COLUMNS_ON_PAGE=2
```

Значения переменных
```
LIBRARY_BOOKS - путь к файлу json с описаниями книг
NUMBER_BOOKS_ON_PAGE - количество книг на одной страницу
COLUMNS_ON_PAGE - количество колонок на одной странице
```
## Запустить сайт локально

В терминале запускаем файл render_website.py. Сайт будет доступ по адресу - http://127.0.0.1:5500/pages/index.html

```shell
python3 render_website.py
```

## Запустить сайт оффлайн из браузера

Чтобы открыть сайт через бразуер, просто перейдите в папку /pages и откройте с помощью браузера файл index.html. Теперь вы сможете перемещаться по сайту и открывать для чтения любую книгу.

## Цели проекта

Учебный проект по парсингу онлайн-библиотеки от онлайн-курса Devman (dvmn.org) ([dvmn.org](https://dvmn.org/)).