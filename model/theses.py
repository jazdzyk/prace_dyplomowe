from sqlalchemy import Column, SMALLINT, VARCHAR, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Theses(Base):
    __tablename__ = "PraceDyplomowe"

    id_praca = Column(SMALLINT, primary_key=True)
    tytul = Column(VARCHAR("max"), nullable=False)
    id_promotor = Column(SMALLINT, nullable=False)
    id_kierunekStudiow = Column(SMALLINT, nullable=False)
    dataZlozenia = Column(DATETIME)

    def __repr__(self):
        return f"<{self.__tablename__}(id_praca={self.id_praca}, tytul={self.tytul}, id_promotor={self.id_promotor}, " \
            f"id_kierunekStudiow={self.id_kierunekStudiow}, dataZlozenia={self.dataZlozenia})>"
