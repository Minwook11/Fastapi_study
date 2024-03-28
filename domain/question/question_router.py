from fastapi import APIRouter

from database import Session
from models import Question


router = APIRouter(
    prefix="/api/question",
)

@router.get("/list")
async def question_list():
    db = Session()
    
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    
    db.close()
    
    return _question_list