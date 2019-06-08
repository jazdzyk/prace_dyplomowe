from sqlalchemy import Column, SMALLINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Degree(Base):
    __tablename__ = "StopienNaukowy"

    id_stopienNaukowy = Column(SMALLINT, primary_key=True)
    nazwaStopniaNaukowego = Column(VARCHAR("max"), nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}(id_stopienNaukowy={self.id_stopienNaukowy}, " \
            f"nazwaStopniaNaukowego={self.nazwaStopniaNaukowego})>"
