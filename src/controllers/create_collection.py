from pymongo import MongoClient
from config.conexao_mongodb import get_db

def create_collection():
    # Conectar ao MongoDB
    client = MongoClient('mongodb://localhost:27017/')

    # Selecionar o banco de dados
    db = client['Contatos']

    # Verificar se a coleção já existe
    get_db()
    if 'listaContatos' not in db.list_collection_names():
        # Criar a coleção
        db.create_collection('listaContatos')
        print("Coleção 'listaContatos' criada com sucesso!")
    else:
        print("A coleção 'listaContatos' já existe.")

if __name__ == "__main__":
    create_collection()