# App Contatos

Um aplicativo simples para gerenciar uma lista de contatos. O projeto foi desenvolvido em Python usando Flask e MongoDB.

## Funcionalidades

- Adicionar contatos
- Editar contatos
- Excluir contatos
- Visualizar lista de contatos

## Tecnologias Utilizadas

- [Python](https://www.python.org/) 
- [Flask](https://flask.palletsprojects.com/) 
- [MongoDB](https://www.mongodb.com/)
- [Bootstrap](https://getbootstrap.com/) para o design responsivo
- [jQuery](https://jquery.com/) para manipulação de DOM

## Estrutura do Projeto

app-contatos/ ├── src/ │ ├── config/ │ │ └── conexao_mongodb.py │ ├── controllers/ │ │ └── create_collection.py │ ├── models/ │ │ └── dicionario.py │ ├── services/ │ │ └── crud.py │ ├── templates/ │ │ └── index.html │ └── app.py


## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **Flask**: Microframework para desenvolvimento web.
- **MongoDB**: Banco de dados NoSQL utilizado para armazenar os contatos.
- **Bootstrap**: Framework CSS para estilização da interface.

## Como Usar

1. **Clone o repositório**:
   ```bash
   git clone <URL do repositório>
   cd app-contatos

2. **Instale as dependências:**
 Certifique-se de ter o Python e o MongoDB instalados em sua máquina. Em seguida, instale as dependências necessárias:
    ```bash
    pip install flask pymongo

3. **Configure a conexão com o MongoDB:**
Edite o arquivo config/conexao_mongodb.py para incluir suas credenciais do MongoDB.

4. **Execute o aplicativo:**
    ```bash
    python src/app.py

5. **Acesse o aplicativo:** Abra um navegador e vá para http://127.0.0.1:5000/.

Funcionalidades
Adicionar novos contatos.
Editar contatos existentes.
Excluir contatos.
Visualizar a lista de contatos.
Contribuição
Sinta-se à vontade para contribuir com o projeto! Faça um fork deste repositório, faça suas alterações e envie um pull request.

## Licença
   ```bash
   Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

   ```bash
   Sinta-se à vontade para ajustar qualquer parte do texto conforme necessário!
