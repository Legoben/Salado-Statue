from tornado import web
import json

#morse code
print "MCode Imported"

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
    "Z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "10":"-----"
}

class SendCode(web.RequestHandler):
    def post(self, *args, **kwargs):
        self.set_header("Content-Type", "application/json")
        text = self.get_argument("text", None)
        if text == None:
            self.write(json.dumps({"error":True,"msg":"Text not found"}))
            return


        msg = ""
        for t in text:
            if t == " ":
                msg = msg.strip() + "\t"
            else:
                msg += code[t.upper()] + " "

        #ToDo: Do the lights
        self.write(json.dumps({"error":False, "msg":msg}))




#"/myroute"
class MyPage(web.RequestHandler):
    def get(self, *args, **kwargs):
        #Do the thing
        self.write("Hello World")
        print("It worked!!")

        pass
