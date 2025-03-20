from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

dici = {
    "alunos":[
        {
            "nome": "string",
            "data_nascimento": "string",
            "nota_primeiro_semestre": 0,
            "nota_segundo_semestre": 0,
            "turma_id": 0
        }
    ],
    "professores":[
        {
            "nome": "string",
            "data_nascimento": "string",
            "disciplina": "string",
            "salario": 0
        }
    ],
    "turmas":[
        {
            "id": 0,
            "nome": "string",
            "turno": "string",
            "professor_id": 0
        }
    ]
}

idAluno = 0
idProfessor = 0

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
    data_nasc = datetime.strptime(data, "%d/%m/%Y")
    data_atual = datetime.today()
    idade = data_atual.year - data_nasc.year - ((data_atual.month, data_atual.day) < (data_nasc.month, data_nasc.day))
    response["idade"] = idade

    global idAluno
    idAluno += 1
    response["id"] = idAluno

    aluno.append(response)
    return jsonify({"mensagem":"Aluno criado","aluno":aluno}),201

@app.route('/alunos/<int:idAluno>', methods=['PUT'])
def updateAluno(idAluno):
    alunos = dici['alunos']
    for aluno in alunos:
        if 'id' in aluno and aluno['id'] == idAluno:
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


# PROFESSOR

@app.route('/professores', methods=['GET'])
def getProfessor():
    dados = dici["professores"]
    return jsonify(dados)

@app.route('/professores', methods=['POST'])
def criandoProfessor():
    response = request.json
    professor = dici['professores']

    data = response['data_nascimento']
    data_nasc = datetime.strptime(data, "%d/%m/%Y")
    data_atual = datetime.today()
    idade = data_atual.year - data_nasc.year - ((data_atual.month, data_atual.day) < (data_nasc.month, data_nasc.day))
    response["idade"] = idade

    global idProfessor
    idProfessor += 1
    response["id"] = idProfessor

    professor.append(response)
    return jsonify({"mensagem":"Professor criado","professor":professor}),201

@app.route('/professores/<int:idProfessor>', methods=['GET'])
def getProfessorId(idProfessor):
    professores = dici['professores']
    for professor in professores:
        if 'id' in professor and professor['id'] == idProfessor:
            return jsonify(professor)
    return jsonify({'mensagem':'Professor não encontrado'})

@app.route('/professores/<int:idProfessor>', methods=['PUT'])
def atualizandoProfessor(idProfessor):
    professores = dici['professores']
    for professor in professores:
        if professor['id'] == idProfessor:
            response = request.json
            professor['nome'] = response['nome']
            return jsonify(response)
    return jsonify({"mensagem":"Professor não encontrado"})

@app.route('/professores/<int:idProfessor>', methods=['DELETE'])
def deletandoProfessor(idProfessor):
    professores = dici['professores']
    for professor in professores:
        if 'id' in professor and professor['id'] == idProfessor: 
            professores.remove(professor)
            return jsonify({"mensagem": "Professor deletado"}), 200
    return jsonify({"mensagem": "Professor não encontrado"}), 404

# TURMA
    
@app.route('/turmas', methods=['GET'])
def getTurma():
    dados = dici["turmas"]
    return jsonify(dados)


@app.route('/turmas', methods=['POST'])
def criandoTurma():
    response = request.json
    turma = dici["turmas"]

    response['id'] = len(turma)

    turma.append(response)
    return jsonify({"mensagem":"Turma criada","turma":turma}),201

@app.route('/turmas/<int:idTurma>', methods=['GET'])
def getTurmaId(idTurma):
    turmas = dici['turmas']
    for turma in turmas:
        if 'id' in turma and turma['id'] == idTurma:
            return jsonify(turma)
    return jsonify({'mensagem':'Turma não encontrada'})

@app.route('/turmas/<int:idTurma>', methods=['PUT'])
def atualizandoTurmas(idTurma):
    turmas = dici['turmas']
    for turma in turmas:
        if turma['id'] == idTurma:
            response = request.json
            turma['nome'] = response['nome']
            return jsonify(response)
    return jsonify({"mensagem":"Turma não encontrada"})

@app.route('/turmas/<int:idTurma>', methods=['DELETE'])
def deletandoTurma(idTurma):
    turmas = dici['turmas']
    for turma in turmas:
        if 'id' in turma and turma['id'] == idTurma: 
            turmas.remove(turma)
            return jsonify({"mensagem": "Turma deletada"}), 200
    return jsonify({"mensagem": "Turma não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)
