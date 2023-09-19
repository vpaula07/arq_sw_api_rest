from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario


class Cadastro(Base):
    __tablename__ = 'cadastro'

    id = Column("pk_cadastro", Integer, primary_key=True)
    usuario = Column(String(50), unique=True)
    cep = Column(Integer)
    logradouro = Column(String(120))
    bairro = Column(String(120))
    cidade = Column(String(120))
    uf = Column(String(10))
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o cadastrado e o comentário.
    # Essa relação é implicita, não está salva na tabela 'produto',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    comentarios = relationship("Comentario")

    def __init__(self, usuario:str, cep:int, logradouro:str, bairro:str, cidade:str, uf:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Usuário
        Arguments:
           usuario: nome do usuario cadstrado.
            cep: inseri o cep do usuario.
            logradouro: endereco do usuário a ser acessado via API.
            bairro: bairro do usuário a ser acessado via API.
            cidade: cidade do usuário a ser acessado via API.
            uf: estado do usuário acessado via API.
            data_insercao: data de quando o produto foi inserido à base
        """
        self.usuario = usuario
        self.cep = cep
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_comentario(self, comentario:Comentario):
        """ Adiciona um novo comentário ao Cadastro
        """
        self.comentarios.append(comentario)