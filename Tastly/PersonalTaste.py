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

	def toString(self):
		return f"gender:{self.gender},age:{self.age},music:{self.music},beverage:{self.beverage},smoker:{self.smoker}"

	def fillValue(self, value):
		if(self.music == "None"):
			self.music = value
		elif(self.beverage == "None"):
			self.beverage = value
		else:
			self.gender = value


def fromString(s):
	taste = PersonalTaste()
	fullString = s.split(",")
	valueDict = dict()
	for v in fullString:
		p = v.split(":")
		valueDict[p[0]] = p[1]
	taste.age = valueDict["age"]
	taste.gender = valueDict["gender"]
	taste.music = valueDict["music"]
	taste.beverage = valueDict["beverage"]
	taste.smoker = valueDict["smoker"]
	return taste