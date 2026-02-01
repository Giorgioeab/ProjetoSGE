from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Configuração do banco de dados
DATABASE_URL = "sqlite:///SGE.db"

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)


# Definição das tabelas como modelos ORM

class Aluno(Base):
    __tablename__ = 'Alunos'

    cpf = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(String, nullable=False)
    nome_mae = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=False)

    # Relacionamento com turmas
    turmas = relationship("AlunoTurma", back_populates="aluno")

    def __repr__(self):
        return f"<Aluno(cpf={self.cpf}, nome='{self.nome}')>"


class Professor(Base):
    __tablename__ = 'Professores'

    cpf = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(String, nullable=False)
    nome_mae = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=False)

    # Relacionamento com turmas
    turmas = relationship("Turma", back_populates="professor")

    def __repr__(self):
        return f"<Professor(cpf={self.cpf}, nome='{self.nome}')>"


class Curso(Base):
    __tablename__ = 'Cursos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_curso = Column(String, nullable=False)
    turno = Column(String, nullable=False)
    duracao = Column(String, nullable=False)

    # Relacionamento com turmas
    turmas = relationship("Turma", back_populates="curso")

    def __repr__(self):
        return f"<Curso(id={self.id}, nome_curso='{self.nome_curso}')>"


class Turma(Base):
    __tablename__ = 'Turmas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_curso = Column(Integer, ForeignKey('Cursos.id'))
    cpf_professor = Column(Integer, ForeignKey('Professores.cpf'))

    # Relacionamentos
    curso = relationship("Curso", back_populates="turmas")
    professor = relationship("Professor", back_populates="turmas")
    alunos = relationship("AlunoTurma", back_populates="turma")

    def __repr__(self):
        return f"<Turma(id={self.id}, id_curso={self.id_curso})>"


class AlunoTurma(Base):
    __tablename__ = 'Alunos_Turmas'

    id_aluno = Column(Integer, ForeignKey('Alunos.cpf'), primary_key=True)
    id_turma = Column(Integer, ForeignKey('Turmas.id'), primary_key=True)

    # Relacionamentos
    aluno = relationship("Aluno", back_populates="turmas")
    turma = relationship("Turma", back_populates="alunos")

    def __repr__(self):
        return f"<AlunoTurma(id_aluno={self.id_aluno}, id_turma={self.id_turma})>"


# Funções auxiliares

def criar_tabelas():
    """Cria todas as tabelas no banco de dados."""
    Base.metadata.create_all(engine)


def obter_sessao():
    """Retorna uma nova sessão do banco de dados."""
    return Session()


# Funções de teste

def test_insert_curso(curso, turno, duracao):
    """Insere um novo curso no banco de dados."""
    session = obter_sessao()
    novo_curso = Curso(nome_curso=curso, turno=turno, duracao=duracao)
    session.add(novo_curso)
    session.commit()
    session.close()


def test_select_alunos():
    """Retorna todos os alunos do banco de dados."""
    session = obter_sessao()
    alunos = session.query(Aluno).all()
    for aluno in alunos:
        print(aluno)
    session.close()
    return alunos


if __name__ == "__main__":
    # Criar todas as tabelas
    criar_tabelas()
    
    # Testar select de alunos
    test_select_alunos()
