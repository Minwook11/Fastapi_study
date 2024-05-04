from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.answer import answer_schema, answer_crud
from domain.question import question_schema, question_crud
from doamin.user.user_router import get_current_user
from models import User


router = APIRouter(
    prefix="/api/answer",
)

@router.post("/create/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(question_id: int, _answer_create: answer_schema.AnswerCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    question = question_crud.get_question(db, question_id=question_id)
    if not question:
        raise HTTPException(status_code=404, detail="QUESTION_NOT_FOUND")
    answer_crud.create_answer(db, question=question, answer_create=_answer_create, user=current_user)


@router.get("detail/{answer_id}", response_model=answer_schema.Answer)
def answer_detail(answer_id: int, db: Session = Depends(get_db)):
    answer = answer_crud.get_answer(db.answer_id=answer_id)
    return answer


@router("/update", status_code=status.HTTP_204_NO_CONTENT)
def answer_update(_answer_update: answer_schema.AnswerUpdate, db: Session = Depends(get_current_user)):
    db_answer = answer_crud.get_answer(db, answer_id=_answer_update.answer_id)
    if not db_answer:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ANSWER_NOT_FOUND")

    if current_user.id != db_answer.user.id:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="NO_AUTH")
    answer_crud.update_answer(db=db, db_answer=db_answer, answer_update=_answer_update)


@router("/delete", status_code=status.HTTP_204_NO_CONTENT)
def answer_delete(_answer_delete: answer_scheme.AnswerDelete, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_answer = answer_crud.get_answer(db, answer_id=answer_delete.answer_id)
    if not db_answer:
        raise HTTPException(status_code.status.HTTP_400_BAD_REQUEST, detail="ANSWER_FOT_FOUND")

    if current_user.id != db_answer.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="NO_AUTH")

    answer_crud.delete_answer(db=db, db_answer=db_answer)
