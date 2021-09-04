from uni_9_classes.controle_academico.pessoa import pessoa


class alunos():

    def __init__(self,nome,data_nascimento, endereco, bairro, cep, cidade,curso,matricula):
        aluno = pessoa(nome,data_nascimento,endereco,bairro, cep,cidade)
        self.curso=curso
        self.matricula=matricula
        self.disciplinas=[]


