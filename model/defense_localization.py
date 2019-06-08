from sqlalchemy import Column, SMALLINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DefenseLocalization(Base):
    __tablename__ = "Lokalizacja"

    id_lokalizacja = Column(SMALLINT, primary_key=True)
    sala = Column(VARCHAR(15), nullable=False)
    budynek = Column(VARCHAR(100), nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}(id_lokalizacja={self.id_lokalizacja}, sala={self.sala}, budynek={self.budynek})>"
