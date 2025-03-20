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
    ],
    "professores":[
        {
        "id": 0,
        "nome": "string",
        "idade": 0,
        "data_nascimento": "string",
        "disciplina": "string",
        "salario": 0
            
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


@app.route('/professores/<int:idProfessor>', methods=['DELETE'])
def deletandoProfessor(idProfessor):
    professores = dici['professores']
    for professor in professores:
        if 'id' in professor and professor['id'] == idProfessor: 
            professores.remove(professor)
            return jsonify({"mensagem": "Professor deletado"}), 200
    return jsonify({"mensagem": "Professor não encontrado"}), 404
    
@app.route('/turmas', methods=['GET'])
def getTurmas():
    r = dici["turmas"]
    return jsonify(r)


@app.route('/turmas', methods=['POST'])
def criar_turma():
    try:
        r = request.get_json()
        turmas = dici["turmas"]
        turma = {
            "id": len(turmas),
            "nome": r["nome"],
            "professor_id": r["professor_id"]
        }
        turmas.append(turma)
        return jsonify(turma)
    except Exception:
        return jsonify({"erro": "Erro ao criar turma"})


@app.route('/turmas/<int:idTurma>', methods=['PUT'])
def updateTurma(idTurma):
    try:
        turmas = dici["turmas"]
        for turma in turmas:
            if turma["id"] == idTurma:
                r = request.get_json()
                turma["nome"] = r.get("nome", turma["nome"])
                turma["professor_id"] = r.get("professor_id", turma["professor_id"])
                return jsonify(turma)
        return jsonify({"erro": "Turma não encontrada"})
    except Exception:
        return jsonify({"erro": "Erro ao atualizar turma"})
    
@app.route('/turmas/<int:idTurma>', methods=['DELETE'])
def deletar_turma(idTurma):
    try:
        turmas = dici["turmas"]
        for turma in turmas:
            if turma["id"] == idTurma:
                turmas.remove(turma)
                return jsonify({"mensagem": "Turma deletada"})
        return jsonify({"erro": "Turma não encontrada"})
    except Exception:
        return jsonify({"erro": "Erro ao deletar turma"})

if __name__ == "__main__":
    app.run(debug=True)
