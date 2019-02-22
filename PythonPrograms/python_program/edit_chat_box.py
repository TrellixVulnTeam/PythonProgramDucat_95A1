from pymysql import *
from tkinter import *
import socket
import threading
# from dashboard import dashboard
from tkinter import messagebox as ms


class ChatBox:
    send_to_client = 0
    receive_by_client = 0
    con = connect(db='tkinter', user='root', password='', host='localhost')
    cur = con.cursor()

    def __init__(self):
        pass

    def is_not_used(self):
        pass

    '''def print_conversation(self):
        self.is_not_used()

        f_conversation = Tk()
        f_conversation.minsize(width=300, height=600)
        f_conversation.maxsize(width=300, height=600)

        f_conversation.title("Chatting")'''

    def server_frame(self, name):
        self.is_not_used()

        def make_server():
            server_button.config(state=DISABLED)
            # f_server.destroy()
            # print("destroy server frame for making server")

            print(server_name)
            create_server()

        def create_server():
            def sign_out():
                f_server.destroy()
                print("destroy server frame")
                ser_sock.close()
                start.login()

            def accept_client():
                while True:
                    # accept
                    cli_sock, cli_add = ser_sock.accept()
                    uname = cli_sock.recv(1024)
                    connections_list.append((uname, cli_sock))
                    print('%s is now connected' % uname)
                    # txt_area = Text(f_server, text=uname) when we used this they running infinite loop
                    # txt_area.place(x=100, y=190)
                    thread_client = threading.Thread(target=broadcast_usr, args=[uname, cli_sock])
                    thread_client.start()

            def broadcast_usr(uname, cli_sock):
                while True:
                    try:
                        data = cli_sock.recv(1024)
                        if data:
                            print("{0}spoke".format(uname))
                            b_usr(cli_sock, uname, data)
                    except Exception as x:
                        print(x)
                        break

            def b_usr(cs_sock, sen_name, msg):
                for client in connections_list:
                    if client[1] != cs_sock:
                        client[1].send(sen_name)
                        client[1].send(msg)

            if __name__ == "__main__":
                connections_list = []
                ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                hostname = socket.gethostname()
                ip_add = socket.gethostbyname(hostname)
                host = ip_add
                port = 50243
                ser_sock.bind((host, port))
                ser_sock.listen(1)
                print("Server Started")
                print('Chat server started on port : ' + str(port))
                thread_ac = threading.Thread(target=accept_client)
                thread_ac.start()
                # thread_bs = threading.Thread(target = broadcast_usr)
                # thread_bs.start()

                ms.showinfo('Server Status', "Server Running")

            Button(f_server, text='Sign out', fg='blue', command=sign_out).place(x=230, y=25)

        print("Now in client frame")
        global cur
        global con
        con = connect(db='tkinter', user='root', password='', host='localhost')
        cur = con.cursor()
        login_person_name = name
        print(login_person_name)

        f_server = Tk()
        f_server.minsize(width=300, height=300)
        f_server.maxsize(width=300, height=300)
        f_server.title("Server")

        txt_welcome = Label(f_server, text="Welcome", font=("bold", 20))
        txt_welcome.pack()

        txt_login = Label(f_server, text="Name : ", font=("bold", 8))
        txt_login.place(x=220, y=5)

        login_name = Label(f_server, text=login_person_name, font=("bold", 8))
        login_name.place(x=250, y=5)

        txt_server_name = Label(f_server, text="Server Name")
        txt_server_name.place(x=40, y=90)
        server_name_entry = Entry(f_server).place(x=125, y=90)

        server_name = server_name_entry
        print(server_name)

        # Button(f_server, text='Sign out', fg='blue', command=sign_out).place(x=230, y=25)
        server_button = Button(f_server, text="Create Server", command=make_server)
        server_button.place(x=100, y=170)

    def client_frame(self):
        self.is_not_used()

        def home():
            f_client.destroy()
            print("destroy client frame")
            start.index()

        def connect_to_server():
            mk.config(state=DISABLED)
            # f_client.destroy()
            print("destroy client frame")
            uname = client_name_entry.get()
            print(uname)
            # start.create_client(name_send)

            # ------------Start chat input and output---------------------

            def client_logout():
                print('In the chat input and output frame')
                f_chat_input_output.destroy()
                print("Destroy chat input and output frame")
                cli_sock.close()
                start.index()

            def send():
                global send_to_client
                while True:
                    msg = input('\nMe > ')
                    cli_sock.send(msg.encode())
                    send_to_client = cli_sock
                    # print(send_to_client)

            def receive():
                while True:
                    sen_name = cli_sock.recv(1024)
                    data = cli_sock.recv(1024)
                    print('\n' + str(sen_name) + ' > ' + str(data))
                    '''text_sen_name = Label(f_client, text=sen_name)
                    text_sen_name.place(x=100, y=210)

                    text_data = Label(f_client, text=data)
                    text_data.place(x=100, y=230)'''

            if __name__ == "__main__":
                cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # HOST = 'localhost'
                # PORT = 50243
                hostname = socket.gethostname()
                ip_add = socket.gethostbyname(hostname)
                host = ip_add
                port = 50243
                cli_sock.connect((host, port))
                print('Connected to remote host...')
                # uname = input('Enter your name to enter the chat > ')
                # uname = client
                cli_sock.send(uname.encode())
                Label(f_client, text=uname).place(x=100, y=190)
                thread_send = threading.Thread(target=send)
                thread_send.start()
                thread_receive = threading.Thread(target=receive)
                thread_receive.start()

            f_chat_input_output = Tk()
            # print(send_to_client)
            f_chat_input_output.minsize(width=350, height=500)
            f_chat_input_output.maxsize(width=350, height=500)

            Label(f_chat_input_output, text='').pack()  # for space
            Button(f_chat_input_output, text='Logout', command=client_logout).pack()

            Label(f_chat_input_output, text='').pack()  # for space
            Label(f_chat_input_output, text="Welcome "+uname, font='bold').pack()
            Label(f_chat_input_output, text='').pack()  # for space
            Label(f_chat_input_output, text='').pack()  # for space

            chat_type_input = Entry(f_chat_input_output)
            chat_type_input.pack()

            scrollbar = Scrollbar(f_chat_input_output)
            scrollbar.pack(side=RIGHT, fill=Y)

            def send_to_client():
                Label(f_chat_input_output, text='').pack()  # for space
                Label(f_chat_input_output, text='').pack()  # for space
                chat_value = chat_type_input.get()
                # chat_print_box = Text(f_chat_input_output)
                # chat_print_box.pack()


                chat_print = Label(f_chat_input_output, text=chat_value)
                chat_print.pack()
                # chat_print.config(yscrollcommand=scrollbar.set)
                # scrollbar.config(command=chat_print.yview)

            # chat_input.place(x=40, y=40)
            Label(f_chat_input_output, text='').pack()  # for space
            send_button = Button(f_chat_input_output, text="Send", command=send_to_client)
            send_button.pack()

            # ------------close chat input and output---------------------

        print("Now in client frame")
        global cur
        global con
        con = connect(db='tkinter', user='root', password='', host='localhost')
        cur = con.cursor()

    # ------------start client frame---------------------

        f_client = Tk()
        f_client.minsize(width=300, height=300)
        f_client.maxsize(width=300, height=300)
        f_client.title("Client")

        txt_welcome = Label(f_client, text="Welcome", font=("bold", 20))
        txt_welcome.pack()

        client_name = Label(f_client, text="Name")
        client_name.place(x=60, y=70)
        client_name_entry = Entry(f_client)
        client_name_entry.place(x=110, y=70)

        # name_send = client_name_entry

        Button(f_client, text="Home", fg='blue', command=home).place(x=245, y=5)
        mk = Button(f_client, text="Start Talking", command=connect_to_server)
        mk.place(x=100, y=140)

    # ------------close client frame---------------------

    def login(self):
        self.is_not_used()

        def check_for_login():
            global cur
            global con
            con = connect(db='tkinter', user='root', password='', host='localhost')
            cur = con.cursor()

            cur.execute("SELECT firstname, email FROM record WHERE email='%s'" % (txt2.get()))
            result = cur.fetchone()
            # print(result)

            if result[0] == txt1.get() and result[1] == txt2.get():
                print("Login success")
                login_person_name = result[0]
                f_login.destroy()
                start.server_frame(login_person_name)
            else:
                print("Invalid Login")
                ms.showinfo("login", "Invalid Login")
            # ms.showinfo("login", "You are Login")

        def demo_registration():
            f_login.destroy()
            print("destroy login frame")
            start.registration()

        def go_home():
            f_login.destroy()
            print("destroy login frame")
            start.index()

        print("Now in login frame")
        f_login = Tk()
        # f_login.geometry("300x200")
        f_login.maxsize(width=300, height=250)
        f_login.minsize(width=300, height=250)
        f_login.title("Login Panel")

        lb = Label(f_login, text="Server Login", font=("bold", 15))
        lb.place(x=100, y=20)

        l1 = Label(f_login, text="First Name")
        l1.place(x=30, y=60)
        txt1 = Entry(f_login)
        txt1.place(x=120, y=60)

        l2 = Label(f_login, text="Email")
        l2.place(x=60, y=90)
        txt2 = Entry(f_login)
        txt2.place(x=120, y=90)

        Button(f_login, text="Home", fg='blue', command=go_home).place(x=240, y=5)
        Button(f_login, text="Login", bg='Green', fg='Black', command=check_for_login).place(x=70, y=150)
        Button(f_login, text="REGISTRATION", bg='Green', fg='Black', command=demo_registration).place(x=120, y=150)

    def registration(self):
        self.is_not_used()
        # save records in the database

        def record():
            global cur
            global con
            con = connect(db='tkinter', user='root', password='', host='localhost')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES('%s','%s','%s','%s','%s','%s')" % (input_first_name.get(),
                                                                                      input_last_name.get(),
                                                                                      input_phone.get(),
                                                                                      input_gender.get(),
                                                                                      input_email.get(),
                                                                                      input_city.get()))
            ms.showinfo('Record', "Data Entered")

        def demo_login():
            print("destroy registration frame")
            form.destroy()
            start.login()

        def go_home():
            form.destroy()
            print("destroy registration frame")
            start.index()

        # registration form GUI start
        print("Now in registration frame")
        form = Tk()
        # form.geometry("500x500")
        form.maxsize(width=500, height=500)
        form.minsize(width=500, height=500)
        form.title("Registration Form")

        headline = Label(form, text="Registration", font=("bold", 20))
        headline.place(x=180, y=25)

        first_name = Label(form, text="First Name", font=("bold", 12))
        first_name.place(x=130, y=80)
        input_first_name = Entry(form)
        input_first_name.place(x=250, y=80)

        last_name = Label(form, text="Last Name", font=("bold", 12))
        last_name.place(x=130, y=110)
        input_last_name = Entry(form)
        input_last_name.place(x=250, y=110)

        phone = Label(form, text="Phone", font=("bold", 12))
        phone.place(x=130, y=140)
        input_phone = Entry(form)
        input_phone.place(x=250, y=140)

        gender = Label(form, text="Gender", font=("bold", 12))
        gender.place(x=130, y=170)
        input_gender = Entry(form)
        input_gender.place(x=250, y=170)

        email = Label(form, text="Email", font=("bold", 12))
        email.place(x=130, y=200)
        input_email = Entry(form)
        input_email.place(x=250, y=200)

        city = Label(form, text="City", font=("bold", 12))
        city.place(x=130, y=230)
        input_city = Entry(form)
        input_city.place(x=250, y=230)

        Button(form, text="Home", fg='blue', command=go_home).place(x=450, y=5)
        Button(form, text="Save", bg='Green', fg='Black', command=record).place(x=200, y=280)
        Button(form, text="Login", bg='Green', fg='Black', command=demo_login).place(x=250, y=280)

        form.mainloop()

        # registration form GUI end

    def index(self):

        def click_server():
            print("now in index")
            main_frame.destroy()
            print("Destroy main frame")
            start.login()

        def client_server():
            main_frame.destroy()
            print("Destroy main frame")
            start.client_frame()
        self.is_not_used()
        print("Now in index frame")
        main_frame = Tk()
        # main_frame.geometry("600x500")
        main_frame.minsize(width=350, height=300)
        main_frame.maxsize(width=350, height=300)

        Button(main_frame, text='Server', font=("bold", 20), command=click_server).place(x=130, y=50)
        Button(main_frame, text='Client', font=("bold", 23), command=client_server).place(x=130, y=120)

        main_frame.mainloop()


start = ChatBox()
start.index()
