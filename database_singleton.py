from __future__ import annotations
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from typing import Optional


class SingletonMeta(type):
    _instance: Optional[Singleton] = None

    def __call__(self) -> Singleton:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Singleton(metaclass=SingletonMeta):
    def database_connection(self):
        db = SQLAlchemy()
        return db

    def migration(self):
        migrate = Migrate()
        return migrate
