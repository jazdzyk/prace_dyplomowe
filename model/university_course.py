from sqlalchemy import Column, SMALLINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UniversityCourse(Base):
    __tablename__ = "KierunekStudiow"

    id_kierunek = Column(SMALLINT, primary_key=True)
    nazwaKierunku = Column(VARCHAR("max"), nullable=False)
    id_rodzajStudiow = Column(SMALLINT, nullable=False)
    id_katedra = Column(SMALLINT, nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}(id_kierunek={self.id_kierunek}, nazwaKierunku={self.nazwaKierunku}, " \
            f"id_rodzajStudiow={self.id_rodzajStudiow}, id_katedra={self.id_katedra})>"
