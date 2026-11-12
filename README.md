# API de Upload e Download de Arquivos

Esse projeto é uma API feita em Python usando Flask. Ela serve para enviar arquivos para o servidor e depois permitir que eles sejam baixados.

A API também verifica o tipo e o tamanho dos arquivos antes de aceitar o envio. Além disso, registra as tentativas de upload em um arquivo de log.

## Tecnologias utilizadas

- Python
- Flask
- SQLite (banco de dados)
- Gunicorn
- Render (para hospedar a API)

## Estrutura do projeto

O projeto está organizado da seguinte maneira:

```text
├── app.py
├── controllers/
├── models/
├── routes/
├── database/db.py
├── uploads/
├── requirements.txt
└── render.yaml
```

Cada pasta tem uma função:

- **app.py:** inicia a aplicação.
- **controllers:** contém as funções de upload e download.
- **models:** parte responsável pelo banco de dados.
- **routes:** contém os caminhos da API.
- **database:** faz a conexão com o SQLite.
- **uploads:** pasta onde os arquivos enviados ficam salvos.
- **requirements.txt:** lista as bibliotecas utilizadas.
- **render.yaml:** configura a hospedagem no Render.

## Como executar o projeto

Para rodar a API no computador, primeiro é necessário abrir o terminal na pasta do projeto.

Depois, execute os comandos:

```bash
# Criar ambiente virtual (opcional)
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Instalar as bibliotecas
pip install -r requirements.txt

# Iniciar a API
python app.py
```

Depois disso, a API ficará disponível no endereço:

`http://127.0.0.1:5000`

## Rotas da API

A API possui três rotas principais:

| Método | Rota | Função |
|---|---|---|
| GET | `/` | Verifica se a API está funcionando |
| POST | `/uploads/upload` | Envia um arquivo |
| GET | `/downloads/download/<filename>` | Baixa um arquivo |

## Envio de arquivos (Upload)

Para enviar um arquivo, é necessário utilizar o método POST no endereço:

`/uploads/upload`

O envio é feito usando o formato `form-data`, com o campo chamado `file`.

A API aceita os seguintes formatos:

- PNG
- JPG
- JPEG
- GIF
- PDF
- TXT

O tamanho máximo permitido é de 30 KB.

Se o arquivo estiver dentro dessas condições, ele será salvo na pasta `uploads`.

Caso tenha algum problema, a API retorna uma mensagem explicando o erro.

## Baixar arquivos (Download)

Para baixar um arquivo que já foi enviado, é necessário utilizar o método GET.

O endereço segue este formato:

`/downloads/download/nome_do_arquivo`

Por exemplo:

`http://127.0.0.1:5000/downloads/download/teste.txt`

Se o arquivo existir, ele será enviado para download. Caso contrário, a API retorna uma mensagem informando que ele não foi encontrado.

## Como testar no Postman

Utilizei o Postman para testar as rotas da API.

**Para testar o upload:**

1. Selecionar o método POST.
2. Colocar o endereço `/uploads/upload`.
3. Entrar na aba Body.
4. Selecionar form-data.
5. Criar uma chave chamada `file`.
6. Mudar o tipo de Text para File.
7. Escolher um arquivo e clicar em Send.

**Para testar o download:**

1. Selecionar o método GET.
2. Colocar o endereço `/downloads/download/nome_do_arquivo`.
3. Clicar em Send para receber o arquivo.

## Hospedagem no Render

O projeto também possui configuração para ser hospedado no Render.

As configurações utilizadas são:

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

O arquivo `render.yaml` contém essas configurações.

Uma observação é que, no plano gratuito do Render, os arquivos salvos podem ser apagados quando o serviço reinicia ou é atualizado. Por isso, os arquivos enviados e o banco de dados não ficam armazenados permanentemente.

Além disso, o serviço pode ficar inativo depois de um tempo sem uso, fazendo com que a primeira requisição demore um pouco mais.

## Registro de logs

A API também possui um arquivo chamado `uploads.log`.

Nele ficam registradas as tentativas de envio de arquivos, tanto as que deram certo quanto as que apresentaram algum erro.

São registrados dados como a data, o nome do arquivo e o endereço IP de quem fez a tentativa.