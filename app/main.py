from fastapi import FastAPI
from app.db.init_db import init_db
from app.api.v1.endpoints import user


app = FastAPI(title="Shopping Wall for your shoppings")
init_db()


@app.get('/health')
def health_check():
    return {"status": "ok", "body":"A sucessful check"}





app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])