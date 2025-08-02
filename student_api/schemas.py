
from pydantic import BaseModel
from typing import Dict, List, Union


class Student(BaseModel):
    name: str
    subject_scores: Dict[str, float]
    average: float = 0.0
    grade: str = ""


class ResponseModel(BaseModel):
    message: str
    status: bool
    data: Union[Student, List[Student], None]

