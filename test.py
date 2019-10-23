from app2 import app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop




http_server = HTTPServer(WSGIContainer(app))

http_server.listen(5500)
IOLoop.instance().start()