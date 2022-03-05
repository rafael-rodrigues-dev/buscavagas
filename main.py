import requests
from bs4 import BeautifulSoup
from time import sleep
from tkinter import *
import pandas as pd
from datetime import date


def validar():
    if var_vagascom.get() == 1:
        vagascom(input_job.get(), input_city.get())
    if var_indeed.get() == 1:
        indeed(input_job.get(), input_city.get())


def vagascom(vaga, cidade):
    lista_vagas = list()

    response = requests.get('https://www.vagas.com.br/vagas-de-' + vaga + '-em-' + cidade + '?ordenar_por=mais_recentes')
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

    file_excel = pd.DataFrame(lista_vagas, columns=('Título da Vaga', 'Empresa', 'Nivel exigido', 'Link da vaga'))
    file_excel.to_excel(f'vagas-{date.today()}.xlsx', index=False)
    print(file_excel)


def indeed(vaga, cidade):
    # Configurando o WebDriver
    browser = webdriver.Firefox(options=options)
    browser.get(f'https://br.indeed.com/jobs?q={vaga}&l={cidade}&sort=date')

    sleep(3)

    # Botão de cookies navegador
    cookies = browser.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

    page_content = browser.page_source
    site = BeautifulSoup(page_content, 'html.parser')
    vagas = site.findAll('div', attrs={'class': 'job_seen_beacon'})

    # Coletando os dados
    for vaga in vagas:
        # Titulo da Vaga
        titulo_vaga = browser.find_element_by_css_selector('div > h2 > span')
        print('Vaga: ', titulo_vaga.text)

        # Empresa
        empresa = vaga.find('span', attrs={'class': 'companyName'})
        if empresa:
            print('Empresa: ', empresa.text)
        else:
            print('Não informado')

        # Data da Postagem
        data_postagem = vaga.find('span', attrs={'class': 'date'})
        print('Data da postagem: ', data_postagem.text)

        # Salário
        salario = vaga.find('span', attrs={'class': 'salary-snippet'})
        if salario:
            print('Salário: ', salario.text)
        else:
            print('Não informado')
        print()


# Interface Gráfica (Tkinter)
app = Tk()



# # Logo
# logo = PhotoImage(file='logo.png')
# logo_label = Label(app, image=logo, bg='#1d004d', anchor=W)
# logo_label.place(x=0, y=-30)

# Texts and inputs
Label(app, text='Digite a vaga desejada:', bg='#1d004d', fg='white', font='Kollektif', anchor=W).place(relx=0.1, rely=0.3)
Label(app, text='Digite a cidade:', bg='#1d004d', fg='white', font='Kollektif', anchor=W).place(relx=0.5, rely=0.3)
input_job = Entry(app, font='Kollektif')
input_job.place(relx=0.22, rely=0.3, width=400, height=25)
input_city = Entry(app, font='Kollektif')
input_city.place(relx=0.6, rely=0.3, width=400, height=25)

# Checkbox Vagas.com
var_vagascom = IntVar()
checkbox_vagascom = Checkbutton(app, text='Vagas.com', bg='#1d004d', fg='white', activebackground='#1d004d', activeforeground='white',
                       selectcolor='#2fb4ae', font='Kollektif', variable=var_vagascom, onvalue=1, offvalue=0)
checkbox_vagascom.place(x=40, y=330)

# Checkbox Indeed
var_indeed = IntVar()
checkbox_indeed = Checkbutton(app, text='Indeed', bg='#1d004d', fg='white', activebackground='#1d004d', activeforeground='white',
                       selectcolor='#2fb4ae', font='Kollektif', variable=var_indeed, onvalue=1, offvalue=0)
checkbox_indeed.place(x=200, y=330)

# Button
btn = Button(app, text='BUSCAR AGORA!', bg='#2fb4ae', fg='white', font='Kollektif', command=validar)
btn.place(x=175, y=400)


class Application:
    def __init__(self):
        self.app = app
        self.config()
        app.mainloop()

    def config(self):
        self.app.title('Busca Vagas')
        self.app.attributes('-zoomed', True)
        self.app.configure(background='#1d004d')



Application()