import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from Tastly.PersonalTaste import PersonalTaste
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

dbUrl = "postgresql://root:Talegazo0931@mypostgresdb.ck9iopsl8va4.us-east-2.rds.amazonaws.com:5432/TastlyDb"
engine = create_engine(dbUrl)
Base.metadata.create_all(engine)


class TastlySession:
	
	session = Session()
	
	def __enter__(self):
		self.session = Session(engine)
		return self.session

	def __exit__(self, exc_type, exc_value, tb):
		self.session.close()


def saveTaste(taste:PersonalTaste):
	with TastlySession() as session:
		session.add(taste)
		session.commit()

def findAll():
	with TastlySession() as session:
		tastes = session.query(PersonalTaste).all()
		for taste in tastes:
			print(vars(taste))