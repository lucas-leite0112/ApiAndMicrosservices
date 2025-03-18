from flask import Flask, jsonify, request

''' Comentário teste '''

app = Flask(__name__)

dici = {
    "alunos":[
        {"id": 1,
        "nome": "lucas"}
    ]
}

@app.route('/alunos', methods=['GET'])
def getAlunos():
    dados = dici["alunos"]
    return jsonify(dados)

class AlunoNaoEncontrado(Exception):
    pass

@app.route('/alunos', methods=['POST'])
def criandoAluno():
    response = request.json
    aluno = dici['alunos']
    aluno.append(response)
    return jsonify(response)

@app.route('/alunos/<int:idAluno>', methods=['PUT'])
def updateAluno(idAluno):
    alunos = dici['alunos']
    for aluno in alunos:
        if aluno['id'] == idAluno:
            response = request.json
            aluno['nome'] = response['nome']
            return jsonify(response),200

if __name__ == "__main__":
    app.run(debug=True)