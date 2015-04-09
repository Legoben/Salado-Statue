from tornado import web

#morse code
print "Hello World"



#"/myroute"
class MyPage(web.RequestHandler):
    def get(self, *args, **kwargs):
        #Do the thing
        self.write("Hello World")
        print("It worked!!")

        pass
