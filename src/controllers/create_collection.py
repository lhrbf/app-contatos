from pymongo import MongoClient
from config.conexao_mongodb import get_db

def create_collection():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['Contatos']

    get_db()
    if 'listaContatos' not in db.list_collection_names():
        # Criar a coleção
        db.create_collection('listaContatos')
        print("Coleção 'listaContatos' criada com sucesso!")
    else:
        print("A coleção 'listaContatos' já existe.")

if __name__ == "__main__":
    create_collection()
