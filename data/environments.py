from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Environment(Base):
    __tablename__ = "Environments"
    id = Column("ID", Integer, primary_key=True)
    name = Column("name", String)
    # Enemies should be inserted as string with enemies available in location, separated by ", ". Example: "Wolf, Fox"
    enemies = Column("Enemies", String)

    def __init__(self, id, name, enemies):
        self.id = id
        self.name = name
        self.enemies = enemies

    def __repr__(self):
        return f"{self.id}. Location: {self.name}. Possible enemies: {self.enemies}"

    def add_entry(self):
        engine = create_engine("sqlite:///databases/environments.db", echo=True)
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(self)
        session.commit()
