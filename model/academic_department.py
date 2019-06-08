from sqlalchemy import Column, SMALLINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AcademicDepartment(Base):
    __tablename__ = "Katedra"

    id_Katedra = Column(SMALLINT, primary_key=True)
    nazwaKatedry = Column(VARCHAR("max"), nullable=False)
    id_Wydzial = Column(SMALLINT, nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}(id_Katedra={self.id_Wydzial}, nazwaKatedry={self.nazwaWydzialu}, " \
            f"id_Wydzial={self.id_Wydzial})>"
