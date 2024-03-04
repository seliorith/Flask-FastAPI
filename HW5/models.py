from typing import Optional
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///db.db'  # URL подключения к базе данных для SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
    "check_same_thread": True})  # create_engine - эта функция создает объект engine, который SQLAlchemy использует для взаимодействия с базой данных

Base = declarative_base()  # создает базовый класс для всех моделей SQLAlchemy
SessionLocal = sessionmaker(autoflush=False,
                            bind=engine)  # это фабрика, которая создает новые объекты сессии при вызове
db = SessionLocal()  # создается экземпляр сессии, который будет использоваться для взаимодействия с базой данных


class TaskBase(Base):  # модель SQLAlchemy, которая определяет структуру таблицы базы данных для хранения задач
    __tablename__ = "tasks"  # название таблицы
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, nullable=False)
    title = Column(String(80), nullable=False)
    description = Column(String(80), nullable=False)
    status = Column(String(80), nullable=False)
    is_del = Column(Boolean, nullable=False)


class Task(BaseModel):  # класс определяет структуру данных задачи, используется для валидации
    task_id: int
    title: Optional[str] = None
    description: str
    status: Optional[str] = None
