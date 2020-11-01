import eel
from bs4 import BeautifulSoup as BS
import requests
import database
import cv2
import os
eel.init('web')


@eel.expose
def fm():
    os.system("python calci.py")

@eel.expose
def exam():
    examval = "a!B2"
    examcode = "a!B5"
    examstime = "a!B3"
    exametime = "a!B4"
    a = ""
    a = a+" "+str(database.read(examval)[0])
    a = a+" "+str(database.read(examcode)[0])
    a = a+" "+str(database.read(examstime)[0])
    a = a+" "+str(database.read(exametime)[0])
    print(a)
    return a


@eel.expose
def login(mail, passwd, code):
    print(mail, passwd, code)
    a = []
    a.append(mail)
    b = []
    b.append(passwd)
    c = []
    c.append(code)
    cnt = 14
    number = 0
    for i in range(0, 10):
        k = "a!B"+str(cnt)
        n = database.read(k)
        r = "a!G"+str(cnt)
        h = database.read(r)
        codeval = "a!B5"
        code = database.read(codeval)
        if a == n:
            number = cnt
            if b == h:
                number = cnt
                if c == code:
                    print("Succes")
                    return "Success"
        cnt = cnt+1


eel.start('index.html',  port=8081, size=(650, 612))  # ),mode='chrome-app',
# cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])
