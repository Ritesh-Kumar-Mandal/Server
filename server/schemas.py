from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

##--------------------------------- Pydantic models --------------------------------
##--------------------------------- User
class User(BaseModel):
    name : str
    age : str
    sex : str

class CreateUser(BaseModel):

    name : str
    age : str
    sex : str
    mobile : Optional[str] = None
    govtID : Optional[str] = None
    guardian : Optional[str] = None
    email : Optional[str] = None
    emergencyNumber : Optional[str] = None
    address : Optional[str] = None
    state : Optional[str] = None
    city : Optional[str] = None
    country : Optional[str] = None
    pincode : Optional[str] = None
    occupation : Optional[str] = None
    religion : Optional[str] = None
    maritalStatus : Optional[str] = None
    bloodGroup : Optional[str] = None
    nationality : Optional[str] = None

## Response Models
class ShowUser(BaseModel):
    name : str
    age : str
    sex : str
    mobile : Optional[str] = None
    address : Optional[str] = None
    govtID : Optional[str] = None
    guardian : Optional[str] = None
    nationality : Optional[str] = None
    
    class Config():
        orm_mode=True