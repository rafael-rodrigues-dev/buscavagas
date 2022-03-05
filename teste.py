import requests
from bs4 import BeautifulSoup
from time import sleep
from tkinter import *
import pandas as pd
from datetime import date

app = Tk()

class Application:
    def __init__(self):
        self.app = app
        self.config()
        self.frames()
        self.inputs_and_texts()
        app.mainloop()

    def config(self):
        self.app.title('Busca Vagas')
        self.app.attributes('-zoomed', True)
        self.app.configure(background='white')

    def frames(self):
        self.frame1 = Frame(self.app, bg='#1d004d')
        self.frame1.place(relx=0.01, rely=0, relheight=0.2, relwidth=0.98)
        self.frame2 = Frame(self.app, bg='#1d004d')
        self.frame2.place(relx=0.01, rely=0.21, relheight=0.2, relwidth=0.98)
        self.frame3 = Frame(self.app, bg='red')
        self.frame3.place(relx=0.01, rely=0.42, relheight=0.57, relwidth=0.98)

    def inputs_and_texts(self):

        Label(self.frame2, text='Digite a vaga desejada:', bg='#1d004d', fg='white', font='Kollektif', anchor=W).place(relx=0.1,
                                                                                                               rely=0.3)
        Label(self.frame2, text='Digite a cidade:', bg='#1d004d', fg='white', font='Kollektif', anchor=W).place(relx=0.5,
                                                                                                        rely=0.3)
        self.input_job = Entry(self.frame2, font='Kollektif')
        self.input_job.place(relx=0.22, rely=0.3, width=400, height=25)
        self.input_city = Entry(self.frame2, font='Kollektif')
        self.input_city.place(relx=0.6, rely=0.3, width=400, height=25)

        # Button
        btn = Button(self.frame2, text='BUSCAR AGORA!', bg='#2fb4ae', fg='white', font='Kollektif')
        btn.place(relx=0.4, rely=0.6)




Application()