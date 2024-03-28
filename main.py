from fastapi import FastAPI

from domain.question import question_router

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"STATUS" : "WORKING_WELL..."}

app.include_router(question_router.router)