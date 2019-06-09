import os

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
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
            self._engine = self.__start_engine()
            self.query("SELECT * FROM Katedra")

    def set_delegate(self, delegate):
        self._delegate = delegate

    def add(self, data):
        session = self.__start_session()
        try:
            session.add(data)
            session.commit()
        except IntegrityError as error:
            self._delegate.manager_reports_error(error)

    def add_many(self, data):
        session = self.__start_session()
        try:
            session.add_all(data)
            session.commit()
        except IntegrityError as error:
            self._delegate.manager_reports_error(error)

    def query(self, sql_command):
        connection = self._engine.connect()
        result = connection.execute(sql_command)
        rows = result.fetchall()
        connection.close()
        return rows

    def __start_session(self):
        Session = sessionmaker(bind=self._engine)
        session = Session()
        return session

    @staticmethod
    def __start_engine():
        return create_engine(
            f"mssql+pyodbc://{DatabaseManager.__USERNAME}:{DatabaseManager.__PASSWORD}@{DatabaseManager.__SERVER}"
            f":{DatabaseManager.__PORT}/{DatabaseManager.__DATABASE}?driver={DatabaseManager.__DRIVER}",
            fast_executemany=True)
