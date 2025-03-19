from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

dici = {
    "alunos":[
    {
        "data_nascimento": "01/12/2002",
        "nome": "lucas",
        "nota_primeiro_semestre":0,
        "nota_segundo_semestre":0,
        "turma":0
    }
    ]
}

idContador = 0

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

    nota1 = float(response['nota_primeiro_semestre'])
    nota2 = float(response['nota_segundo_semestre'])
    media_final = (nota1 + nota2) / 2
    response["media_final"] = media_final

    data = response['data_nascimento']
    data_nasc = datetime.strptime(data, "%d-%m-%Y")
    data_atual = datetime.today()
    idade = data_atual.year - data_nasc.year - ((data_atual.month, data_atual.day) < (data_nasc.month, data_nasc.day))
    response["idade"] = idade

    global idContador
    idContador += 1
    response["id"] = idContador

    aluno.append(response)
    return jsonify({"mensagem":"Aluno criado","aluno":aluno}),201

@app.route('/alunos/<int:idAluno>', methods=['PUT'])
def updateAluno(idAluno):
    alunos = dici['alunos']
    for aluno in alunos:
        if aluno['id'] == idAluno:
            response = request.json
            aluno['nome'] = response['nome']
            return jsonify(response),200
    return jsonify({"mensagem":"Aluno não encontrado"})

@app.route('/alunos/<int:idAluno>', methods=['GET'])
def getAlunoId(idAluno):
    alunos = dici['alunos']
    for aluno in alunos:
        if 'id' in aluno and aluno['id'] == idAluno:
            return jsonify(aluno)
    return jsonify({'mensagem:"Aluno não encontrado '})


@app.route('/alunos/<int:idAluno>', methods=['DELETE'])
def deletandoAluno(idAluno):
    alunos = dici['alunos']
    for aluno in alunos:
        if 'id' in aluno and aluno['id'] == idAluno: 
            alunos.remove(aluno)
            return jsonify({"mensagem": "Aluno deletado"}), 200
    return jsonify({"mensagem": "Aluno não encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)