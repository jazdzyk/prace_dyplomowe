from sqlalchemy import Column, SMALLINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Researchers(Base):
    __tablename__ = "PracownicyNaukowi"

    id_pracownikNaukowy = Column(SMALLINT, primary_key=True)
    imie = Column(VARCHAR("max"), nullable=False)
    nazwisko = Column(VARCHAR("max"), nullable=False)
    telefon = Column(VARCHAR(11), nullable=False)
    email = Column(VARCHAR("max"), nullable=False)
    id_stopienNaukowy = Column(SMALLINT, nullable=False)
    id_katedra = Column(SMALLINT, nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}(id_pracownikNaukowy={self.id_pracownikNaukowy}, imie={self.imie}, " \
            f"nazwisko={self.nazwisko}, telefon={self.telefon}, email={self.email}, " \
            f"id_stopienNaukowy={self.id_stopienNaukowy}, id_katedra={self.id_katedra})>"
