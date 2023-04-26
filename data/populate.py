from enemy import Enemy
from environments import Environment
from data_manager import EnvironmentEnemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()
engine = create_engine("sqlite:///databases/data.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_objects(*args):
    session.add_all(args)
    session.commit()

def link_objects(to_be_linked, target_category):
    target_category.append(to_be_linked)
    session.commit()


'''
############################################## Don't touch anything above ##############################################


'''

enemy1 = Enemy("Wolf", 100, 100, 10, 2, 30)
env1 = Environment("Forrest")

add_objects(enemy1, env1)
