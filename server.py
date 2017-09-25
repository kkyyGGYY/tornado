import config
import tornado.web
from views import index
import tornado.httpserver
import tornado.ioloop

if __name__ == "__main__":
    print(config.options['list'])
    app = tornado.web.Application([
        (r"/", index.IndexHandler),
    ], **config.settings)
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(config.options['port'])

    tornado.ioloop.IOLoop.current().start()
