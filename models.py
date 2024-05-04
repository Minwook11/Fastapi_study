from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from database import Base


question_voter = Table(
    'question_voter',
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("question_id", Integer, ForeignKey("question.id"), primary_key=True)
)

answer_voter = Table(
    'answer_voter',
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("answer_id", Integer, ForeignKey("answer.id"), primary_key=True)
)


class Question(Base):
    __tablename__ = "question"
    
    id          = Column(Integer, primary_key=True)
    subject     = Column(String, nullable=False)
    content     = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    user_id     = Column(Integer, ForeignKey("user.id"), nullable=True)
    user        = relationship("User", backref="question_user")
    modify_date = Column(DateTime, nullable=True)
    voter       = relationship("User", secondary=question_voter, backref="question_voter")

    
class Answer(Base):
    __tablename__= "answer"
    
    id          = Column(Integer, primary_key=True)
    content     = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question    = relationship("Question", backref="Answer")
    user_id     = Column(Integer, ForeignKey("user.id"), nullable=True)
    user        = relationship("User", backref="answer_user")
    modify_date = Column(DateTime, nullable=True)
    voter       = relationship("User", secondary=answer_voter, backref="answer_voter")
    
    
class User(Base):
    __tablename__= "user"
    
    id       = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email    = Column(String, nullable=False, unique=True)
