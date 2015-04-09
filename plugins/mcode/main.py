from tornado import web


#morse code
print "Hello World"

code = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":".-",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":"._.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--.."
}

class SendCode(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_header("Content-Type", "application/json")
        text = self.get_argument("text", None)
        if text == None:
            self.write("")
            return



#"/myroute"
class MyPage(web.RequestHandler):
    def get(self, *args, **kwargs):
        #Do the thing
        self.write("Hello World")
        print("It worked!!")

        pass
