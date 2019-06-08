from sqlalchemy import Column, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DefenseCommitteeMembers(Base):
    __tablename__ = "CzlonkowieKomisji"

    id_czlonek = Column(SMALLINT, primary_key=True)
    id_komisja = Column(SMALLINT, primary_key=True)

    def __repr__(self):
        return f"<{self.__tablename__}(id_czlonek={self.id_czlonek}, id_komisja={self.id_komisja})>"
