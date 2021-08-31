from tkinter import *
from add_func import *

PASSWORD = "1"
LARGE_FONT = ("Verdana", 13)
BUTTON_FONT = ("Batang", 13, "bold")

class Login(Tk):
    """docstring for Login"""

    def __init__(self, *args):
        Tk.__init__(self, *args)

        Tk.wm_title(self, "Password Manager")
        self.state = {
            "text": "Login to access password database.", "valid_user": False
        }

        self.addLoginFrame()

        # Adding frames

    def addLoginFrame(self, *kwargs):
        login = Frame(self, padx=2, pady=2, bd=2)
        login.pack()

        #loginLabel = Label(login, text=self.state['text'],bd=10, width=30)
        loginLabel = Label(login, text="Please input your password", bd=10, font=LARGE_FONT, width=30)
        loginLabel.grid(row=0, columnspan=3)

        entry = Entry(login, show="*")
        entry.config(cursor='pencil', bd=10, relief=GROOVE)
        entry.grid(row=1, column=1, pady=3)
        # _ marks an unused variable; used for lambda compatibility
        # Bind event for when enter is pressed in the Entry
        entry.bind('<Return>', lambda _: self.checkPwd(
            login, label=loginLabel, entry=entry, btn=submitBtn))
        entry.focus_set()

        submitBtn = Button(login, text="Submit",
                               command=lambda: self.checkPwd(
                                   login, label=loginLabel, entry=entry,
                                   btn=submitBtn))
        submitBtn.config(bd=10, relief=RAISED)
        submitBtn.grid(row=2, column=1, pady=3)

    """Kwargs = loginLabel, password entry, and submit button"""

    def checkPwd(self, frame, **kwargs):
        chk = kwargs['entry'].get()
        # if passwords match
        #we save the login password in the login_pwd.txt
        password = open("login_pwd.txt", "r").read()
        in_pwd = kwargs['entry'].get()
        if chk == PASSWORD:

            self.state['text'] = "Logged In"
            self.state['valid_user'] = True
            # Using .config() to modift the args
            kwargs['label'].config(text=self.state['text'])
            kwargs['entry'].config(state=DISABLED)
            kwargs['btn'].config(state=DISABLED)

            # adding buttons
            self.addConfigBtn(frame)
            #self.addlistBtn(frame)

        # If passwords don't match
        else:
            #kwargs['label'].config(text=self.state['text'] + "\nTry Again!!!")
            kwargs['label'].config(text="Password don't match!!\nTry Again!!!")
            kwargs['label'].config(bd=10, font=("Verdana", 11), fg="red")
            # errorLabel.grid(row=4, column=1, pady=3)


    def addConfigBtn(self, login):
        # configured buttons
        # btnList = (addBtn, listBtn, getBtn)

        # Creating temp references to images using temp1,2 so as to disallow
        # garbage collection problems
        btnList = ["Add", "List"]
        btnCmdList = [lambda: addScreen(self),
                      lambda: List.ListWindow(self)]
        f = []  # Frames array
        img = []  # image array
        self.temp = []  # temp array

        for i in range(2):
            f.append(Frame(login, padx=2, width=200, height=100))
            f[i].grid(row=3, column=i)
            img.append(PhotoImage(
                file=btnList[i] + ".gif", width=70, height=90))
            self.temp.append(img[i])
            Button(f[i], image=img[i], text=btnList[i],
                   command=btnCmdList[i]).grid(row=3,column = i)


if __name__ == '__main__':
    new = Login()
    new.mainloop()
