from sqlalchemy import Column, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Students(Base):
    __tablename__ = "Studenci"

    id_student = Column(VARCHAR(10), primary_key=True)
    imie = Column(VARCHAR("max"), nullable=False)
    nazwisko = Column(VARCHAR("max"), nullable=False)
    telefon = Column(VARCHAR(11), nullable=False)
    email = Column(VARCHAR("max"), nullable=False)

    def __repr__(self):
        return f"<{self.__tablename__}(id_pracownikNaukowy={self.id_student}, imie={self.imie}, " \
            f"nazwisko={self.nazwisko}, telefon={self.telefon}, email={self.email})>"
