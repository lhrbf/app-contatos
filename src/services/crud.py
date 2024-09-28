from pymongo import MongoClient
from bson import ObjectId
from config.conexao_mongodb import get_db

db = get_db()
collection = db['contatos']

def create_contact(nome, numero):
    contato = {
        "nome": nome,
        "numero": numero
    }
    result = collection.insert_one(contato)
    return str(result.inserted_id)

def read_contacts():
    return list(collection.find())

def update_contact(contato_id, novo_nome, novo_numero):
    result = collection.update_one(
        {"_id": ObjectId(contato_id)},
        {"$set": {"nome": novo_nome, "numero": novo_numero}}
    )
    return result.modified_count

def delete_contact(contato_id):
    result = collection.delete_one({"_id": ObjectId(contato_id)})
    return result.deleted_count