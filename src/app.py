from flask import Flask, render_template, request, jsonify
from services.crud import create_contact, read_contacts, update_contact, delete_contact

app = Flask(__name__)

@app.route('/')
def index():
    contatos = read_contacts()
    return render_template('index.html', contacts=contatos)

@app.route('/add-contact', methods=['POST'])
def add_contact():
    nome = request.form['nome']
    numero = request.form['numero']
    create_contact(nome, numero)
    return jsonify(success=True)

@app.route('/edit-contact', methods=['POST'])
def update_contact_route():
    contato_id = request.form.get('id')
    novo_nome = request.form.get('nome')
    novo_numero = request.form.get('numero')
    success = update_contact(contato_id, novo_nome, novo_numero)
    return jsonify(success=success)  # Retornando um JSON

@app.route('/delete-contact', methods=['POST'])
def delete_contact_route():
    contato_id = request.form.get('id')
    success = delete_contact(contato_id)
    return jsonify(success=success)  # Retornando um JSON

if __name__ == '__main__':
    app.run(debug=True)