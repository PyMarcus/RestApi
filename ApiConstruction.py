# esta API visa gerenciar desenvolvedores

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {'Nome': 'Marcus',
     'habilidade': ['Python', 'HTML5', 'CSS3', 'JavaScript', 'Java']},
    {
        'nome': 'MVRA',
        'habilidade': ['Python', 'Flask']
    },
    {
        'Nome': 'Vinicius',
        'habilidade': ['Python', 'Assembly', 'C', 'JavaScript', 'Java']},
    ,
    {
        'Nome': 'Ribeiro',
        'habilidade': ['Python', 'C++', 'NodeJS', 'JavaScript', 'Java']},
    ,
    {
        'Nome': 'Andrade',
        'habilidade': ['Python', 'HTML5', 'CSS3', 'JavaScript', 'Java']},
    ,
    {
        'Nome': 'Robo',
        'habilidade': ['Python', 'Assembly', 'C', 'JavaScript', 'Java']},
    ,
    {
        'Nome': 'Ninja',
        'habilidade': ['Python', 'C++', 'NodeJS', 'JavaScript', 'Java'},
    ,
    {
        'Nome': 'Fighter',
        'habilidade': ['Python', 'HTML5', 'CSS3', 'JavaScript', 'Java']},
    ,
    {
        'Nome': 'Hacker',
        'habilidade': ['Python', 'HTML5', 'CSS3', 'JavaScript', 'Java']},
    ,
    {
        'Nome': 'Nice',
        'habilidade': ['Python', 'C++', 'NodeJS', 'JavaScript', 'Java']},
    ,
    {
        'Nome': 'OK',
        'habilidade': ['Python', 'Assembly', 'C', 'JavaScript', 'Java']},
    ,
    {
        'Nome': 'Google',
        'habilidade': ['Python', 'HTML5', 'CSS3', 'JavaScript', 'Java']},
]


# devolve developer pelo id
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE', 'POST'])
def developer(id):
        """
        Busca, insere, atualiza, deleta dados
        """
    if request.method == 'GET':
        try:
        
            desenvolvedor = developers[id]  # conforme o id passado, pega-se os nomes
            return jsonify(desenvolvedor)
        
        except IndexError:
        
            return jsonify({'Dados status': 'deletados'})
        
        except Exception:
        
            return jsonify({"ERROR status": "Desconhecido, procure o administrador "})
        
    elif request.method == 'POST':
        
        dados = json.loads(request.data)  # pega do body e atualiza
        developers[id] = dados
        return jsonify(dados)
        
    elif request.method == 'PUT':
        pass
        
    elif request.method == 'DELETE':
        
        developers.pop(id)
        return jsonify({'Sucesso!': "Excluído"})


# inserção de dados
@app.route('/dev', methods=['POST', 'GET'])
def listaDeveloper():
        """
        Insere dados através do post e retorna a lista json completa com o método HTTP get.
        """
    if request.method == 'POST':
        
        dados = json.loads(request.data)
        developers.append(dados)
        return jsonify({'status': 'Sucesso!Registro inserido'})

    # consultar todos os dev
    elif request.method == 'GET':
        return jsonify(developers)


if __name__ == '__main__':
    app.run(debug=True)
