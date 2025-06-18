
• 📝 Cadastro de Clientes (com Tkinter + ViaCEP)

Projeto desenvolvido durante o curso de **Análise e Desenvolvimento de Sistemas** (SENAI Curitiba).

• 💡 Sobre o projeto

Aplicação desktop com interface gráfica feita em Python usando **Tkinter**, que permite realizar o cadastro de clientes. O sistema busca automaticamente o endereço através do **CEP**, integrando com a API gratuita do [ViaCEP](https://viacep.com.br).

• Funcionalidades:
- Cadastro de nome, idade, telefone, e-mail e endereço
- Busca automática do endereço via CEP (logradouro, bairro, cidade, estado)
- Validação de campos e exibição de mensagens de erro
- Limpeza de todos os campos com um clique
- Exportação dos dados para um arquivo `.txt`

---

• 🛠️ Tecnologias e ferramentas

- Python 3
- Tkinter (GUI)
- API ViaCEP
- Requests (requisições HTTP)

---

• 📁 Estrutura do projeto

```
Cadastro/
│
├── tela.py              # Código-fonte principal da aplicação
├── fundo.png            # Imagem usada como plano de fundo da interface
├── tela.exe             # Executável gerado (versão desktop)
└── README.md            # Documentação do projeto
```

---

• 🚀 Como executar (modo desenvolvedor)

1. Instale o Python 3
2. Instale as dependências:
   ```bash
   pip install requests pillow
   ```
3. Execute o arquivo `tela.py`:
   ```bash
   python tela.py
   ```

---

• 👨‍💻 Autor

**Lucas Ribeiro da Silva**  
Estudante de ADS – SENAI Curitiba  
[GitHub @Lucasribeiro-Silva](https://github.com/Lucasribeiro-Silva)
