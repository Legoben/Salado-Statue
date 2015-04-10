from tornado import web, ioloop, escape
import json as j
import sys
import os


#Python 2.7

class Statue():
    def __init__(self):
        pass



class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        #ToDo: Present login page if user is not authed
        self.render("web/index.html", pages=jsa)

jsn = {}
jsa = []
def startup():
    #ToDo: hook up to statue

    thedir = "plugins"
    dirs = [ name for name in os.listdir(thedir) if os.path.isdir(os.path.join(thedir, name)) ]

    pages = [(r'/', IndexHandler)] #we need to add every page to this, along with the class(es) that viewing the page executes.
    
    for d in dirs:

        print(d)
        try:
            json = j.loads(open("plugins/"+d+"/conf.json").read())
        except Exception:
            continue

        exec "import plugins."+d+".main"

        jsn[json['webname']] = json
        jsa.append(json)
        pgs = []
        for p in json['routes']:
            pgs.append(("/"+json['webname']+p[0], eval("plugins."+d+".main."+p[1])))
            #if
            pgs.append(("/"+json['webname']+p[0]+"/([^/]+)", eval("plugins."+d+".main."+p[1])))

        pages.extend(pgs)

    print(pages)


    #start tornado sever



    app = web.Application(pages, debug=True)
    app.listen(9893)
    ioloop.IOLoop.instance().start()  #The program will never get past this. Put all code above.

    pass



startup()