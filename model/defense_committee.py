from sqlalchemy import Column, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DefenseCommittee(Base):
    __tablename__ = "KomisjaDyplomowa"

    id_komisja = Column(SMALLINT, primary_key=True)
    id_przewodniczacy = Column(SMALLINT, nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}(id_komisja={self.id_komisja}, id_przewodniczacy={self.id_przewodniczacy})>"
