from sqlalchemy import Column, SMALLINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StudiesType(Base):
    __tablename__ = "RodzajStudiow"

    id_rodzajStudiow = Column(SMALLINT, primary_key=True)
    nazwaRodzaju = Column(VARCHAR("max"), nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}(id_rodzajStudiow={self.id_rodzajStudiow}, nazwaRodzaju={self.nazwaRodzaju})>"
