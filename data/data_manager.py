from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from main.enemy import Enemy
from main.items import Item

Base = declarative_base()


class EnvironmentEnemy(Base):
    __tablename__ = "Environment_Enemy"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    env_id = Column("Environment_id", Integer, ForeignKey('Environments.id'))
    enemy_id = Column("Enemy_id", Integer, ForeignKey('Enemies.id'))


class ItemEnemy(Base):
    __tablename__ = "Item_Enemy"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    item_id = Column("Item_id", Integer, ForeignKey('Items.id'))
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
    items = relationship("ItemDB", secondary=ItemEnemy.__tablename__, back_populates="enemies")

    def __init__(self, name, x, y, strength, defense, health_points):
        super().__init__(x, y, name, strength, defense, health_points)
        self.name = name
        self.x = x
        self.y = y
        self.strength = strength
        self.defense = defense
        self.health_points = health_points


class ItemDB(Item, Base):
    __tablename__ = "Items"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    level = Column("level", Integer)
    category = Column("category", String)
    armor = Column("armor", Integer)
    damage = Column("damage", Integer)
    health = Column("health", Integer)
    mana = Column("mana", Integer)
    value = Column("value", Integer)
    enemies = relationship("EnemyDB", secondary=ItemEnemy.__tablename__, back_populates="items")

    def __init__(self, name, level, category, armor, damage, health, mana, value):
        super().__init__(name, level, category, armor, damage, health, mana, value)
        self.name = name
        self.level = level
        self.category = category
        self.armor = armor
        self.damage = damage
        self.health = health
        self.mana = mana
        self.value = value


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


def add_objects(*args):
    session.add_all(args)
    session.commit()


def link_environment_enemy(environment_name: str, enemy_name: str):
    environment = session.query(EnvironmentDB).filter(EnvironmentDB.name == environment_name).first()
    enemy = session.query(EnemyDB).filter(EnemyDB.name == enemy_name).first()
    environment.enemies.append(enemy)
    session.commit()


def get_all_related_enemies(environment_name):
    environment = session.query(EnvironmentDB).filter(EnvironmentDB.name == environment_name).first()
    return environment.enemies


def get_all_related_environments(enemy_name):
    enemy = session.query(EnemyDB).filter(EnemyDB.name == enemy_name).first()
    return enemy.environments


def get_all_related_items(enemy_name):
    enemy = session.query(EnemyDB).filter(EnemyDB.name == enemy_name).first()
    return enemy.items


engine = create_engine("sqlite:///databases/data.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
'''
############################################## Don't touch anything above ##############################################


'''

# enemy1 = EnemyDB("Wolf", 100, 100, 10, 2, 30)
# # env1 = EnvironmentDB("Forrest")
# item1 = ItemDB("Wolf Fur", 0, "Neutral", 0, 0, 0, 0, 15)
# item2 = ItemDB("Wolf Fang", 0, "Neutral", 0, 0, 0, 0, 5)
#
# # link_environment_enemy("Forrest", "Wolf")
# # print(get_all_related_enemies("Forrest"))
#
# add_objects(item1, item2)
