from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class PersonalTaste(Base):
	__tablename__ = "personaltaste"
	id = Column(Integer, primary_key = True)
	gender = Column(String(40))
	age = Column(Integer)
	music = Column(String(40))
	beverage = Column(String(40))
	smoker = Column(String(10))

	def toDict(self):
		return {
			"gender" : self.gender,
			"age" : self.age,
			"music" : self.music,
			"beverage" : self.beverage,
			"smoker" : self.smoker
		}