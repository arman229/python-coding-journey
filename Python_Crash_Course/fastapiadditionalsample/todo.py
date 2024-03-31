from typing import List,Optional,Union
from enum import Enum
from pydantic import BaseModel

from datetime import datetime

class Priority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    
class Status(Enum):
    COMPLETED = "COMPLETED"
    PENDING= "PENDING"   

class Todo(BaseModel):
        id:int
        title:str
        description:str
        date: str
        priority :Priority
        status:Status
        labels:List[str] 


