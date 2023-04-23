from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class EnvironmentEnemy(Base):
    __tablename__ = "Environment-Enemy"
    env_id = Column("Environment_id", Integer, ForeignKey('Environments.id'))
    enemy_id = Column("Enemy_id", Integer, ForeignKey('Enemies.id'))

    def __init__(self, name, level, category, armor, damage, health, mana, value):
        self.name = name
        self.level = level
        self.category = category
        self.armor = armor
        self.damage = damage
        self.health = health
        self.mana = mana
        self.value = value

    def __repr__(self):
        return f"{self.id}. Item: {self.name}, category: {self.category}, value: {self.value}"

    def add_entry(self):
        engine = create_engine("sqlite:///databases/data.db", echo=True)
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(self)
        session.commit()