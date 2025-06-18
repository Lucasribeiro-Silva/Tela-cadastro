from tkinter import *
from tkinter import messagebox, filedialog
import requests
from datetime import datetime

def limpar_dados():
    dados = [entrada_dados_idade, entrada_dados_nome, entrada_dados_telefone, entrada_dados_email, entrada_dados_endereco]
    for entrada in dados:
        entrada.delete(0, END)

    canvas.itemconfig(label_rua_id, text='')
    canvas.itemconfig(label_bairro_id, text='')
    canvas.itemconfig(label_cidade_id, text='')
    canvas.itemconfig(label_estado_id, text='')

dicionario_cliente = {}

def endereco_link(cep):
    link = f'https://viacep.com.br/ws/{cep}/json/'
    link_2 = requests.get(link)
    dados = link_2.json()

    if 'erro' in dados:
        messagebox.showerror('Erro', 'CEP não encontrado!')
        return None

    return {
        'rua': dados.get('logradouro', ''),
        'bairro': dados.get('bairro', ''),
        'cidade': dados.get('localidade', ''),
        'estado': dados.get('uf', '')
    }

def mostrar_endereco():
    cep = entrada_dados_endereco.get().strip()
    if cep == '':
        messagebox.showwarning('Aviso', 'Informe o CEP antes!')
        return

    cep_formatado = cep.replace('-', '').replace('.', '').replace(' ', '')

    if len(cep_formatado) != 8 or not cep_formatado.isdigit():
        messagebox.showerror('Erro!', 'CEP inválido! Deve conter 8 números.')
        return

    dados = endereco_link(cep_formatado)
    if dados:
        canvas.itemconfig(label_rua_id, text=f"Rua: {dados['rua']}")
        canvas.itemconfig(label_bairro_id, text=f"Bairro: {dados['bairro']}")
        canvas.itemconfig(label_cidade_id, text=f"Cidade: {dados['cidade']}")
        canvas.itemconfig(label_estado_id, text=f"Estado: {dados['estado']}")

def salvar_dados():
    nome = entrada_dados_nome.get().strip()
    idade = entrada_dados_idade.get().strip()
    telefone = entrada_dados_telefone.get().strip()
    email = entrada_dados_email.get().strip()
    endereco = entrada_dados_endereco.get().strip()

    if nome == '' or idade == '' or telefone == '' or email == '' or endereco == '':
        messagebox.showwarning('Aviso!', 'Campos vazios!!')
        return

    try:
        idade_int = int(idade)
        if idade_int <= 0 or idade_int > 120:
            raise ValueError
    except ValueError:
        messagebox.showerror('Erro!', 'Digite apenas números válidos em Idade!!')
        return

    try:
        telefone_limpo = telefone.replace('(','').replace(')','').replace('-','').replace(' ','')
        telefone_int = int(telefone_limpo)
        if len(telefone_limpo) != 11:
            messagebox.showerror('Erro!', 'Telefone inválido! Deve conter 11 números.')
            return
        
        if telefone_int < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror('Erro!', 'Digite apenas números válidos em Telefone!!')
        return

    if '@' not in email or '.' not in email:
        messagebox.showerror('Erro!', 'Email está errado!')
        return

    endereco_limpo = endereco.replace('-','').replace('.','').replace(' ','')
    if len(endereco_limpo) != 8 or not endereco_limpo.isdigit():
        messagebox.showerror('Erro!', 'CEP inválido! Deve conter 8 números.')
        return

    dicionario_cliente[nome] = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone,
        'email': email,
        'endereço': endereco
    }

    messagebox.showinfo('Cadastro clientes','Cadastro realizado com sucesso!!')
    print(dicionario_cliente)

def gerar_txt():
    if not dicionario_cliente:
        messagebox.showwarning("Aviso!","Não há elementos salvos!")
        return
    
    data_atual = datetime.now().strftime('%d-%m-%y') #Pegar data atual no formato brasileiro
    nome_arquivo = f'clientes_{data_atual}.txt'

    arquivo_cadastro = filedialog.asksaveasfilename(initialfile=nome_arquivo,
                                                  defaultextension='.txt',
                                                  filetypes=[('Arquivo de texto', '*.txt')])
    
    if arquivo_cadastro:
        with open(arquivo_cadastro, 'w', encoding='utf-8') as arq:
            for nome, dados in dicionario_cliente.items():
                arq.write(f"Nome: {dados['nome']}\n")
                arq.write(f"Idade: {dados['idade']}\n")
                arq.write(f"Telefone: {dados['telefone']}\n")
                arq.write(f"Email: {dados['email']}\n")
                arq.write(f"Endereço: {dados['endereço']}\n")
                arq.write("\n")

        messagebox.showinfo('Arquivo gerado com sucesso!', f'Arquivo salvo em:\n{arquivo_cadastro}')


# Cores padrão:

cor_entrada_fundo = '#f0f4f8'
cor_entrada_texto = '#2b2b2b'
cor_botao_fundo = '#d1d9e6'
cor_botao_texto = '#2b2b2b'

janela = Tk()
janela.geometry('800x500')
janela.title('Lógica de programação')

canvas = Canvas(janela, width=800, height=500)
canvas.pack(fill='both', expand=True)

try:
    imagem_fundo = PhotoImage(file='fundo.png')
    canvas.create_image(0, 0, image=imagem_fundo, anchor='nw')
except Exception:
    pass

# Título:

canvas.create_text(400, 30, text='Lógica de Programação', font=('Comic Sans MS',16),
                   fill='slategray1')

# Labels:

canvas.create_text(50, 130, text='Nome:', font=('Comic Sans MS',13), fill='#d1d9e6', anchor='w')
canvas.create_text(50, 180, text='Idade:', font=('Comic Sans MS',13), fill='#d1d9e6', anchor='w')
canvas.create_text(50, 230, text='Telefone:', font=('Comic Sans MS',13), fill='#d1d9e6', anchor='w')
canvas.create_text(50, 280, text='Email:', font=('Comic Sans MS',13), fill='#d1d9e6', anchor='w')
canvas.create_text(50, 330, text='Endereço (CEP):', font=('Comic Sans MS',13), fill='#d1d9e6', anchor='w')

# Entradas:

entrada_dados_nome = Entry(janela, bg=cor_entrada_fundo, fg=cor_entrada_texto)
canvas.create_window(200, 130, window=entrada_dados_nome, width=440, height=25, anchor='w')

entrada_dados_idade = Entry(janela, bg=cor_entrada_fundo, fg=cor_entrada_texto)
canvas.create_window(200, 180, window=entrada_dados_idade, width=80, height=25, anchor='w')

entrada_dados_telefone = Entry(janela, bg=cor_entrada_fundo, fg=cor_entrada_texto)
canvas.create_window(200, 230, window=entrada_dados_telefone, width=200, height=25, anchor='w')

entrada_dados_email = Entry(janela, bg=cor_entrada_fundo, fg=cor_entrada_texto)
canvas.create_window(200, 280, window=entrada_dados_email, width=260, height=25, anchor='w')

entrada_dados_endereco = Entry(janela, bg=cor_entrada_fundo, fg=cor_entrada_texto)
canvas.create_window(200, 330, window=entrada_dados_endereco, width=260, height=25, anchor='w')

label_rua_id = canvas.create_text(50, 380, text='', font=('Comic Sans MS',13), fill='#d1d9e6', anchor='w')
label_bairro_id = canvas.create_text(50, 405, text='', font=('Comic Sans MS',13), fill='#d1d9e6', anchor='w')
label_cidade_id = canvas.create_text(50, 430, text='', font=('Comic Sans MS',13), fill='#d1d9e6', anchor='w')
label_estado_id = canvas.create_text(50, 455, text='', font=('Comic Sans MS',13), fill='#d1d9e6', anchor='w')

# Botões:

botao_enviar = Button(janela, text='Salvar', bg=cor_botao_fundo, fg=cor_botao_texto, bd=2, command=salvar_dados)
canvas.create_window(320, 90, window=botao_enviar, width=100, height=30)

botao_limpar = Button(janela, text='Limpar', bg=cor_botao_fundo, fg=cor_botao_texto, bd=2, command=limpar_dados)
canvas.create_window(430, 90, window=botao_limpar, width=100, height=30)

botao_buscar_cep = Button(janela, text='Buscar CEP', bg=cor_botao_fundo, fg=cor_botao_texto, bd=2, command=mostrar_endereco)
canvas.create_window(480, 330, window=botao_buscar_cep, width=90, height=25)

botao_gerar_txt = Button(janela, text='Gerar TXT', bg=cor_botao_fundo, fg=cor_botao_texto, bd=2, command=gerar_txt)
canvas.create_window(540, 90, window=botao_gerar_txt, width=100, height=30)

janela.mainloop()
