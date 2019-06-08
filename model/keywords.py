from sqlalchemy import Column, SMALLINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Keywords(Base):
    __tablename__ = "SlowaKluczowe"

    id_slowoKluczowe = Column(SMALLINT, primary_key=True)
    slowoKluczowe = Column(VARCHAR("max"), nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}(id_slowoKluczowe={self.id_slowoKluczowe}, slowoKluczowe={self.slowoKluczowe})>"
