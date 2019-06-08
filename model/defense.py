from sqlalchemy import Column, SMALLINT, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Defense(Base):
    __tablename__ = "Obrona"

    id_obrona = Column(SMALLINT, primary_key=True)
    data = Column(DATETIME, nullable=False)
    id_praca = Column(SMALLINT, nullable=False)
    id_komisja = Column(SMALLINT, nullable=False)
    id_lokalizacja = Column(SMALLINT, nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}(id_obrona={self.id_obrona}, data={self.data}, id_praca={self.id_praca}, " \
            f"id_komisja={self.id_komisja}, id_lokalizacja={self.id_lokalizacja})>"
