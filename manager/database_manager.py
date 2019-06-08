import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseManager:
    __instance__ = None

    __SERVER = "jj-pw.database.windows.net"
    __DATABASE = "prace_dyplomowe"
    __PORT = 1433
    __DRIVER = "ODBC+Driver+17+for+SQL+Server"
    __USERNAME = os.environ.get("DB_USERNAME")
    __PASSWORD = os.environ.get("DB_PASSWORD")

    @staticmethod
    def instance():
        if DatabaseManager.__instance__ is None:
            DatabaseManager()
        return DatabaseManager.__instance__

    def __init__(self):
        if DatabaseManager.__instance__ is not None:
            raise Exception("The DatabaseManager class is a singleton.")
        else:
            DatabaseManager.__instance__ = self
            self._session, self._engine = self.__start_session()

    def add(self, data):
        self._session.add(data)
        self._session.commit()

    @staticmethod
    def __start_session():
        engine = create_engine(
            f"mssql+pyodbc://{DatabaseManager.__USERNAME}:{DatabaseManager.__PASSWORD}@{DatabaseManager.__SERVER}"
            f":{DatabaseManager.__PORT}/{DatabaseManager.__DATABASE}?driver={DatabaseManager.__DRIVER}",
            fast_executemany=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session, engine
