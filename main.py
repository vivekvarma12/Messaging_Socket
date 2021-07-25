from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk as itk
import socket
import threading
import time

init = tk.Tk()
init.geometry("300x500")
init.config(bg="white")
init.title("Server")

def init_func():
    t1 = threading.Thread(target=recv)
    t1.start()

def recv():
    l = socket.socket()
    port = 5000
    max_con = 9
    ip = socket.gethostname()
    l.bind(('', port))
    l.listen(max_con)
    (clientsocket, address) = l.accept()
    while True:
        send_msg = clientsocket.recv(1024).decode()
        if not send_msg == "":
            time.sleep(2)
            lst_box.insert(0,"Vivek : "+send_msg)

g = 0

def send_msg():
    global g, g1
    if g == 0 :
        g1 = socket.socket()
        hostname = socket.gethostname()
        print(hostname)
        port = 3050
        g1.connect((hostname, port))
        msg = msg_box.get()
        lst_box.insert(g, "Server :"+msg)
        g1.send(msg.encode())
        g+=1

    else:
        print("g1 value --> {}".format(g))
        msg = msg_box().get()
        lst_box.insert(g, "Server :"+msg)
        g1.send(msg.encode())
        g+=1


def thread_send():
    t = threading.Thread(target=send_msg)
    t.start()

#Session to create
start_chat = Image.open('start.png')
start_chat = start_chat.resize((80, 50), Image.ANTIALIAS)
start_chat = itk.PhotoImage(start_chat)
bu = Button(init, image=start_chat, command=init_func, borderwidth=2)
bu.place(x=110, y=10)

#list of msgs here
lst_box = Listbox(init, height=20, width=43)
lst_box.place(x=15, y=80)

#msg field, user will give input here
msg = tk.StringVar()

msg_box = Entry(init, textvariable=msg, font=('TimesNewRoman',12,'italic'), border=2, width=23)
msg_box.place(x=15, y=420)

#sending msg after clicking this button
send_img = Image.open('send.png')
send_img = send_img.resize((30, 25), Image.ANTIALIAS)
send_img = itk.PhotoImage(send_img)
send_img_but = Button(init, image=send_img, command=thread_send, borderwidth=1)
send_img_but.place(x=240, y=415)
init.mainloop()