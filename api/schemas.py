from typing import List
from pydantic import BaseModel


class CourseData(BaseModel):
    ano_ingresso : int
    inst : str
    nome : str
    disciplinas : List[str]

    def getJson(self):
        return {
            "ano_ingresso" : self.ano_ingresso,
            "inst" : self.inst,
            "nome" : self.nome,
            "disciplinas" : str(self.disciplinas)
        }

class StudentData(BaseModel):
    nome : str
    nasc : str
    email : str
    reside_farroupilha : bool
    altura : float
    curso : CourseData

    def getJson(self):
        return {
            "nome" : self.nome,
            "nasc" : self.nasc,
            "email" : self.email,
            "reside_farroupilha" : self.reside_farroupilha,
            "altura" : self.altura,
            "curso" : self.curso.getJson()
        }