from sqlalchemy import Column, String, Integer
from server.utils.dbUtil import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(String)
    sex = Column(String)
    mobile = Column(String)
    govtID = Column(String)
    guardian = Column(String)
    email = Column(String)
    emergencyNumber = Column(String)
    address = Column(String)
    state = Column(String)
    city = Column(String)
    country = Column(String)
    pincode = Column(String)
    occupation = Column(String)
    religion = Column(String)
    maritalStatus = Column(String)
    bloodGroup = Column(String)
    nationality = Column(String)