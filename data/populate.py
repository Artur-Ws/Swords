from enemy import Enemy
from environments import Environment

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()