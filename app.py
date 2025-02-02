from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import sqlite3

app = Flask(__name__)

# Função para inicializar o banco de dados
def init_db():
    with sqlite3.connect("corretores.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS corretores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf TEXT NOT NULL,
            nome_completo TEXT NOT NULL,
            data_nascimento DATE NOT NULL,
            imobiliaria TEXT,
            creci TEXT NOT NULL,
            estado_creci TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            cep TEXT NOT NULL,
            logradouro TEXT NOT NULL,
            bairro TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            numero TEXT NOT NULL
        )''')
        conn.commit()

init_db()

# Função para buscar endereço pelo CEP
def buscar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        return dados.get("logradouro", ""), dados.get("bairro", ""), dados.get("localidade", ""), dados.get("uf", "")
    return "", "", "", ""

@app.route('/')
def index():
    with sqlite3.connect("corretores.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM corretores")
        corretores = cursor.fetchall()
    return render_template('index.html', corretores=corretores)

@app.route('/add_corretor', methods=['POST'])
def add_corretor():
    id = request.form.get('id')
    cpf = request.form['cpf']
    nome_completo = request.form['nome_completo']
    data_nascimento = request.form['data_nascimento']
    imobiliaria = request.form['imobiliaria']
    creci = request.form['creci']
    estado_creci = request.form['estado_creci']
    telefone = request.form['telefone']
    email = request.form['email']
    cep = request.form['cep']
    logradouro = request.form['logradouro']
    bairro = request.form['bairro']
    cidade = request.form['cidade']
    estado = request.form['estado']
    numero = request.form['numero']

    with sqlite3.connect("corretores.db") as conn:
        cursor = conn.cursor()
        if id:
            cursor.execute('''UPDATE corretores SET cpf=?, nome_completo=?, data_nascimento=?, imobiliaria=?, creci=?, estado_creci=?, telefone=?, email=?, cep=?, logradouro=?, bairro=?, cidade=?, estado=?, numero=? WHERE id=?''',
                           (cpf, nome_completo, data_nascimento, imobiliaria, creci, estado_creci, telefone, email, cep, logradouro, bairro, cidade, estado, numero, id))
        else:
            cursor.execute('''INSERT INTO corretores (cpf, nome_completo, data_nascimento, imobiliaria, creci, estado_creci, telefone, email, cep, logradouro, bairro, cidade, estado, numero)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                           (cpf, nome_completo, data_nascimento, imobiliaria, creci, estado_creci, telefone, email, cep, logradouro, bairro, cidade, estado, numero))
        conn.commit()

    return '', 204

@app.route('/get_corretores', methods=['GET'])
def get_corretores():
    with sqlite3.connect("corretores.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM corretores")
        corretores = cursor.fetchall()
        corretores_list = []
        for corretor in corretores:
            corretores_list.append({
                'id': corretor[0],
                'cpf': corretor[1],
                'nome_completo': corretor[2],
                'data_nascimento': corretor[3],
                'imobiliaria': corretor[4],
                'creci': corretor[5],
                'estado_creci': corretor[6],
                'telefone': corretor[7],
                'email': corretor[8],
                'cep': corretor[9],
                'logradouro': corretor[10],
                'bairro': corretor[11],
                'cidade': corretor[12],
                'estado': corretor[13],
                'numero': corretor[14]
            })
    return jsonify(corretores_list)

@app.route('/get_corretor/<int:id>', methods=['GET'])
def get_corretor(id):
    with sqlite3.connect("corretores.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM corretores WHERE id = ?", (id,))
        corretor = cursor.fetchone()
        if corretor:
            corretor_dict = {
                'id': corretor[0],
                'cpf': corretor[1],
                'nome_completo': corretor[2],
                'data_nascimento': corretor[3],
                'imobiliaria': corretor[4],
                'creci': corretor[5],
                'estado_creci': corretor[6],
                'telefone': corretor[7],
                'email': corretor[8],
                'cep': corretor[9],
                'logradouro': corretor[10],
                'bairro': corretor[11],
                'cidade': corretor[12],
                'estado': corretor[13],
                'numero': corretor[14]
            }
            return jsonify(corretor_dict)
        return '', 404

@app.route('/delete_corretor/<int:id>', methods=['DELETE'])
def delete_corretor(id):
    with sqlite3.connect("corretores.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM corretores WHERE id = ?", (id,))
        conn.commit()
    return '', 204

@app.route('/enviar_corretores', methods=['POST'])
def enviar_corretores():
    # Implementar a lógica para enviar os corretores cadastrados
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)