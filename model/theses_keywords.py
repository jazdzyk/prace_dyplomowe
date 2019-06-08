from sqlalchemy import Column, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ThesesKeywords(Base):
    __tablename__ = "SlowaKluczowePracy"

    id_slowoKluczowe = Column(SMALLINT, primary_key=True)
    id_praca = Column(SMALLINT, primary_key=True)

    def __repr__(self):
        return f"<{self.__tablename__}(id_slowoKluczowe={self.id_slowoKluczowe}, id_praca={self.id_praca})>"
