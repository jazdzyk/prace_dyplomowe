from sqlalchemy import Column, SMALLINT, VARCHAR, NUMERIC, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Review(Base):
    __tablename__ = "Recenzja"

    id_recenzja = Column(SMALLINT, primary_key=True)
    id_praca = Column(SMALLINT, nullable=False)
    id_recenzujacy = Column(SMALLINT, nullable=False)
    ocena = Column(NUMERIC)
    tekstRecenzji = Column(VARCHAR("max"))
    dataWystawienia = Column(DATETIME)

    def __repr__(self):
        return f"<{self.__tablename__}(id_recenzja={self.id_recenzja}, id_praca={self.id_praca}, " \
            f"id_recenzujacy={self.id_recenzujacy}, ocena={self.ocena}, tekstRecenzji={self.tekstRecenzji}, " \
            f"dataWystawienia={self.dataWystawienia})>"
