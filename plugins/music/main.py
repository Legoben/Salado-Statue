from tornado import web
import json

#morse code
print "MCode Imported"

class DoMusic(web.RequestHandler):
    def post(self, *args, **kwargs):
        pass




#"/myroute"
class MyPage(web.RequestHandler):
    def get(self, *args, **kwargs):
        #Do the thing
        self.render("web/index.html")
        print("It worked!!")

        pass
