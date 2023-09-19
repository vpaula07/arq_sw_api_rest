from pydantic import BaseModel
from typing import List
from model.cadastro import Cadastro

from schemas import ComentarioSchema


class CadastroSchema(BaseModel):
    """ Define como um novo usuário a ser inserido deve ser representado
    """
    usuario: str = "vanessapaula"
    cep: int = 30320900
    logradouro: str = "Rodovia BR-356"
    bairro: str = "Belvedere"
    cidade: str = "Belo Horizonte"
    uf: str = "MG"


class CadastroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do usuário.
    """
    id: int = "1"


class ListagemCadastrosSchema(BaseModel):
    """ Define como uma listagem de cadastrados será retornada.
    """
    cadastros:List[CadastroSchema]


def apresenta_cadastros(cadastros: List[Cadastro]):
    """ Retorna uma representação do cadastrado seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for cadastro in cadastros:
        result.append({
            "usuario": cadastro.usuario,
            "cep": cadastro.cep,
            "logradouro": cadastro.logradouro,
            "bairro": cadastro.bairro,
            "cidade": cadastro.cidade,
            "uf": cadastro.uf,
        })

    return {"cadastros": result}


class CadastroViewSchema(BaseModel):
    """ Define como um usuário será retornado: cadastro + comentários.
    """
    id: int = 1
    usuario: str = "vanessapaula"
    cep: int = 30320900
    logradouro: str = "Rodovia BR-356"
    bairro: str = "Belvedere"
    cidade: str ="Belo Horizonte"
    uf: str = "MG"
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]


class CadastroDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    usuario: str

def apresenta_cadastro(cadastro: Cadastro):
    """ Retorna uma representação do usuário seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": cadastro.id,
        "usuario": cadastro.usuario,
        "cep": cadastro.cep,
        "logradouro": cadastro.logradouro,
        "bairro":cadastro.bairro,
        "cidade": cadastro.cidade,
        "uf": cadastro.uf,
        "total_cometarios": len(cadastro.comentarios),
        "comentarios": [{"texto": c.texto} for c in cadastro.comentarios]
    }