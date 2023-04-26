from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from enemy import Enemy

Base = declarative_base()


class EnvironmentEnemy(Base):
    __tablename__ = "Environment_Enemy"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    env_id = Column("Environment_id", Integer, ForeignKey('Environments.id'))
    enemy_id = Column("Enemy_id", Integer, ForeignKey('Enemies.id'))


class EnemyDB(Enemy, Base):
    __tablename__ = "Enemies"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    x = Column("x-pos", Integer)
    y = Column("y-pos", Integer)
    strength = Column("strength", Integer)
    defense = Column("defense", Integer)
    health_points = Column("health_points", Integer)
    environments = relationship("EnvironmentDB", secondary=EnvironmentEnemy.__tablename__, back_populates="enemies")

    def __init__(self, name, x, y, strength, defense, health_points):
        super().__init__(x, y, name, strength, defense, health_points)
        self.name = name
        self.x = x
        self.y = y
        self.strength = strength
        self.defense = defense
        self.health_points = health_points

    # def add_entry(self):
    #     engine = create_engine("sqlite:///databases/data.db", echo=True)
    #     Base.metadata.create_all(bind=engine)
    #     Session = sessionmaker(bind=engine)
    #     session = Session()
    #     session.add(self)
    #     session.commit()


class EnvironmentDB(Base):
    __tablename__ = "Environments"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    # Enemies should be inserted as string with enemies available in location, separated by ", ". Example: "Wolf, Fox"
    enemies = relationship("EnemyDB", secondary=EnvironmentEnemy.__tablename__, back_populates="environments")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.id}. Location: {self.name}. Possible enemies: {self.enemies}"

    def add_entry(self):
        engine = create_engine("sqlite:///databases/data.db", echo=True)
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(self)
        session.commit()


def add_objects(*args):
    session.add_all(args)
    session.commit()


def link_objects(to_be_linked, target_category):
    target_category.append(to_be_linked)
    session.commit()


engine = create_engine("sqlite:///databases/data.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
'''
############################################## Don't touch anything above ##############################################


'''

enemy1 = EnemyDB("Wolf", 100, 100, 10, 2, 30)
env1 = EnvironmentDB("Forrest")

add_objects(enemy1, env1)
