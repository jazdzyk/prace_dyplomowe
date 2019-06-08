from sqlalchemy import Column, SMALLINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Faculty(Base):
    __tablename__ = "Wydzial"

    id_Wydzial = Column(SMALLINT, primary_key=True)
    nazwaWydzialu = Column(VARCHAR("max"), nullable=False)

    def __repr__(self):
        return f"<Wydzial(id_Wydzial={self.id_Wydzial}, nazwaWydzialu={self.nazwaWydzialu})>"
