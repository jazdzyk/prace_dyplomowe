from sqlalchemy import Column, SMALLINT, NUMERIC, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ThesesAuthors(Base):
    __tablename__ = "AutorzyPracy"

    id_student = Column(VARCHAR(10), primary_key=True)
    id_praca = Column(SMALLINT, primary_key=True)
    ocenaKoncowa = Column(NUMERIC)

    def __repr__(self):
        return f"<{self.__tablename__}(id_student={self.id_student}, id_praca={self.id_praca}, " \
            f"ocenaKoncowa={self.ocenaKoncowa})>"
