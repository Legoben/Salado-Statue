from tornado import web, ioloop, escape
import json as j
import sys
import os
from time import sleep
import RPi.GPIO as GPIO


# Python 2.7

class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # ToDo: Present login page if user is not authed
        self.render("web/index.html", pages=jsa)


jsn = {}
jsa = []

class Lights():
    # GPIO pins
    serial_pin = 23
    clock_pin = 24
    latch_pin = 25


    # cleanup and init GPIO pins when class is created
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.serial_pin, GPIO.OUT)
        GPIO.setup(self.clock_pin, GPIO.OUT)
        GPIO.setup(self.latch_pin, GPIO.OUT)

    # clock bit
    def clock(self):
        GPIO.output(self.clock_pin, GPIO.HIGH)
        sleep(0.01)
        GPIO.output(self.clock_pin, GPIO.LOW)
        sleep(0.01)

    # set 16 bits to parallel output on the shift register
    def latch(self):
        GPIO.output(self.latch_pin, GPIO.HIGH)
        GPIO.output(self.latch_pin, GPIO.LOW)

    # Convert Hexadecimal input to Binary
    def parsehex(array):
        for hex in range(len(array)):
            array[hex] = bin(int(array[hex], 16))[2:]
            array[hex] = [int(char) for char in array[hex]]
        return array

    # load pattern from multi-array
    def loadPattern(self, pattern, delay, hexinput=True):
        if hexinput:
            pattern = parsehex(pattern)
        GPIO.output(self.latch_pin, GPIO.LOW)
        for subarray_count in range(len(pattern)):
            for i in range(24):
                GPIO.output(self.serial_pin, pattern[subarray_count][i])
                self.clock()
                print "\033[92mShifted In: " + str(pattern[subarray_count]) + "\033[0m"
            sleep(delay)
            self.latch()

    # turn on a single light   Ex. light(12) - Turns on light number 12
    def light(self, lightNum):
        sequence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        sequence[lightNum] = 1

        self.loadPattern([sequence], 0)

    def __del__(self):
        GPIO.cleanup()

def startup():

    statue = Lights()

    #statue.loadPattern()

    thedir = "plugins"
    dirs = [name for name in os.listdir(thedir) if os.path.isdir(os.path.join(thedir, name))]

    pages = [(r'/',
              IndexHandler)]  # we need to add every page to this, along with the class(es) that viewing the page executes.

    for d in dirs:

        print(d)
        try:
            json = j.loads(open("plugins/" + d + "/conf.json").read())
        except Exception:
            continue

        exec "import plugins." + d + ".main"

        jsn[json['webname']] = json
        jsa.append(json)
        pgs = []
        for p in json['routes']:
            pgs.append(("/" + json['webname'] + p[0], eval("plugins." + d + ".main." + p[1])))
            # if
            pgs.append(("/" + json['webname'] + p[0] + "/([^/]+)", eval("plugins." + d + ".main." + p[1])))

        pages.extend(pgs)

    print(pages)


    # start tornado sever



    app = web.Application(pages, debug=True)
    app.listen(9893)
    ioloop.IOLoop.instance().start()  # The program will never get past this. Put all code above.

    pass


startup()
