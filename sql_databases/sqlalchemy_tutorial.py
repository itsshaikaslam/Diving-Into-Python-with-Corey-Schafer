from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship



Base = declarative_base()

class User(Base):
	""" User table class """
	__tablename__ = "person"

	id = Column("id", Integer, primary_key=True)
	name = Column("username", String, unique=True)

# user = User()
# user.id = 0
# user.name = 'bandy'

# session.add(user)
# session.commit()

engine = create_engine("sqlite:///user.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
users = session.query(User).all()
for user in users:
	print(user)

session.close()