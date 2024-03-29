from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Question
from domain.question import question_schema


router = APIRouter(
    prefix="/api/question",
)

@router.get("/list", response_model=list[question_schema.Question])
async def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(
        Question
    ).order_by(
        Question.create_date.desc()
    ).all()
    
    return _question_list