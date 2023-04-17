from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Item(Base):
    __tablename__ = "Items"
    id = Column("ID", Integer, primary_key=True)
    name = Column("name", String)
    level = Column("level", Integer)
    category = Column("category", String)
    armor = Column("armor", Integer)
    damage = Column("damage", Integer)
    health = Column("health", Integer)
    mana = Column("mana", Integer)
    value = Column("value", Integer)

    def __init__(self, id, name, level, category, armor, damage, health, mana, value):
        self.id = id
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
        engine = create_engine("sqlite:///databases/items.db", echo=True)
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(self)
        session.commit()


# Item(1, "Wolf Fur", 0, "Neutral", 0, 0, 0, 0, 10).add_entry()
