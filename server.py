from livereload import Server
from render_website import on_reload


server = Server()
on_reload()
server.watch('template.html', on_reload)
server.serve(root='.', default_filename='./pages/index1.html')