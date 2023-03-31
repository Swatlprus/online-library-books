from livereload import Server
from render_website import on_reload


def start_server():
    server = Server()
    on_reload()
    server.watch('template.html', on_reload)
    server.serve(root='.', default_filename='./pages/index.html')


if __name__ == '__main__':
    start_server()
