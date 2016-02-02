from tornado import web, ioloop

class MainHandler(web.RequestHandler):
    def post(self, *args, **kwargs):
        pass



app = web.Application([
        (r"/", MainHandler),
    ], debug=True)


if __name__ == "__main__":

    app.listen(9893)
    ioloop.IOLoop.instance().start()  # The program will never get past