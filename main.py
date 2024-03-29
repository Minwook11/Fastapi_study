from fastapi import FastAPI

from domain.question import question_router
from domain.answer import answer_router
from domain.user import user_router


app = FastAPI()


@app.get("/health")
def health_check():
    return {"STATUS" : "WORKING_WELL..."}

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)