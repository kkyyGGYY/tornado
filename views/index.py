import tornado.web
from tornado.web import RequestHandler
import tornado.ioloop
import tornado.httpserver
import config


class IndexHandler(RequestHandler):
    def get(self):
        self.write("<h1>Hello world!</h1>")



