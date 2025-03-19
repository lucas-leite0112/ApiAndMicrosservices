from flask import Flask, jsonify, request

app = Flask(__name__)

dici = {
    "alunos":[{}],
    "professores":[{}],
    "turmas":[{}]
}

@app.route('/alunos', methods=['GET'])
def getAlunos():
    r = dici["alunos"]
    return jsonify(r)

class AlunoNaoEncontrado(Exception):
    pass

@app.route('/alunos', methods=['POST'])
def criarAluno():
    try:
        r = request.get_json()
        alunos = dici['alunos']
        aluno = {
            "id": len(alunos),
            "nome": r["nome"],
            "matricula": r["matricula"],
            "idade": r["idade"],
            "data_nascimento": r["data_nascimento"],
            "nota_primeiro_semestre": r["nota_primeiro_semestre"],
            "nota_segundo_semestre": r["nota_segundo_semestre"],
            "media_final": r["media_final"],
            "turma_id": r["turma_id"]
        }
        alunos.append(aluno)
        return jsonify(aluno)
    except Exception:
        return jsonify({"erro": "Erro ao criar o aluno"})

@app.route('/alunos/<int:idAluno>', methods=['PUT'])
def updateAluno(idAluno):
    try:
        alunos = dici['alunos']
        for aluno in alunos:
            if aluno['id'] == idAluno:
                r = request.get_json()
                aluno["nome"] = r.get("nome", aluno["nome"])
                aluno["matricula"] = r.get("matricula", aluno["matricula"])
                aluno["idade"] = r.get("idade", aluno["idade"])
                aluno["data_nascimento"] = r.get("data_nascimento", aluno["data_nascimento"])
                aluno["nota_primeiro_semestre"] = r.get("nota_primeiro_semestre", aluno["nota_primeiro_semestre"])
                aluno["nota_segundo_semestre"] = r.get("nota_segundo_semestre", aluno["nota_segundo_semestre"])
                aluno["media_final"] = r.get("media_final", aluno["media_final"])
                aluno["turma_id"] = r.get("turma_id", aluno["turma_id"])
                return jsonify(aluno)
        return jsonify({"erro": "Aluno não encontrado"})
    except Exception:
        return jsonify({"erro": "Erro ao atualizar aluno"})
    
@app.route('/alunos/<int:idAluno>', methods=['DELETE'])
def deletar_aluno(idAluno):
    try:
        alunos = dici["alunos"]
        for aluno in alunos:
            if aluno["id"] == idAluno:
                alunos.remove(aluno)
                return jsonify({"mensagem": "Aluno deletado"})
        return jsonify({"erro": "Aluno não encontrado"})
    except Exception:
        return jsonify({"erro": "Erro ao deletar aluno"})
        
@app.route('/professores', methods=['GET'])
def getProfessores():
    r = dici['professores']
    return jsonify(r)

@app.route('/professores', methods=['POST'])
def criarProfessor():
    try:
        r = request.get_json()
        professores = dici['professores']
        professor = {
            "id": len(professor),
            "nome": r["nome"],
            "especialidade": r["especialidade"],
            "idade": r["idade"],
            "info": r["info"]
        }
        professores.append(professor)
        return jsonify(professor)
    except Exception:
        return jsonify({"erro": "Erro ao criar professor"})
    
@app.route('/professores/<int:idProfessor>', methods=['PUT'])
def updateProfessor(idProfessor):
    try:
        professores = dici["professores"]
        for professor in professores:
            if professor["id"] == idProfessor:
                r = request.get_json()
                professor["nome"] = r.get("nome", professor["nome"])
                professor["especialidade"] = r.get("especialidade", professor["especialidade"])
                professor["idade"] = r.get("idade", professor["idade"])
                professor["info"] = r.get("info", professor["info"])
                return jsonify(professor)
        return jsonify({"erro": "Professor não encontrado"})
    except Exception:
        return jsonify({"erro": "Erro ao atualizar professor"})
    
@app.route('/professores/<int:idProfessor>', methods=['DELETE'])
def deletar_professor(idProfessor):
    try:
        professores = dici["professores"]
        for professor in professores:
            if professor["id"] == idProfessor:
                professores.remove(professor)
                return jsonify({"mensagem": "Professor deletado"})
        return jsonify({"erro": "Professor não encontrado"})
    except Exception:
        return jsonify({"erro": "Erro ao deletar professor"})
    
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
