from tornado import web, ioloop, escape
import json
from multiprocessing.pool import ThreadPool
import sys
from plugins import *


class Statue():
    def __init__(self):
        pass




#Tested using python 3.4
class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello world")




def startup(self):
    #hook up to statue


    #plugins --- http://martyalchin.com/2008/jan/10/simple-plugin-framework/

    #If we can't figure this out we can use some sort of config file. It's lame but it works.


    #start tornado sever
    pages = [(r'/', IndexHandler),] #we need to add every page to this, along with the class(es) that viewing the page executes.
    app = web.Application(pages, debug=True)


    app.listen(9893)
    ioloop.IOLoop.instance().start()  #The program will never get past this. Put all code above.

    pass


startup()