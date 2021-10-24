# esta API visa gerenciar desenvolvedores

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {'Nome': 'Marcus',
     'habilidade': ['Python', 'HTML5', 'CSS3', 'JavaScript', 'Java']},
    {
        'nome': 'MSDA',
        'habilidade': ['Python', 'Flask']
    }
]


# devolve developer pelo id
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE', 'POST'])
def developer(id):
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
    if request.method == 'POST':
        dados = json.loads(request.data)
        developers.append(dados)
        return jsonify({'status': 'Sucesso!Registro inserido'})

    # consultar todos os dev
    elif request.method == 'GET':
        return jsonify(developers)


if __name__ == '__main__':
    app.run(debug=True)
