import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk

app = Tk()

class Application:
    def __init__(self):
        self.app = app
        self.config()
        self.frames()
        self.inputs_and_texts()
        self.treeview()
        self.buttons_and_options()
        app.mainloop()

    def config(self):
        self.app.title('Busca Vagas')
        self.app.state('zoomed')
        self.app.configure(background='#1d004d')

    def frames(self):
        self.frame1 = Frame(self.app, bg='#1d004d')
        self.frame1.place(relx=0.01, rely=0, relheight=0.2, relwidth=0.98)
        self.logo = PhotoImage(file='logo.png')
        self.logo_label = Label(self.app, image=self.logo, bg='#1d004d', anchor=W)
        self.logo_label.place(relx=0.3, rely=-0.05)
        self.frame2 = Frame(self.app, bg='#1d004d')
        self.frame2.place(relx=0.01, rely=0.21, relheight=0.2, relwidth=0.98)
        self.frame3 = Frame(self.app, bg='red')
        self.frame3.place(relx=0.01, rely=0.42, relheight=0.57, relwidth=0.98)

    def vagascom(self):
        lista_vagas = list()

        response = requests.get(
            'https://www.vagas.com.br/vagas-de-' + self.input_job.get() + '-em-' + self.input_city.get() + '?ordenar_por=mais_recentes')
        site = BeautifulSoup(response.text, 'html.parser')

        conteudo_vagas = site.findAll('header', attrs={'class': 'clearfix'})
        # print(conteudoVagas)

        for propostas in conteudo_vagas:
            # Título da vaga
            tituloVaga = propostas.find('h2', attrs={'class': 'cargo'})
            # print('Vaga: ', tituloVaga.text.strip())

            # Empresa
            empresaVaga = propostas.find('span', attrs={'class': 'emprVaga'})
            # print('Empresa: ', empresaVaga.text.strip())

            # Nível da Vaga
            nivelVaga = propostas.find('span', attrs={'class': 'nivelVaga'})
            # print('Nível: ', nivelVaga.text.strip())

            # Link da Vaga
            linkVaga = propostas.find('a', attrs={'class': 'link-detalhes-vaga'})
            # print(f"Link para candidatura: https://www.vagas.com.br{linkVaga['href']}")

            lista_vagas.append([tituloVaga.text.strip(), empresaVaga.text.strip(), nivelVaga.text.strip(),
                                f"https://www.vagas.com.br{linkVaga['href']}"])
            # print('')

        for i in lista_vagas:
            self.tabela.insert("", END, values=i)

    def inputs_and_texts(self):

        Label(self.frame2, text='Digite a vaga desejada:', bg='#1d004d', fg='white', font='Kollektif', anchor=W).place(relx=0.01, rely=0.3)
        Label(self.frame2, text='Digite a cidade:', bg='#1d004d', fg='white', font='Kollektif', anchor=W).place(relx=0.45, rely=0.3)
        self.input_job = Entry(self.frame2, font='Kollektif')
        self.input_job.place(relx=0.16, rely=0.3, width=400, height=25)
        self.input_city = Entry(self.frame2, font='Kollektif')
        self.input_city.place(relx=0.55, rely=0.3, width=400, height=25)

        # Progress Bar
        self.progress_bar = ttk.Progressbar(self.frame2, length=1000)
        self.progress_bar.place(relx=0.1, rely=0.7)

    def treeview(self):
        self.tabela = ttk.Treeview(self.frame3, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.tabela.heading('#0', text='')
        self.tabela.heading('#1', text='Título da Vaga')
        self.tabela.heading('#2', text='Empresa')
        self.tabela.heading('#3', text='Nível Exigido')
        self.tabela.heading('#4', text='Link da Vaga')

        self.tabela.column('#0', width=1, stretch=NO)
        self.tabela.column('#1', width=200)
        self.tabela.column('#2', width=25)
        self.tabela.column('#3', width=25)
        self.tabela.column('#4', width=250)

        self.tabela.place(relx=0, rely=0, relwidth=1, relheight=1)

    def remove_all(self):
        for record in self.tabela.get_children():
            self.tabela.delete(record)

    def buttons_and_options(self):
        # Button
        self.btn = Button(self.frame2, text='PESQUISAR', bg='#2fb4ae', fg='white', font='Kollektif',
                          command=self.vagascom)
        self.btn.place(relx=0.85, rely=0.2)

        self.btn_limpar = Button(self.frame2, text='LIMPAR', bg='#2fb4ae', fg='white', font='Kollektif', width=11,
                                 command=self.remove_all)
        self.btn_limpar.place(relx=0.85, rely=0.5)


Application()
