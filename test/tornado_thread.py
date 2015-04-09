#this code does not work


from tornado import web, ioloop, escape
import json
from multiprocessing.pool import ThreadPool

_workers = ThreadPool(30)

def start_server(port,*args, **kwargs):
    print("1")
    app.listen(port)
    print("2")
    ioloop.IOLoop.instance().start()
    print("3")

def callback():
    print("this should not happen")

class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello world")
        print("here")



app = web.Application([
     ('/', IndexHandler),
    ])

start_server(9833)


