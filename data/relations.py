from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from enemy import Enemy
from items import Item
from environments import Environment

Base = declarative_base()


class EnvironmentEnemy(Base):
    pass


class EnemyItem(Base):
    pass