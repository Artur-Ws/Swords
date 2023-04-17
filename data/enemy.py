from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

from main.character import Character

Base = declarative_base()


class Enemy(Character, Base):
    __tablename__ = "Enemies"
    id = Column("ID", Integer, primary_key=True)
    name = Column("name", String)
    x = Column("x-pos", Integer)
    y = Column("y-pos", Integer)
    strength = Column("strength", Integer)
    defense = Column("defense", Integer)
    health_points = Column("health_points", Integer)
    # Loot should be inserted as string with loot available for enemy, separated by ", ". Example: "ring, pelt"
    loot = Column("Loot", String)

    def __init__(self, id, name, x, y, strength, defense, health_points, loot):
        super().__init__(x, y, name, strength, defense, health_points)
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.strength = strength
        self.defense = defense
        self.health_points = health_points
        self.loot = loot

    def __repr__(self):
        return f"{self.id}. Enemy: {self.name}. Stats: STR-{self.strength}, DEF-{self.defense}, HP-{self.health_points}"

    def add_entry(self):
        engine = create_engine("sqlite:///databases/enemies.db", echo=True)
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(self)
        session.commit()


# Enemy(1, "Wolf", 100, 100, 10, 2, 30, "Pelt, Fang").add_entry()
